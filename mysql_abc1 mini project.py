import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
)
cursor = mydb.cursor()
print(mydb.connection_id)
cursor.execute("USE abc")
'''
cursor.execute("CREATE DATABASE abc")
print("Database created successfully.")



cursor.execute("CREATE TABLE stud1(id INT, name VARCHAR(32));")
print("Table created successfully.")


'''
def insert(rn, name):
    cursor.execute(f'insert into stud1 values({rn},"{name}")')
    print("Data Inserted Succesfully")
def update(rn,name):
    cursor.execute(f'update stud1 set name="{name}" where id={rn};')
    print("Data Updated Succesfully")

def delete(rn):
    cursor.execute(f'delete from stud1 where id={rn};')
    print("Data Delete Succesfully")

def show():
    cursor.execute('select * from stud1;')
    for row in cursor:
         print(row)

while True:
    print('======= Student Record =======')
    print('1. Inserted Record')
    print('2. Updated Record')
    print('3. Deleted Record')
    print('4. Show All Record')
    print('5. Exit.....')

    choice=int(input('Enter Your Choice 1 To 5 :'))

    if choice==1:
        rn=int(input('Enter your ID no :'))
        name=input('Enter your name :')
        insert(rn, name)
        
    elif choice==2:
        rn=int(input('Enter your ID no :'))
        name=input('Enter your name :')
        update(rn,name)

    elif choice==3:
          rn=int(input('Enter your ID no :'))
          delete(rn)

    elif choice==4:
         show()
         
         
    elif choice==5:
        print('Exiting project')
        break
    else:
        print('Enter valide choice /n')
    



    
mydb.commit()
cursor.close()
mydb.close()
