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