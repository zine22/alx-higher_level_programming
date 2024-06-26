#!/usr/bin/python3
"""
This script connects to a MySQL database
and lists all states with a name starting with
the letter 'N'(uppercase) from the
table 'states' in the database 'hbtn_0e_0_usa'.

Usage:
    ./1-filter_states.py [MYSQL_USERNAME] [MYSQL_PASSWORD] [DATABASE_NAME]

    MYSQL_USERNAME: the username for MySQL database login
    MYSQL_PASSWORD: the password for MySQL database login
    DATABASE_NAME: the name of the database to connect to

Example:
    ./1-filter_states.py vagrant somepassword hbtn_0e_0_usa
"""

import MySQLdb
import sys

# code should not be executed when imported
if __name__ == "__main__":
    # Connect to MySQL database using provided credentials
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )

    # Create cursor object to execute SQL commands
    mycursor = db.cursor()

    # Execute SQL query to select all states whose name starts with 'N'
    mycursor.execute("SELECT * FROM states\
                     ORDER BY id ASC")

    # Fetch all rows that match the query and print them
    rows = mycursor.fetchall()
    for row in rows:
        if row[1][0] == "N":
            print(row)

    # Close the database connection and cursor
    mycursor.close()
    db.close()
