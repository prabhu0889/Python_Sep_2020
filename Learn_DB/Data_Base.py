import sqlite3

# create connection
con = sqlite3.connect('database.db')
print('Create DB')
#********************************************************************************
# Create Table in databasee.db
con.execute('''CREATE TABLE IF NOT EXISTS leaf_db(  NAME, 
                                                    USERNAME, 
                                                    EMAIL, 
                                                    PASSWORD)''')
print('Table Created')
#********************************************************************************

# Insert the records
con.execute('''INSERT INTO leaf_db(NAME, USERNAME, EMAIL, PASSWORD)
                VALUES('Babu', 'Babu123', 'babu@gmail.com', 654321) ''')
con.commit()
print('Inserting records')
#********************************************************************************

# update the records
qr = '''UPDATE leaf_db set USERNAME = 'Babu321' WHERE NAME='Babu' '''
con.execute(qr)
con.commit()
#********************************************************************************
# fetch all values
data = con.execute(''' SELECT * FROM leaf_db''')
print(data)

for i in data:
    print(i)
#********************************************************************************

# close the connection
con.close()
print('close DB')