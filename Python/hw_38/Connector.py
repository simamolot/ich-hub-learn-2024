import mysql.connector


def connector(dbconfig):
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
    return connection, cursor
