#!/usr/bin/python3
'''Cities by states module'''
import sys
import MySQLdb


if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost', port=3306,
                          user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cr = con.cursor()
    query = '''
               SELECT cities.id, cities.name, states.name FROM cities
               LEFT JOIN states
               ON cities.state_id = states.id
               ORDER BY cities.id ASC
            '''
    cr.execute(query)
    cities = cr.fetchall()
    for city in cities:
        print(city)
    cr.close()
    con.close()
