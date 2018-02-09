import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    
    return None

def create_row(conn, create_row_sql, values):
    try:
        cur = conn.cursor()
        cur.execute(create_row_sql, values)
    except Error as e:
        print(e)

def select_all_employees(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Employee")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)



def main():
    database = "db.db"
    
    sql_create_employee_table = """
        CREATE TABLE IF NOT EXISTS Employee(
            ID              INTEGER     PRIMARY KEY     NOT NULL    ,
            Fname           TEXT                        NOT NULL    ,
            Lname           TEXT                        NOT NULL
        );
    """

    sql_create_employee_row = "INSERT OR IGNORE INTO Employee(ID, Fname, Lname) VALUES(?, ?, ?);"
    
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create employee table
        create_table(conn, sql_create_employee_table)
    else:
        print("Error! DB connection unsuccessful.")

    with conn:
        # create a new employee
        values = (1, "ALYSSON", "ALVARAN")
        create_row(conn, sql_create_employee_row, values)
        
        # select all employees
        select_all_employees(conn)

if __name__ == '__main__':
    main()