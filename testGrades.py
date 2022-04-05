import statistics
from time import asctime
import mysql.connector
import logging

logging.basicConfig(filename='grades.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

dbCollege = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="Livelaughlove@2020",
  database="college"
)
mycursor = dbCollege.cursor()
mycursor.execute("SELECT * FROM student")
sql_reader = mycursor.fetchall()
sql_grades = "INSERT INTO grades (Firstname, Surname, Average, Grade) VALUES (%s,%s,%s,%s)"

for line in sql_reader:
        student_first_name = line[1]
        student_last_name = line[2]
        marks = line[3:7]
        marks_list = [int(i) for i in marks]
        avg_mark = round(statistics.mean(marks_list),1)
        if avg_mark >=80:
            grade = "A"
        elif avg_mark >=70:
            grade = "B"
        elif avg_mark >=60:
            grade = "C"
        elif avg_mark >=50:
            grade = "D"
        elif avg_mark >=40:
            grade = "E"
        elif avg_mark >=0:
            grade = "F"          
        val = [(student_first_name,student_last_name,avg_mark,grade)]
        
        #Logging to check if correct names are added to database
        logging.info('Created student record: {} {}'.format(student_first_name,student_last_name))

        #Logging to check if average marks match the grades
        logging.debug('Created average marks and grades check: {} - {}'.format(avg_mark,grade))
    
        mycursor.executemany(sql_grades, val)
        
dbCollege.commit()


       