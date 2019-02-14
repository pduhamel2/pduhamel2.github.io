import random
import string
import httplib2
import json
import requests

from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify, session as login_session, make_response, flash

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func, select
from database_setup import Base, Catagories, Games, User

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog App"

engine = create_engine('sqlite:///videogamescatalog.db?'
                       'check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/login')
def showLogin():
    state = ''.join(random.choice
                    (string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print ("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps
                                 ('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px; " \
                " -webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print ("done!")
    return output

# DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print ('Access Token is None')
        response = make_response(json.dumps
                                 ('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print ('In gdisconnect access token is %s'), access_token
    print ('User name is: ')
    print (login_session['username'])
    url = 'https://accounts.google.com'
    '/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print ('result is ')
    print (result)
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed'
                                 'to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
    return response

# Show the home page's JSON


@app.route('/JSON')
@app.route('/catalog/JSON')
def showHomePageJSON():
    catagories = session.query(Catagories).order_by(asc(Catagories.name))
    return jsonify(Catagories=[i.serialize for i in catagories])

# Show the current catagorie's JSON


@app.route('/catalog/<catagory>/JSON')
def displayCatagoryJSON(catagory):
    catagories = session.query(Catagories).order_by(asc(Catagories.name))
    games = session.query(Games).filter_by(catagory=catagory)
    return jsonify(Catagories=[i.serialize for i in catagories],
                   Games=[i.serialize for i in games])

# Show the current game's JSON


@app.route('/catalog/<catagory>/<game>/JSON')
def viewGameJSON(catagory, game):
    catagories = session.query(Catagories).order_by(asc(Catagories.name))
    game = session.query(Games).filter_by(name=game).one()
    return jsonify(Catagories=[i.serialize for i in catagories],
                   Games=[game.serialize])

# Show the home page for the public or a logged in user


@app.route('/')
@app.route('/catalog')
def showHomePage():
    catagories = session.query(Catagories).order_by(asc(Catagories.name))
    games = session.query(Games).order_by(func.random()).limit(10)
    if 'username' not in login_session:
        return render_template('publicindex.html', catagories=catagories,
                               games=games)
    else:
        return render_template('index.html', catagories=catagories,
                               games=games)

# Allow a logged in user to create a new catagory


@app.route('/catalog/new', methods=['GET', 'POST'])
def newCatagory():
    if 'username' not in login_session:
        return redirect('/login')
    catagories = session.query(Catagories).order_by(asc(Catagories.name))
    if request.method == 'POST':
        newCatagory = Catagories(name=request.form['catagory'],
                                 user_id=login_session['user_id'])
        session.add(newCatagory)
        session.commit()
        return(redirect(url_for('showHomePage')))
    else:
        return render_template('newcatagory.html', catagories=catagories)

# Allow a logged in user to delete their catagory


@app.route('/catalog/<catagory>/delete', methods=['GET', 'POST'])
def deleteCatagory(catagory):
    catagoryToDelete = session.query(Catagories).filter_by(name=catagory).one()
    creator = getUserInfo(catagoryToDelete.user_id)
    if 'username' not in login_session:
        return redirect('/login')
    elif creator.id != login_session['user_id']:
        return "<script>function myFunction() {alert('Only the creator of this genre is authorized to delete it.');}</script><body onload='myFunction()''>"  # noqa
    catagories = session.query(Catagories).order_by(asc(Catagories.name))
    gamesToDelete = session.query(Games).filter_by(catagory=catagory)
    if request.method == 'POST':
        session.delete(catagoryToDelete)
        for game in gamesToDelete:
            if game.catagory == catagory:
                session.delete(game)
        session.commit()
        return(redirect(url_for('showHomePage')))
    else:
        return render_template('deletecatagory.html',
                               catagories=catagories, catagory=catagory)

# Display a catagory


@app.route('/catalog/<catagory>')
def displayCatagory(catagory):
    catagories = session.query(Catagories).order_by(asc(Catagories.name))
    games = session.query(Games).filter_by(catagory=catagory)
    if 'username' not in login_session:
        return render_template('publicdisplaycatagory.html',
                               catagories=catagories, games=games,
                               catagory=catagory)
    else:
        return render_template('displaycatagory.html',
                               catagories=catagories, games=games,
                               catagory=catagory)

# Allow a logged in user to create a game


@app.route('/catalog/<catagory>/new', methods=['GET', 'POST'])
def newGame(catagory):
    if 'username' not in login_session:
        return redirect('/login')
    catagories = session.query(Catagories).order_by(asc(Catagories.name))
    if request.method == 'POST':
        newGame = Games(name=request.form['name'],
                        description=request.form['description'],
                        catagory=request.form['genres'],
                        user_id=login_session['user_id'])
        session.add(newGame)
        session.commit()
        return(redirect(url_for('showHomePage')))
    else:
        return render_template('newgame.html', catagories=catagories,
                               currentCatagory=catagory)

# Display a game


@app.route('/catalog/<catagory>/<game>')
def viewGame(catagory, game):
    catagories = session.query(Catagories).order_by(asc(Catagories.name))
    game = session.query(Games).filter_by(name=game).one()
    if 'username' not in login_session:
        return render_template('publicviewgame.html', catagories=catagories,
                               game=game)
    else:
        return render_template('viewgame.html', catagories=catagories,
                               game=game)

# Allow a logged in user to edit their game


@app.route('/catalog/<catagory>/<game>/edit', methods=['GET', 'POST'])
def editGame(catagory, game):
    editedGame = session.query(Games).filter_by(name=game).one()
    creator = getUserInfo(editedGame.user_id)
    if 'username' not in login_session:
        return redirect('/login')
    elif creator.id != login_session['user_id']:
        return "<script>function myFunction() {alert('Only the creator of this game is authorized to edit it. Please create your own game.');}</script><body onload='myFunction()''>"  # noqa
    catagories = session.query(Catagories).order_by(asc(Catagories.name))
    if request.method == 'POST':
        editedGame.name = request.form['name']
        editedGame.description = request.form['description']
        editedGame.catagory = request.form['genres']
        session.add(editedGame)
        session.commit()
        return(redirect(url_for('showHomePage')))
    else:
        return render_template('editgame.html', catagories=catagories,
                               game=editedGame)

# Allow a logged in user to delete their genre


@app.route('/catalog/<catagory>/<game>/delete', methods=['GET', 'POST'])
def deleteGame(catagory, game):
    gameToDelete = session.query(Games).filter_by(name=game).one()
    creator = getUserInfo(gameToDelete.user_id)
    if 'username' not in login_session:
        return redirect('/login')
    elif creator.id != login_session['user_id']:
        return "<script>function myFunction() {alert('Only the creator of this game is authorized to delete it.');}</script><body onload='myFunction()''>"  # noqa
    catagories = session.query(Catagories).order_by(asc(Catagories.name))
    if request.method == 'POST':
        session.delete(gameToDelete)
        session.commit()
        return(redirect(url_for('showHomePage')))
    else:
        return render_template('deletegame.html', catagories=catagories,
                               game=gameToDelete)

# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
app.run(host='0.0.0.0', port=5000)
