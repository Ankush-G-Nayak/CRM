import mysql.connector
database= mysql.connector.connect(
    host='localhost',
    user ='root',
    passwd='RandomPassword',
)
#cursor obj prep
CursorObject=database.cursor()

# Create db
CursorObject.execute('CREATE DATABASE Sekiro')