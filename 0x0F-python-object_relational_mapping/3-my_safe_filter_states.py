#!/usr/bin/python3
""" Module that searches the database for a row that is specified by the user
    """
import MySQLdb
import sys


def main():
    """
    Connects to a database and retrieve the states
    that starts with a capital letter N.
    """
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    query = """ SELECT states.id, states.name
                FROM states
                WHERE states.name = %s
                ORDER BY states.id ASC
                """

    cursor = db.cursor()
    cursor.execute(query, (sys.argv[4],))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
