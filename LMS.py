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

while True:
    
    print("1-Create a new account")
    print("2-See the account info")
    print("3-Update card holder info")
    print("4-Delete account")
    print("5-Add new books")
    print("6-See all books")
    print("7-Update book details")
    print("8-Delete book")
    print("9-Lend a book")
    print("10-Return book")
    print("11-Display lending history")
    print("12-Order new book")
    print("13-Update order details")
    print("14-Display order history")
    print("15-EXIT the program")
    ch=int(input("enter your choice"))
    

#TO CREATE A NEW LIBRARY ACCOUNT(QUERY 1)
    if ch==1:
        print("To go back press 1")
        print()     
        print("To continue press 2")
        print()
        a=int(input("enter your choice:"))
        if a==1:
            continue
        if a==2:
            print("FILL ALL PERSONAL DETAILS OF ACCOUNT HOLDER")
            cardno=str(input("enter card no:"))
            name_of_person=str(input("Enter name:"))
            phone_no=str(input("Enter phone no:"))
            address=str(input("Enter the address(max 30 words):"))
            dob=str(input("Enter the date of birth(yyyy-mm-dd):"))
            mycursor.execute("insert into main_lib values('"+cardno+"','"+name_of_person+"','"+phone_no+"','"+address+"','"+dob+"')")
            mydb.commit()
            print("ACCOUNT IS SUCCESSFULLY CREATED!!!!")
                        
#TO SEE DETAILS OF CARD HOLDER(QUERY 2)
    
    elif ch==2:
        cardno=str(input("Enter card no:"))
        
        mycursor.execute("select  *  from main_lib where cardno='"+cardno+"'")
        data=mycursor.fetchall()
        if data==[]:
            print("No record found")
        else:
            print(data)
                        
#TO UPDATE CARD HOLDER INFORMATION(QUERY 3)            
    elif ch==3:
         
        print("Press 1 to update name:")
        print()
        print("Press 2 to update phone no:")
        print()
        print("Press 3 to update address:")
        print()
        print("Press 4 to update date of birth:")
        print()
        ch1=int(input("Enter your choice:"))