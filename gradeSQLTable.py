import mysql.connector

dbCollege = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="Livelaughlove@2020",
  database="college"
)
mycursor = dbCollege.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)