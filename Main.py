#class Database(object):
import sqlite3
from sqlite3 import Error
db=False

#    def __init__(self, database='database.db'): #if passed database fileName and tableName[],columns[], and types[] could reuse class in
#        # other program, but would also need to tweak test scenarios bellow, as wouldn't have 'itemQuantity' etc.


filename= 'p2_db.sqlite'  # name of the sqlite database file
tableName = 'products'  # name of the table to be created

#        # Connecting to the database file
def useDatabase(option):
    print("use database")
    global filename
    global tableName
    columns = ['itemNum', 'itemType', 'itemDescription', 'itemVendor', 'itemExp', 'itemValue', 'itemQuantity']
    types = [' INTEGER', ' TEXT', ' TEXT', ' INTEGER', ' REAL', ' REAL', ' INTEGER']
    like = "LIKE '[0-9][0-9][0-9][0-9][0-9]'"
    try:
        connect = sqlite3.connect(filename)
        #c=connect.cursor()
        if option==1:
            c = connect.cursor()
            c.execute("CREATE TABLE {tn} ( 'itemNum' INTEGER PRIMARY KEY, 'itemType' TEXT, 'itemDescription' TEXT, 'itemVendor' INTEGER , 'itemCost' REAL, 'itemValue' REAL, 'itemQuantity' INTEGER DEFAULT 0)".format(tn=tableName))#, col=columns[0], field=types[0]))

            c.execute("Insert INTO {tn} Values(NULL, 'sample', 'test record', 54321, 2.20, 5.01, 2)".format(tn=tableName))
            connect.commit()
            #c.execute("ALTER TABLE Products ADD COLUMN 'itemType' TEXT")
            #c.execute("ALTER TABLE Products ADD COLUMN 'itemDescription' TEXT")
            #c.execute("ALTER TABLE Products ADD COLUMN 'itemVendor' INTEGER")#can't get this to work CHECK (itemVendor {c}".format (c=like))
            #c.execute("ALTER TABLE Products ADD COLUMN 'itemCost' TEXT")
            #c.execute("ALTER TABLE Products ADD COLUMN 'itemValue' TEXT")
            #c.execute("ALTER TABLE Products ADD COLUMN 'itemQuantity' INTEGER DEFAULT 0")

        elif option==2:
            c = connect.cursor()
            se = input("Please type in the values for the new row separated by commas.")
            v = se.split(',')
            #v.insert(0,'NULL')
            var = []
            for value in v:
                a = value.strip()
                var.append(a)
            val = (var[0], var[1], var[2], var[3], var[4], var[5])
            #val = (var[0], var[1], var[2], var[3], var[4], var[5])
            #sql = '''INSERT INTO products(itemType,itemDescription,itemVendor,itemCost,itemValue,itemQuantity) VALUES(NULL,?,?,?,?,?,?)'''
            #sql = '''INSERT INTO products VALUES(?,?,?,?,?,?,?)'''
            print("INSERT INTO products (itemNum,'itemType', 'itemDescription', 'itemVendor', 'itemCost', 'itemValue', 'itemQuantity') VALUES('{ai}','{bi}',{ci},'{di}','{ei}',{fi})"
                      .format(ai=var[0],bi=var[1],ci=var[2],di=var[3],ei=var[4],fi=var[5]))
            c.execute("INSERT INTO products (itemNum,'itemType', 'itemDescription', 'itemVendor', 'itemCost', 'itemValue', 'itemQuantity') VALUES(NULL,'{ai}','{bi}',{ci},'{di}','{ei}',{fi})"
                      .format(ai=var[0],bi=var[1],ci=var[2],di=var[3],ei=var[4],fi=var[5]))
            connect.commit()
            #c.execute("INSERT INTO products VALUES(NULL,'pet','black cat',12345,'1.11','2.22',6)")

            #c.execute(sql, val)
            print("data entered was ", val)
        elif option==3:
            c = connect.cursor()
            upIn=input("Please type in the item number and the new quantity separated by a comma.")
            inf=upIn.split(',')
            #This will throw an error if the item id entered does not exist
            c.execute("UPDATE {tn} SET {col}='{inp}'WHERE {itemNum}={id}".format(tn=tableName,col='itemQuantity',inp=inf[0],id=inf[1]))
        elif option==4:
            c = connect.cursor()
            deleteRow(c,option)
        elif option==5:
            c = connect.cursor()
            c.execute("SELECT * FROM {tn}".format(tn=tableName))
            records=c.fetchall()
            for record in records:
                print(record)
        elif option==6:
            c = connect.cursor()
            s = input("What is the number of the item you are looking for?")
            if isInt(s) and len(s) == 5:
                search(c, s, option)
        else:
            print("That is not one of the options on the menu.")
        db=True


    except Error as e:
        print(e)
    finally:
        connect.close()



