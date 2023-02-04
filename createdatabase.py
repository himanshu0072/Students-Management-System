# create database
import pymysql as ms


con = ms.connect(host="localhost", user="root", password="Himanshu", database="test")
cur = con.cursor()


# creating employee table
mycursor=con.cursor()
mycursor.execute("create database stm")
mycursor.execute("use stm")
mycursor.execute('create table students (roll_no int(100) primary key, name varchar(100) not null, email varchar(100) not null, gender varchar(100) not null, contact varchar(100) not null, dob varchar(100) not null, address varchar(100) not null)')

