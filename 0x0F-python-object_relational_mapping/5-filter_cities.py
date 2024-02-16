#!/usr/bin/python3
'''Cities by states module'''
import sys
import MySQLdb


if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost', port=3306,
                          user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cr = con.cursor()
    query = '''
               SELECT cities.name FROM cities
               LEFT JOIN states
               ON cities.state_id = states.id
               WHERE states.name = "{}"
               ORDER BY cities.id ASC
            '''.format(sys.argv[4])
    if (len(sys.argv[4]) < 10):
        cr.execute(query)
        states = cr.fetchall()
        res = ''
        for i in range(len(states)):
            for city in states[i]:
                res += city
            if (i != len(states) - 1):
                res += ','
        print(res)
    cr.close()
    con.close()
