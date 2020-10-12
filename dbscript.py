import psycopg2

def create_table():
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, qty INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert(item,qty,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,qty,price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?" , (item,))
    conn.commit()
    conn.close()

def update(item,qty,price):
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET qty=?, price=? WHERE item=?",(qty,price,item))
    conn.commit()
    conn.close()

create_table()
#update("mouse",9,800)
#delete("mouse")
#insert("mouse",2,1000)
print(view())
