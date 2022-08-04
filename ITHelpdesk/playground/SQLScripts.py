import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port="6603",
    user="Admin",
    password="!!!Yman123!!!"
)

print(mydb)