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
                
#TO UPDATE NAME(CHOICE 1) 
        if ch1==1:
            mycursor.execute("select * from main_lib")
            for i in mycursor:
                print(i)
            cardno=str(input("Enter card no:"))
            name_of_person=str(input("Enter new name:"))
            mycursor.execute("update main_lib set name_of_person='"+name_of_person+"' where cardno='"+cardno+"'")
            mydb.commit()
            print("Name has been updated")
            mycursor.execute("select * from main_lib")
            for i in mycursor:
                print(i)
                
#TO UPDATE PHONE NUMBER(CHOICE 2)            
        elif ch1==2:
            mycursor.execute("select * from main_lib")
            for i in mycursor:
                print(i)
            cardno=str(input("Enter card no:"))
            phone_no=str(input("Enter new phone no:"))
            mycursor.execute("update main_lib set phone_no='"+phone_no+"' where cardno='"+cardno+"'")
            mydb.commit()
            print("Phone Number has been updated")
            mycursor.execute("select * from main_lib")
            for i in mycursor:
                print(i)
                                
#TO UPDATE ADDRESS(CHOICE 3)
        elif ch1==3:
            mycursor.execute("select * from main_lib")
            for i in mycursor:
                print(i)
            cardno=str(input("Enter card no:"))
            address=str(input("Enter new address:"))
            mycursor.execute("update main_lib set address='"+address+"' where cardno='"+cardno+"'")
            mydb.commit()
            print("Address has been updated")
            mycursor.execute("select * from main_lib")
            for i in mycursor:
                print(i)

#TO UPDATE DATE OF BIRTH(CHOICE 4)           
        elif ch1==4:
            mycursor.execute("select * from main_lib")
            for i in mycursor:
                print(i)
            cardno=str(input("Enter card no:"))
            dob=str(input("Enter new date of birth(yyyy-mm-dd):"))
            mycursor.execute("update library_master set dob='"+dob+"' where cardno='"+cardno+"'")
            mydb.commit()
            print("Date of birth has been updated")
            mycursor.execute("select * from main_lib")
            for i in mycursor:
                print(i)
                     
#TO DELETE AN ACCOUNT(QUERY 4)              
    elif ch==4:
        mycursor.execute("select * from main_lib ")
        for i in mycursor:
                print(i)
        cardno=str(input("Enter card no:"))
        mycursor.execute("delete from main_lib where cardno='"+cardno+"'")
        mydb.commit()
        print("Account removed succesfully")
        mycursor.execute("select * from main_lib")
        for i in mycursor:
                print(i)
                                
#TO ADD NEW BOOK(QUERY 5)              
    elif ch==5:
        print("FILL ALL BOOK DETAILS ")
        book_name=str(input("enter book  name:"))
        book_no=str(input("Enter no (max 5 characters):"))
        genre=str(input("Enter genre:"))
        authors_name=str(input("Enter the authors name (max 15 words):"))
        language=str(input("Enter the language of book:"))
        mycursor.execute("insert into books values('"+book_name+"','"+book_no+"','"+genre+"','"+authors_name+"','"+language+"')")
        mydb.commit()
        print("Book added succesfully")
        for i in mycursor:
            print(i)
                    
#TO SEE BOOK DETAILS(QUERY 6)     
    elif ch==6:
        book_no=str(input("Enter Book No:"))
        mycursor.execute("select  *  from books where book_no='"+book_no+"'")
        for i in mycursor:
            print(i)
                        
#TO UPDATE BOOK DETAILS(QUERY 7)         
    elif ch==7:
        print("Press 1 to update Book name")
        print()
        print("Press 2 to update Genre")
        print()
        print("Press 3 to update Author Name")
        print()
        print("Press 4 to update Language")
        print()
        ch1=int(input("Enter your choice:"))
        
#TO UPDATE BOOK NAME(CHOICE 1)
        if ch1==1:
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
            book_no=str(input("Enter book no:"))
            name_of_book=str(input("Enter new name:"))
            mycursor.execute("update books set book_name='"+name_of_book+"' where book_no='"+book_no+"'")
            mydb.commit()
            print("Name has been updated")
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
                
#TO UPDATE GENRE(CHOICE 2)              
        elif ch1==2:
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
            book_no=str(input("Enter book no:"))
            genre=str(input("Enter new genre:"))
            mycursor.execute("update books set genre='"+genre+"' where book_no='"+book_no+"'")
            mydb.commit()
            print("Genre has been updated")
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
                                
#TO UPDATE AUTHOR NAME(CHOICE 3)               
        elif ch1==3:
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
            book_no=str(input("Enter book no:"))
            author=str(input("Enter new author's name:"))
            mycursor.execute("update books set authors_name='"+author+"' where book_no='"+book_no+"'")
            mydb.commit()
            print("Author's name has been updated")
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
                
