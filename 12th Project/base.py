import mysql.connector() as x

con = x.connector(host = 'localhost', user = 'kai', password = 'a')

if con.is_connected():
    print("Connected !")
