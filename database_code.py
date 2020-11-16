import sqlite3

def creatDataBase():
    con=sqlite3.connect('pos_database.db')
    curObj=con.cursor()
    curObj.execute("CREATE TABLE IF NOT EXISTS supplierData(supplierID INTEGER PRIMARY KEY AUTOINCREMENT,\
        name TEXT NOT NULL,address TEXT)")
    con.commit()
    curObj.execute("CREATE TABLE IF NOT EXISTS productData(ProductID INTEGER PRIMARY KEY,\
        name TEXT NOT NULL,brand TEXT NOT NULL,unit_value REAL NOT NULL,QTY INTEGER,\
            stock_value REAL,supplierID INTEGER NOT NULL,\
        FOREIGN KEY(supplierID) REFERENCES supplierData(supplierID))")
    con.commit()
    curObj.execute("CREATE TABLE IF NOT EXISTS staffData(staffID INTEGER PRIMARY KEY AUTOINCREMENT,\
        first_name TEXT NOT NULL,last_name TEXT NOT NULL,\
        email TEXT UNIQUE NOT NULL ,phone_number TEXT NOT NULL,address TEXT NOT NULL,\
        city TEXT NOT NULL,birth_date TEXT NOT NULL,gender TEXT,postal_code TEXT NOT NULL)")
    con.commit()
    curObj.execute("CREATE TABLE IF NOT EXISTS costumerData(costumerID INTEGER PRIMARY KEY AUTOINCREMENT,\
        first_name TEXT NOT NULL,last_name TEXT NOT NULL,\
        email TEXT,phone_number TEXT,city TEXT)")
    con.commit()
    curObj.execute("CREATE TABLE IF NOT EXISTS salesData(saleID INTEGER PRIMARY KEY AUTOINCREMENT,\
        productID INTEGER NOT NULL REFERENCES productData(productID),\
        quantity INTEGER NOT NULL, total INTIGER NOT NULL,\
        staffID INTEGER NOT NULL, costumerID INTEGER NOT NULL,date TEXT NOT NULL)")
    con.commit()
    con.close()

def addProduct(entities):
    con=sqlite3.connect('pos_database.db')
    curObj=con.cursor()
    curObj.execute("INSERT INTO productData VALUES(?,?,?,?,?,?,?)",entities)
    con.commit()
    con.close()
def addStaff(entities):
    con=sqlite3.connect('pos_database.db')
    curObj=con.cursor()
    curObj.execute("INSERT INTO staffData VALUES(?,?,?,?,?,?,?,?,?,?)",entities)
    con.commit()
    curObj.execute("SELECT * FROM staffData WHERE staffID = (SELECT MAX(staffID) FROM staffData)")
    id=curObj.fetchall()[0][0]
    con.close()
    return id
def addCostumer(entities):
    con=sqlite3.connect('pos_database.db')
    curObj=con.cursor()
    curObj.execute("INSERT INTO costumerData VALUES(?,?,?,?,?,?)",entities)
    con.commit()
    curObj.execute("SELECT * FROM costumerData WHERE costumerID = (SELECT MAX(costumerID) FROM costumerData)")
    id=curObj.fetchall()[0][0]
    con.close()
    return id
def addSupplier(entities):
    con=sqlite3.connect('pos_database.db')
    curObj=con.cursor()
    curObj.execute("INSERT INTO supplierData VALUES(?,?,?)",entities)
    con.commit()
    curObj.execute("SELECT * FROM supplierData WHERE supplierID = (SELECT MAX(supplierID) FROM supplierData)")
    id=curObj.fetchall()[0][0]
    con.close()
    return id
def addSales(entities):
    con=sqlite3.connect('pos_database.db')
    curObj=con.cursor()
    curObj.execute("INSERT INTO salesData VALUES(?,?,?,?,?,?,?)",entities)
    con.commit()
    curObj.execute("SELECT * FROM salesData WHERE saleID = (SELECT MAX(saleID) FROM salesData)")
    id=curObj.fetchall()[0][0]
    con.close()
    return id

def removeProduct(ID):
    con=sqlite3.connect('pos_database.db')
    curObj=con.cursor()
    curObj.execute("DELETE FROM productData WHERE ProductID=?",(ID,))
    con.commit()
    con.close()
def removeSupplier(ID):
    con=sqlite3.connect('pos_database.db')
    curObj=con.cursor()
    curObj.execute("DELETE FROM supplierData WHERE supplierID=?",(ID,))
    con.commit()
    con.close()
def removeStaff(ID):
    con=sqlite3.connect('pos_database.db')
    curObj=con.cursor()
    curObj.execute("DELETE FROM staffData WHERE staffID=?",(ID,))
    con.commit()
    con.close()
def removeCostumer(email):
    con=sqlite3.connect('pos_database.db')
    curObj=con.cursor()
    curObj.execute("DELETE FROM costumerData WHERE email=?",(email,))
    con.commit()
    con.close()

def updateProductQ(entities):
    con=sqlite3.connect('pos_database.db')
    curObj=con.cursor()
    curObj.execute("UPDATE productData SET QTY=QTY-?, stock_value=stock_value-? WHERE ProductID=?",entities)
    con.commit()
    con.close()

def updateProduct(entities):
    con=sqlite3.connect('pos_database.db')
    curObj=con.cursor()
    curObj.execute(
        """UPDATE productData SET name=?,
        brand=?,unit_value=?,QTY=?,stock_value=?,supllierID=?
        WHERE productID=?""",entities)
    con.commit()
    con.close()
    
def updateCostumer():
    pass

def updateSupplier(entities):
    con=sqlite3.connect('pos_database.db')
    curObj=con.cursor()
    curObj.execute(
        """UPDATE supplierData SET name=?,address=? WHERE supplierID=?""",entities)
    con.commit()
    con.close()

creatDataBase()
