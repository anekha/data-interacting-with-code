# pylint: disable=missing-docstring, C0103

def directors_count(db):
    # return the number of directors contained in the database
    query = "SELECT COUNT(name) FROM directors"
    db.execute(query)
    results = db.fetchall()
    return int(results[0][0])


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = "SELECT name FROM directors ORDER BY name "
    db.execute(query)
    results = db.fetchall()
    end_names = []
    for i in results:
        end_names.append(i[0])
    return end_names
        #return end_names.append(i[0])



def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query =  """SELECT title
            FROM movies
            WHERE UPPER(movies.title) LIKE 'LOVE %'
            OR UPPER(movies.title) LIKE '% LOVE'
            OR UPPER(movies.title) LIKE '% LOVE %'
            OR UPPER(movies.title) LIKE '%, LOVE %'
            OR UPPER(movies.title) LIKE '% LOVE, %'
            OR UPPER(movies.title) LIKE '%, LOVE %'
            OR UPPER(movies.title) LIKE '%. LOVE %'
            OR UPPER(movies.title) LIKE '% LOVE. %'
            OR UPPER(movies.title) LIKE '% LOVE. '
            OR UPPER(movies.title) LIKE "%' LOVE %"
            OR UPPER(movies.title) LIKE "% LOVE' %"
            ORDER BY title
            """
    db.execute(query)
    results = db.fetchall()
    return results


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    #How many directors contain a word, given by a user, in their name?
    query = """SELECT count(name)
            FROM directors
            WHERE UPPER(name) LIKE ?
            """
    db.execute(query, (f"%{name}%",)) # <- Will replace "?" in the query with %keyword%
    rows = db.fetchall()
    return int(rows[0][0])


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    t = (min_length, )
    query = """ SELECT title
            FROM movies
            WHERE minutes > ?
            ORDER BY title
            """
    db.execute(query, t)
    results = db.fetchall()
    end_names = []
    for i in results:
        end_names.append(i[0])
    return end_names

import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()
#print(directors_count(db))
#print(directors_list(db))
#print(love_movies(db))
print(directors_named_like_count(db, 'Lang'))
#print(movies_longer_than(db, 300))
