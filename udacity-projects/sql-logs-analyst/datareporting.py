#!/usr/bin/env python3
#
# Internal reporting tool for news article data

import psycopg2

DBNAME = "news"

"""Query the news database and print the
top 3 articles along with their views."""


def print_top3_articles():

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = "select title, count(path) from log, articles where path like '%'|| articles.slug group by path, title order by count(path) desc limit 3;"  # noqa
    c.execute(query)
    rows = c.fetchall()
    print ("Top Three Articles:")
    for row in rows:
        print("\"" + row[0] + "\" - " + str(row[1]) + " views")
    db.close()
    print ("\n")

"""Query the news database and print the
authors rankings along with their views."""


def print_author_rankings():

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = "select name, count(path) as views from log, author_slug where path like '%'|| slug group by name order by count(path) desc;"  # noqa
    c.execute(query)
    rows = c.fetchall()
    print ("Author Rankings:")
    for row in rows:
        print(row[0] + " - " + str(row[1]) + " views")
    db.close()
    print ("\n")

"""Query the news database and print any days where
there were more that 1% page request errors."""


def print_high_error_dates():

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = "select count(status) as views, errors,  time::date as date from log, error_dates where time::date = error_dates.date group by time::date, errors order by time::date;"  # noqa
    c.execute(query)
    rows = c.fetchall()
    print ("Days with more than 1% request errors:")
    for row in rows:
        error_percentage = float(row[1]) / float(row[0]) * 100
        if error_percentage > 1:
            print(str(row[2]) + " - " +
                  str(int(error_percentage)) + "% errors")
    db.close()
    print ("\n")

print_top3_articles()
print_author_rankings()
print_high_error_dates()
