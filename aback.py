import sqlite3

def create_table():
    con=sqlite3.connect("banksdata.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS banks(account_no INTEGER PRIMARY KEY,Name TEXT,City TEXT ,Balance FLOAT)")
    con.commit()
    con.close()

def insert_value(a,n,b,c):
    con=sqlite3.connect("banksdata.db")
    cur=con.cursor()
    cur.execute("INSERT INTO banks VALUES(?,?,?,?)",(a,n,b,c))
    con.commit()
    con.close()

def view():
        con=sqlite3.connect("banksdata.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM banks")
        r = cur.fetchall()
        con.close()
        return r

def checkaccount(a):#returns int ie a when account does not exist in db
    con=sqlite3.connect("banksdata.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM banks WHERE account_no=?",(a,))
    r = cur.fetchall()
    con.close()
    #print(r)
    if (len(r)==0):
        return a #do not exist
    else:
        return "account no already exist"

def search_account(a):
    con=sqlite3.connect("banksdata.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM banks WHERE account_no=?",(a,))
    r = cur.fetchall()
    con.close()
    if len(r)>0:
        return r
    else:
        return "NO such account no " +a+" exists in database"
def deposit_money(a,m):
    con=sqlite3.connect("banksdata.db")
    cur=con.cursor()
    cur.execute("SELECT Balance FROM banks WHERE account_no=?",(a,))
    r = cur.fetchall()
    bal=r[0][0]
    #print(type(m))
    netbal=bal+float(m)
    cur.execute("UPDATE banks SET Balance = ? WHERE account_no =?",(netbal,a))
    con.commit()
    return netbal
    con.close()

def with_money(a,m):
    con=sqlite3.connect("banksdata.db")
    cur=con.cursor()
    cur.execute("SELECT Balance FROM banks WHERE account_no=?",(a,))
    r = cur.fetchall()
    bal=r[0][0]
    netbal=bal-float(m)
    if (netbal>0):
        cur.execute("UPDATE banks SET Balance = ? WHERE account_no =?",(netbal,a))
        con.commit()
        return netbal
    else:
        return "sorry not enough BALANCE"
    con.close()


def transfer_amount(a,m,d):
    con=sqlite3.connect("banksdata.db")
    cur=con.cursor()
    account_frontend.withdrawal()


def delete_account(a):
    con=sqlite3.connect("banksdata.db")
    cur=con.cursor()
    cur.execute("DELETE FROM banks WHERE account_no=?",(a,))
    con.commit()
    con.close()





#create_table()
#xyz=checkaccount(15606100)
#print(xyz)
#insert_value(155555,"testerrr","noviiii",6667)
#add_entry("the sun","jason roy",1990,1506097)
#add_entry("mars planet","chris woakes",1999,1506101)
#print(search_table(y="1999"))
#delete_entry(4)
#update_entry(8,t="mars planet",a="ben stokes",y="2007",i="1506117")
#insert_value(1506108,"apurv kr","rnc",11770)
#print(view())
#print(deposit_money(1506111,50))
