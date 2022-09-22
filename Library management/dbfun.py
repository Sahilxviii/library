import pymysql as p

def create_con():
    con=p.connect(user="root", password="", host="localhost", database="Library")
    return con

# function to keep emails unique in sql table
def email_check(e):
    con=create_con()
    cur=con.cursor()
    print(e)
    q = f"SELECT id FROM Login WHERE Email = '{e}'"
    cur.execute(q)
    id = cur.fetchone()
    print(id)
    return id

def insert_fun(t):
    con=create_con()
    cur=con.cursor()

    q="INSERT INTO Login (Email, Password, UserName, Role) values (%s, %s, %s, %s)"
    cur.execute(q,t)
    
    con.commit()
    con.close()

def access(t):
    con = create_con()
    cur = con.cursor()

    q = "SELECT Id, Role FROM Login WHERE Email = %s AND Password = %s"
    cur.execute(q,t)
    a = cur.fetchone()
    return a

def library():
    con = create_con()
    cur = con.cursor()

    q = "select * from library"
    cur.execute(q)
    data = cur.fetchall()
    return data

def fetch_spec(id):
    con=create_con()
    cur=con.cursor()

    q = f"select * from library where id = {id}"
    cur.execute(q)
    data=cur.fetchone()
    return data

def update(t):
    con=create_con()
    cur=con.cursor()

    q = "UPDATE library SET Book_name = %s, Author_name = %s , Publisher_name = %s, pages = %s, price = %s WHERE Id = %s" 
    cur.execute(q,t)
    con.commit()
    con.close()

def delete(id):
    con=create_con()
    cur=con.cursor()
    q = f"DELETE FROM Library where id = {id}"
    cur.execute(q)
    con.commit()
    con.close()

def add_book(t):
    con = create_con()
    cur = con.cursor()

    q = "INSERT INTO Library (Book_name, Author_name, Publisher_name, Pages, Price) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(q,t)
    con.commit()
    con.close()