from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="sash",database="pdbc")
# cursor = con.cursor()
# sql = "select * from users"
# cursor.execute(sql)
# result = cursor.fetchall()
# print()

# we need to insert,delete,update 
# connection.commit



def insert(name,age,city):
    cur = con.cursor()
    sql = "insert into users(name,age,place) values(%s,%s,%s)"
    user = (name,age,city)
    cur.execute(sql,user)
    con.commit()

def update(id,name,age,city):
    cur = con.cursor()
    sql = "update users set name=%s,age=%s,place=%s where id=%s"
    user = (name,age,city,id)
    cur.execute(sql,user)
    con.commit()

def delete(id):
    cur = con.cursor()
    sql = "delete from users where id = %s"
    user = tuple(id)
    cur.execute(sql,user)
    con.commit()

def select():
    cur = con.cursor()
    sql = "select * from users"
    cur.execute(sql)
    result = cur.fetchall()
    #print(result)
    print(tabulate(result,headers=["Id","Name","Age","Place"]))

while True:
    print("1 to insert")
    print("2 to update")
    print("3 to select")
    print("4 to delete")
    print("5 to Exit")
    c = int(input("Enter Your Option: "))
    if c == 1:
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        city = input("Enter City: ")
        insert(name,age,city)
        print("Data successfully inserted")
    elif c == 2:
        id = input("Enter id: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        city = input("Enter City: ")
        update(id,name,age,city)
        print("Data successfully Updated")
    elif c==3:
        select()
    elif c==4:
        id = input("Enter id: ")
        delete(id)
        print("Data successfully Deleted")
    elif c==5:
        break
    else:
        print("OOPs Enter correct Option... ")
