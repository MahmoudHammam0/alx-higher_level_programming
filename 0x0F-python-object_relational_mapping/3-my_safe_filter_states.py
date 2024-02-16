#!/usr/bin/python3
'''Get all states module'''
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = 'SELECT * FROM states WHERE BINARY name = "{}" ORDER BY id ASC'.\
            format(sys.argv[4])
    if (len(sys.argv[4]) < 10):
        cur.execute(query)
        states = cur.fetchall()
        for state in states:
            print(state)
    cur.close()
    db.close()
