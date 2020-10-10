import sqlite3
from Learn_DB.TestData import Test_Data


class Data_Base:

    def __init__(self, filename):
        self.filename = filename


    def get_connection(self):
        con = sqlite3.connect(self.filename)
        print('DataBase Opened')
        return con

    def create_table(self, con, table_name):
        con.execute('''CREATE TABLE IF NOT EXISTS ''' + table_name + '''(F_NAME, L_NAME, EMAIL, PWD)''')
        print('Table created')

    def insert_records(self, con, table_name, obj):
        data = '''INSERT INTO ''' + table_name + '''(F_NAME, L_NAME, EMAIL, PWD) VALUES(?, ?, ?, ?) '''
        con.execute(data, (obj.fname, obj.lname, obj.email, obj.pwd))
        con.commit()
        print('inserted the given records')

    def close_connection(self, con):
        con.close()
        print('closed the connections')


if __name__ == "__main__":
    db_obj = Data_Base('sample.db')
    con = db_obj.get_connection()
    db_obj.create_table(con, 'sample1')
    per1 = Test_Data(fname=100, lname=200, email=300, pwd=400)
    db_obj.insert_records(con, 'sample1', per1)
    db_obj.close_connection(con)
