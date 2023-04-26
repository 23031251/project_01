# lvl_4/task_4.1.py
# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

#  Часть 1

# import sqlite3

# connection = sqlite3.connect('teacher.db')
# cursor = connection.cursor()
# query = """CREATE TABLE Students (
# Student_Id INTEGER NOT NULL PRIMARY KEY,
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL);
# """
# cursor.execute(query)
# connection.commit()

# query_ins = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# ('201','Иван','1'),
# ('202','Петр','2'),
# ('203','Анастасия','3'),
# ('204','Игорь','4')
# """
# cursor.execute(query_ins)
# connection.commit()
# connection.close()

# Часть 2
import sqlite3

def get_con():
  connection = sqlite3.connect('teacher.db')
  return connection

def close_con(connection):
  if connection:
    connection.close()

def student(student_id):
  try:
    connection = get_con()
    cursor = connection.cursor()
    zapr = """SELECT * FROM School
    JOIN Students ON School.School_Id = Students.School_Id
    WHERE Students.Student_Id = ?"""
    cursor.execute(zapr,(student_id,))
    viborka = cursor.fetchall()
    print(viborka)
    for poz in viborka:
      print ("ID студента:", poz[3])
      print ("Имя студента:", poz[4])
      print ("ID школы:", poz[0])
      print ("Название школы:", poz[1])
    close_con(connection)
  except (Exception, sqlite3.Error) as erorr:
    print ("Ошибки", erorr)
print(student(202))
