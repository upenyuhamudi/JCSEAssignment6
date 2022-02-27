import mysql.connector

dbCollege = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="Livelaughlove@2020",
  database="college"
)
mycursor = dbCollege.cursor()
mycursor.execute("SELECT * FROM grades")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)