# create a database
import sqlite3
conn = sqlite3.connect('article.db')
c=conn.cursor()
conn.close
# create a table 
import sqlite3
conn = sqlite3.connect('article.db')
c=conn.cursor()
c.execute("create table exa(Software VARCHAR, Version Real,Price Real )")
# Inserting a data into the table

c.execute("Insert into exam Values('Python',3.4,'100')")
c.execute("Insert into exam Values('Adobe',10.2,'1000')")
c.execute("Insert into exam Values('Office',16,'1000')")
# read the data  from the database


sql = "SELECT * FROM exam"
for row in c.execute(sql):
    print("Software: " + row[0])
    print("Version: " + str(row[1]))
    print("Price: " + str(row[2]))

# insert data dynamically in a database

def dynamic_data():
   soft = input("Write Software Name : ")
   version = input("Write Versio : ")
Price= input("Write Price")

c.execute("insert into exa(Software,Version,Price) values(?,?,?)" ,(soft,version,Price))
conn.commit()
dynamic_data()

# update the data
sql="update exa set Version = 3.5 where Software = 'Python'"
c.execute(sql)
sql = "select * from example"

for row in c.execute(sql):
    print(row)
# Delete operation on database

sql="delete from exa where Software = 'Python'"
c.execute(sql)
sql = "select * from example"
for row in c.execute(sql):
    print(row)



