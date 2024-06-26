#!/usr/bin/python3
"""
Connects to a MySQL database,
executes a SELECT query to fetch all rows from the 'states' table,

and filters the results to only include rows
where the 'name' column matches the 'state_name' parameter.
Prints the filtered rows to stdout.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # connect to MySQLdb database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )

    # Create cursor object to execute SQL queries
    mycursor = db.cursor()

    # Execute SELECT query to fetch all rows from the 'states' table
    mycursor.execute("SELECT * FROM states WHERE BINARY name='{}'\
                    ORDER BY id ASC".format(sys.argv[4]))

    # Fetch all rows from the SELECT query
    rows = mycursor.fetchall()

    # Loop through each row
    # check if the 'name' column matches the 'state_name' parameter
    for row in rows:
        print(row)

    # Close cursor and database connections
    mycursor.close()
    db.close()
