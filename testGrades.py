import csv
import statistics
import mysql.connector

outfile = open("output.csv",'w')
outfile_header = "First Name, Surname, Average, Grade\n"
outfile.write(outfile_header)
dbCollege = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="Livelaughlove@2020",
  database="college"
)
mycursor = dbCollege.cursor()
mycursor.execute("SELECT * FROM student")
sql_reader = mycursor.fetchall()

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
        line = "{},{},{},{}\n".format(student_first_name,student_last_name,avg_mark,grade)
        outfile.write(line)
outfile.close()        