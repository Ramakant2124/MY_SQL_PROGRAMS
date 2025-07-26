import mysql.connector

def insert(ern, ename, dept, salary):
    cursor.execute(f'insert into Emp values({ern},"{ename}","{dept}",{salary})')
    print("Data Inserted Succesfully")
    
def update(ern,ename, dept, salary):
    cursor.execute(f'update Emp set name="{ename}","{dept}",{salary} where id={ern};')
    print("Data Updated Succesfully")

def delete(ern):
    cursor.execute(f'delete from Emp where id={ern};')
    print("Data Delete Succesfully")

def show():
    cursor.execute('select * from Emp;')
    for row in cursor:
         print(row)

try:         
    # Connect to MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
    )
    cursor = mydb.cursor()
    print(mydb.connection_id)
    cursor.execute("USE abc")
    
    #cursor.execute("CREATE DATABASE abc")
    #print("Database created successfully.")



    #cursor.execute("CREATE TABLE Emp(eid INT primary key, ename VARCHAR(32),dept varchar(32),salary float);")
    #print("Table created successfully.")


    while True:
        print('======= Employee Record =======')
        print('1. Inserted Record')
        print('2. Updated Record')
        print('3. Deleted Record')
        print('4. Show All Record')
        print('5. Exit.....')

        choice=int(input('Enter Your Choice 1 To 5 :'))

        if choice==1:
            ern=int(input('Enter your ID no :'))
            ename=input('Enter your name :')
            dept=input('Enter your department :')
            salary=float(input('Enter your salary :'))
            insert(ern, ename, dept, salary)
            
        elif choice==2:
            rn=int(input('Enter your ID no :'))
            name=input('Enter your name :')
            dept=input('Enter your department :')
            salary=float(input('Enter your salary :'))
            update(ern, ename, dept, salary)

        elif choice==3:
              rn=int(input('Enter your ID no :'))
              delete(ern)

        elif choice==4:
             show()
             
             
        elif choice==5:
            print('Exiting project')
            break
        else:
            print('Enter valide choice /n')
except mysql.connector.Error as err:
    print("MYSQL Error :",err)



finally:
    mydb.commit()
    cursor.close()
    mydb.close()
         
