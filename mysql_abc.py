import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
)
cursor = mydb.cursor()
print(mydb.connection_id)


cursor.execute("CREATE DATABASE abc")
print("Database created successfully.")

cursor.execute("USE abc")

cursor.execute("CREATE TABLE stud(id INT, name VARCHAR(32));")
print("Table created successfully.")


cursor.execute('INSERT INTO stud VALUES (1, "ramakant");')

cursor.execute('INSERT INTO stud VALUES (2, "harsh");')
print("Data inserted successfully.")


cursor.execute('UPDATE stud SET name="radha" WHERE id=2;')
print("Data update successfully.")

cursor.execute('delete from stud where id=2;')
print("Data Delete successfully.")

cursor.execute('select * from stud;')
for row in cursor:
    print(row)

    
mydb.commit()
cursor.close()
mydb.close()
