# Stephanie Ramos
# July 5, 2023
# Database Development and Use
# Module 7.2 Movies: Table Queries

#The purpose of this script is to connect to a MySQL database and perform various queries on the movies database.

import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values

secrets = dotenv_values('.env')

config = {
    'user': secrets['USER'],
    'password': secrets['PASSWORD'],
    'host': secrets['HOST'],
    'database': secrets['DATABASE'],
    'raise_on_warnings': True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config['user'], config['host'], config['database']))

    print ()

    cursor = db.cursor()

    # Studio Table
    print("-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT * FROM studio")
    for studio in cursor.fetchall():
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}\n")
    print()

    # Genre Table
    print("-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT * FROM genre")
    for genre in cursor.fetchall():
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}\n")
    print()

    # Films under 2 hours
    print("-- DISPLAYING Short Film RECORDS --")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    for film in cursor.fetchall():
        print(f"Film Name: {film[0]}")
        print(f"Runtime: {film[1]}\n")
    print()

    # Films grouped by director
    print("-- DISPLAYING Director RECORDS in Order --")
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    for film in cursor.fetchall():
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}\n")
    print()
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
    
finally:
    db.close()
        