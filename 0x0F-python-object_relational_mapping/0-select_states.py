#!/usr/bin/python3
""" Module that selects the column from a database """
import MySQLdb
import sys


def main():
    """
    Connects to a database and retrieve the states
    """
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    query = """ SELECT states.id, states.name
                FROM states
                ORDER BY states.id ASC
                """

    cursor = db.cursor()
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
