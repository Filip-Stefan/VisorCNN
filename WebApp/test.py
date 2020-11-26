import mysql.connector
import sys


cnx = mysql.connector.connect(user='salut', password='',
                              host='127.0.0.1',
                              port='3308',
                              database='visor')

sql_select_Query =  sys.argv[1]
cursor = cnx.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()

print(records)

cnx.close()