# Stephanie Ramos
# July 5, 2025
# Database Development and Use
# Module 8.2 Movies: Update and Delete

# The purpose of this script is to connect to a MySQL database, display films, insert a new film, update an existing film's genre, and delete a film from the database.
import mysql.connector
from mysql.connector import errorcode
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
    cursor = db.cursor()

    def show_films(cursor, title):
        cursor.execute("""
            SELECT film_name AS 'Film Name',
                    film_director AS 'Director',
                    genre_name AS "Genre Name",
                    studio_name AS 'Studio Name'
            FROM film
            INNER JOIN genre ON film.genre_id = genre.genre_id
            INNER JOIN studio ON film.studio_id = studio.studio_id
        """)
        films = cursor.fetchall()

        print("\n-- {} --".format(title))

        for film in films:
            print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name ID: {}\n".format(
                film[0], film[1], film[2], film[3]))
    
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new film 
    cursor. execute("""
        INSERT INTO film (
            film_name,
            film_releaseDate,
            film_runtime,
            film_director,
            studio_id,
            genre_id
        )
        VALUES (
            'The Notebook',
            '2004',
            123,
            'Nick Cassavetes',
            1,
            3
        )
    """)
    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
    
    # Update Alien's genre to Horror
    cursor.execute("""
        UPDATE film
        SET genre_id = 1
        WHERE film_name = 'Alien'
    """)
    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

    # Delete the film 'Gladiator'
    cursor.execute("""
        DELETE FROM film
        WHERE film_name = 'Gladiator'
    """)
    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    cursor.close()
    db.close()


