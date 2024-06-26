#!/usr/bin/python3
"""
Connects to a MySQL database and retrieves rows
from the 'cities' and 'states' tables,
joining them on the 'state_id' column to get the corresponding state names.
Prints the 'id' and 'name' columns of the resulting joined table.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQLdb database using command line arguments
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )

    # Create cursor object to execute SQL queries
    mycursor = db.cursor()

    # Execute SELECT query to join 'cities' and 'states' tables on 'state_id'
    mycursor.execute("SELECT cities.id, cities.name,\
                      states.name FROM cities\
                      INNER JOIN states\
                      ON states.id=cities.state_id")

    # Fetch all rows from the SELECT query
    rows = mycursor.fetchall()

    # Loop through each row and print the 'id' and 'name' columns
    lst = []
    for row in rows:
        if row[2] == sys.argv[4]:
            lst.append(row[1])

    print(", ".join(lst))

    # Close cursor and database connections
    mycursor.close()
    db.close()
