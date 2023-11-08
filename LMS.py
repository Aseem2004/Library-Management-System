#CODE FOR LIBRARY(PYTHON+MYSQL)
print("LIBRARY DATABASE")

#CREATING DATABASE
import mysql.connector as sqltor
#import datetime
import sys
mydb=sqltor.connect(host="localhost",user="root",passwd="As@010104")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists library")
mycursor.execute("use library")

#CREATING  ALL REQUIRED TABLES

mycursor.execute("create table if not exists main_lib(cardno char(10) primary key,name_of_person varchar(30),phone_no char(10),address varchar(30),dob date)")
mycursor.execute("create table if not exists books  (book_name varchar(30),book_no char(5) primary key,genre varchar(10),authors_name varchar(15),language varchar(15))")
mycursor.execute("create table if not exists library_trans(cardno char(10),foreign key(cardno) references main_lib(cardno),book_name varchar(20),dateoflend date,dateofreturn date)") 
mycursor.execute("create table if not exists buy_new_books(orderno varchar(6) primary key,name_of_book varchar(20),del_date date,price char(4))")
mydb.commit()
