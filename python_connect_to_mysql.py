import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='Kanniyamma@03',database='python_mysql_db')

if conn:
    print("success done")
else:
    print("error")


def insert(ename, age, designation):
    res = conn.cursor()
    sql = "insert into employee (ename,age,designation) values (%s,%s,%s)"
    user = (ename,age,designation)
    res.execute(sql, user)
    conn.commit()
    print("Data Insert Success")
   
    
def update(ename, age, designation, e_id):
    res = conn.cursor()
    sql = "update employee set ename=%s,age=%s,designation=%s where e_id=%s"
    user = (ename, age, designation, e_id)
    res.execute(sql, user)
    conn.commit()
    print("Data Update Success")

def select():
    res = conn.cursor()
    sql = "select e_id,ename,age,designation from employee"
    res.execute(sql)
    # result=res.fetchone()
    # result=res.fetchmany(2)
    result = res.fetchall()
    print(result)

def delete(e_id):
    res = conn.cursor()
    sql = "delete from employee where e_id=%s"
    user = (e_id,)
    res.execute(sql, user)
    conn.commit()
    print("Data Delete Success")


while True:
    print("1.insert data")
    print("2.update data")
    print("3.select data")
    print("4.delete data")
    print("5.exit")

    choice = int(input("enter your choice : "))

    if choice==1:
        ename = input("enter name : ")
        age = input("enter age : ")
        designation = input("enter designation : ")
        insert(ename, age, designation)

    elif choice==2:
        e_id = input("enter id : ")
        ename = input("enter name : ")
        age = input("enter age : ")
        designation = input("enter designation : ")
        update(ename, age, designation, e_id)

    elif choice==3:
        select()

    elif choice==4:
        e_id = input("enter id : ")
        delete(e_id)

    elif choice==5:
        quit()

    else:
        print("invalid choice")