#TO UPDATE LANGUAGE(CHOICE 4)            
        elif ch1==4:
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
            book_no=str(input("Enter book no:"))
            language=str(input("Enter new language:"))
            mycursor.execute("update books set language='"+language+"' where book_no='"+book_no+"'")
            mydb.commit()
            print("Language has been updated")
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
                                
#TO DELETE A BOOK(QUERY 8)              
    elif ch==8:
        mycursor.execute("select * from books")
        for i in mycursor:
            print(i)
        book_no=str(input("Enter book no:"))
        mycursor.execute("delete from books where book_no='"+book_no+"'")
        mydb.commit()
        print("Details of book removed succesfully")
        mycursor.execute("select * from books")
        for i in mycursor:
            print(i)
                        
#TO LEND A BOOK(QUERY 9)           
    elif ch==9:
        print("To go back press 1")
        print()
        print("To continue press 2")
        print()
        a=int(input("Enter your choice:"))
        if a==1:
            continue
        if a==2:
            cardno=str(input("Enter card no:"))
            book_name=str(input("Enter the name of the book:"))
            dateoflend=str(input("Enter date of lending(yyyy-mm-dd)"))
            dateofreturn=str(input("enter date of return(yyyy-mm-dd):"))    
            mycursor.execute("insert into library_trans values('"+cardno+"','"+book_name+"','"+dateoflend+"','"+dateofreturn+"')")
            mydb.commit()
                        
#TO RETURN A BOOK(PART OF UPDATION)(QUERY 10)           
    elif ch==10:
        print("To go back press 1")
        print()
        print("To continue press 2")
        print()
        a=int(input("enter your choice:"))
        if a==1:
            continue
        if a==2:
            cardno=str(input("Enter card no:"))
            date_of_return=str(input("Enter date of return(yyyy-mm-dd):"))
            mycursor.execute("update library_trans set dateofreturn='"+date_of_return+"' where cardno='"+cardno+"'")
            mydb.commit()
                        
#TO SEE LENDING HISTORY(QUERY 11)          
    elif ch==11:
        cardno=str(input("Enter card no:"))
        mycursor.execute("select  *  from library_trans where cardno='"+cardno+"'")
        for i in mycursor:
         print(i)
                     
#TO ORDER A NEW BOOK(QUERY 12)
    elif ch==12:
        orderno=str(input("Enter the order no:"))
        name_of_book=str(input("Enter the name of the book:"))
        del_date=str(input("Enter the expected delivery date of books(yyyy-mm-dd):"))
        price=str(input("Enter the price of the book"))
        mycursor.execute("insert into buy_new_books values('"+orderno+"','"+name_of_book+"','"+del_date+"','"+price+"')")
        mydb.commit()
                
#TO UPDATE ORDER DETAILS(QUERY 13)       
    elif ch==13:
        print("Press 1 to update name of book")
        print() 
        print("Press 2 to update delivery date")
        print()
        print("Press 3 to update price")
        print()
        ch1=int(input("Enter your choice:"))
                
#TO UPDATE BOOK NAME(CHOICE 1)        
        if ch1==1:
            mycursor.execute("select * from buy_new_books")
            for i in mycursor:
                print(i)
            orderno=str(input("Enter order no:"))
            name_of_book=str(input("Enter new name:"))
            mycursor.execute("update buy_new_books set name_of_book='"+name_of_book+"' where orderno='"+orderno+"'")
            mydb.commit()
            print("Name has been updated")
            mycursor.execute("select * from buy_new_books")
            for i in mycursor:
                print(i)
                
#TO UPDATE DELIVERY DATE(CHOICE 2)               
        elif ch1==2:
            mycursor.execute("select * from buy_new_books")
            for i in mycursor:
                print(i)
            orderno=str(input("Enter card no:"))
            del_date=str(input("Enter new delivery date(yyyy-mm-dd):"))
            mycursor.execute("update buy_new_books set del_date='"+del_date+"' where orderno='"+orderno+"'")
            mydb.commit()
            print("Delivery date has been updated")
            mycursor.execute("select * from buy_new_books")
            for i in mycursor:
                print(i)
                               
#TO UPDATE PRICE(CHOICE 3)               
        elif ch1==3:
            mycursor.execute("select * from buy_new_books")
            for i in mycursor:
                print(i)
            orderno=str(input("Enter card no:"))
            price=str(input("Enter new price:"))
            mycursor.execute("update buy_new_books set price='"+price+"' where orderno='"+orderno+"'")
            mydb.commit()
            print("Price has been updated")
            mycursor.execute("select * from buy_new_books")
            for i in mycursor:
                print(i)