Video Games Catalog
===================

## Project Description:
This web application provides a list of games within a variety of categories and integrates third party user registration and authentication with Google sign in. Once authenticated, users have the ability to post, edit, and delete their own games, as well as create new catagories. The technologies used in this project are: HTML, CSS, SQLite, Python, Flask, and SQLAlchemy.

## Viewing This Applications Functionality:
I have included a folder called screenshots, which has several pictures showing the applications functionality. This way you do not have to install the dependencies to see it working.

## Dependencies:
* [Python](https://www.python.org/downloads/) 3.6 or higher installed.
* [Flask](https://pypi.org/project/Flask/) 1.0.2 or higher installed.
* [SQLAlchemy](https://www.sqlalchemy.org/download.html) 1.2.7 or higher installed.

## Running The Application:
* Prepare the database:
 1. Download the catalog folder.
 2. Open a terminal or Git bash window and change directories to the catalog folder.
 3. Enter `python database_setup.py` to create the database.
 4. Once the database is created you can populate it by entering `python populate_database.py`.
 5. Enter `python catalog_app.py` to run the web application.
 6. Open a web browser and enter the URL `http://localhost:5000/`
 9. To stop the application enter `ctrl+c` in terminal or bash window where the application is running.

* Using The Application:
 1. To sign in and make changes click the orange Login button in the top right corner.
 2. Click the blue Google Sign in button
 3. Sign in with your Google account.
 4. You will now see links on each page that allow you to create, edit, and delete.
 6. To disconnect your Google account, click the orange Logout button in the top right corner.

## File Manifest
* catalog_app.py
* database_setup.py
* populate_database.py
* client_secrets.JSON
* README.md
* static
  * style.css
* templates
  * deletecatagory.html
  * deletegame.html
  * displaycatagory.html
  * editgame.html
  * index.html
  * layout.html
  * login.html
  * newcatagory.html
  * newgame.html
  * publicdisplaycatagory.html
  * publicindex.html
  * publicviewgame.html
  * viewgame.html
* screenshots
  * 01-home.png
  * 02-actions-games.png
  * 03-game-description.png
  * 04-google-oath2-login.png
  * 05-home-authenticated.png
  * 06-action-games-authenticated.png
  * 07-game-description-authenticated
  * 08-new-game-genre.png
  * 09-add-game.png
  * 10-edit-game.png
  * 11-delete-game.png
  * 12-google-oath2-logout.png