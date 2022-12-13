#!/usr/bin/python3
"""script that lists all states statrts N """
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    my_db = MySQLdb.connect(host='localhost',
                            port=3306,
                            user=user
                            code=password
                            database=my_db)
    cursor = my_db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER BY id ASC")
    For state in cursor.fetchall():
        print(i)