connect=sqlite3.connect(filename)
c = connect.cursor()





#Lets make a table in the database
"""def makeColumns(i, type):
    global tableName
    like = "LIKE '[0-9][0-9][0-9][0-9][0-9]'"
    print("makeTable")
    #for i in columns:
    if (i != 'itemVendor') and (i != 'itemQuantity') and (i != 'itemNum'):
        r=str("ALTER TABLE {tn} ADD COLUMN'{nf}''{ft}'".format(tn=tableName,nf=i, ft=type))
        print(r)
        return r

    elif i == 'itemQuantity': #uses default value of 0 for Quantitiy
        r=str("ALTER TABLE {tn} ADD COLUMN'{nf}'{ft} DEFAULT '{d}'".format(tn=tableName,nf=i, ft=type, d=0))
            #format(tn=tableName,nf=i, ft=types.index(i), d=0))
        print(r)
        return r

    elif i=='itemVendor':   #uses CHECK to ensure that vendor numbers are 5 digit numbers
      # Will eventually point to a Vendor's table, but can't set that up without having a Vendor's table
        r=str("ALTER TABLE {tn} ADD COLUMN'{nf}'{ft} CHECK (itemVendor {c})".format(tn=tableName,nf=i, ft=type, c=like))
            #format(tn=tableName, nf=i, ft=types.index(i), d=0, c=checkString))
        print (r)
        return r

#    else: #it's the primary key, used CHECK to ensure that itemNums are 5 digit numbers
#        r=("ALTER TABLE {tn} ADD COLUMN'itemNum' {ft} PRIMARY KEY CHECK (itemNum {c})".
#            format(tn=tableName, ft=types[0], c=checkString))
#        print(r)
#        return r
"""


def newRow(c):
#Something to add a row.
    se=input("Please type in the values for the new row separated by commas.")
    v=se.split(',')
    var=[]
    for value in v:
        a=value.strip()
        var.append(a)
    val=(var[0],var[1],var[2],var[3],var[4],var[5],var[6])

    print("Not done writing addRow yet, here's the data so far ")
    sql='''INSERT INTO products(itemNum,itemType,itemDescription,itemVendor,itemCost,itemValue,itemQuantity) VALUES(?,?,?,?,?,?,?)'''
    c.execute(sql,val)

def updateRow(c):
    print("still working on update, but I got. ")

def displayAll(c):
    print("still working on display")
    searchStr='SELECT * FROM {table}'.format (table=tableName)

def search(c, s, option):
    s=input("What is the number of the item you are looking for?")
    if isInt(s) and len(s)==5:
        print("still working on search, got string ")
#prevalidated search string
        searchStr='SELECT * FROM {table}WHERE{colName}={look}'.format (table= tableName, colName='itemNum', look=s) #why doesn't self.tableName work?
        c.execute(searchStr)
        itemExists=c.fetchone()
        if itemExists:
            print('{}'.format(itemExists))
        else:
            print('{} is not in the database.'.format(s))
    else:
        print("That is not the correct format for an item number.  Item numbers have five numeric digits.")
def deleteRow (c, option):
    print("delete isn't done")
    s=input("What is the item number of the item you wish to delete?")
    search(c, s,option)

def isInt (data):
    try:
        i=int(data)
        return True
    except ValueError:
        print ("The data you have entered is not an integer.")
        return False

def main():
    global daba
    global db
    global stTest
#    import Database
    print("This program helps you to create and use a products database.  \nPlease choose one of the following menu options.")
    option=input("1: Create a Database and Table\n2: Add a row to the table\n3: Update a row in the table\n4: Delete a row in the table\n5: Display all rows in the table\n6: Search for a specific row and display it.")
    if isInt(option):
        op=int(option)
        if (op >0) & (op <7): #test for numbers
            useDatabase(op)
    else:
        print("That is not one of the options on the menu.  To select an item from the menu, type its number.")

main()



