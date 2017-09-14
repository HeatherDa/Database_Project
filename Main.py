#class Database(object):
import sqlite3
from sqlite3 import Error
db=False

#    def __init__(self, database='database.db'): #if passed database fileName and tableName[],columns[], and types[] could reuse class in
#        # other program, but would also need to tweak test scenarios bellow, as wouldn't have 'itemQuantity' etc.


filename= 'p2_db.sqlite'  # name of the sqlite database file
tableName = 'products'  # name of the table to be created
columns = ['itemNum','itemType', 'itemDescription', 'itemVendor', 'itemExp', 'itemValue', 'itemQuantity']
types = ['INTEGER','TEXT', 'TEXT', 'INTEGER', 'TEXT', 'TEXT', 'INTEGER']
#        # Connecting to the database file
def useDatabase(option):
    try:
        connect = sqlite3.connect(filename)
        c=connect.cursor()

        if option==1:
            makeTable(c)
        elif option==2:
            newRow(c)
        elif option==3:
            updateRow(c)
        elif option==4:
            deleteRow(c)
        elif option==5:
            displayAll(c)
        elif option==6:
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
checkString = "LIKE '[0-9][0-9][0-9][0-9][0-9]'"




#Lets make a table in the database
def makeTable(c):

    for i in columns:
        if (i != 'itemVendor') and (i != 'itemQuantity') and (i != 'itemNum'):
            c.execute("ALTER TABLE {tn} ADD COLUMN'{nf}''{ft}'".\
                format(tn=tableName,nf=i, ft=types.index(i)))

        elif i == 'itemQuantity': #uses default value of 0 for Quantitiy
            c.execute("ALTER TABLE {tn} ADD COLUMN'{nf}'{ft} DEFAULT '{d}'".\
                format(tn=tableName,nf=i, ft=types.index(i), d=0))

        elif i=='itemVendor':   #uses CHECK to ensure that vendor numbers are 5 digit numbers
         # Will eventually point to a Vendor's table, but can't set that up without having a Vendor's table
            c.execute("ALTER TABLE {tn} ADD COLUMN'{nf}'{ft} CHECK (itemVendor {c})".\
                format(tn=tableName, nf=i, ft=types.index(i), d=0, c=checkString))

        else: #it's the primary key, used CHECK to ensure that itemNums are 5 digit numbers
            c.execute("ALTER TABLE {tn} ADD COLUMN'{nf}' {ft} PRIMARY KEY, CHECK (itemNum {c})". \
                format(tn=tableName, nf=columns[0], ft=types[0], c=checkString))

def newRow(c):
#Something to add a row.
    print("Not done writing addRow yet, here's the data so far ")
#self.connect.commit()

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







import sqlite3
#import Database

#daba=Database.Database() # defined or initialized?  Want defined, not initialized....

def dbExists(option):
    global db
    if not db: # don't know if this will work to tell me if it exists, ie has been initialized.'
        print('no daba, so make one')
        if option !=1:
            useDatabase(option)
        return False
    else:
        return True

def isInt (data):
    try:
        i=int(data)
        return True
    except TypeError:
        print ("The data you have entered is not an integer.")
        return False

#def isText(data):
#    try:
#        s=str(data)
#        return True
#    except TypeError:
#        print ("This field needs a string.") #when would you ever use this?  Data always comes in as a string...
stTest="I'm a test"

def main():
    global daba
    global db
    global stTest
#    import Database
    print("This program helps you to create and use a products database.  \nPlease choose one of the following menu options.")
    option=int(input("1: Create a Database and Table\n2: Add a row to the table\n3: Update a row in the table\n4: Delete a row in the table\n5: Display all rows in the table\n6: Search for a specific row and display it."))
    if(isInt(option)): #test for numbers
        if option==1:
            dbExists(option)
        elif option==2:
            if dbExists(option):
                newRow(daba, stTest)
            else:
                print("Please create the Database before attempting to use it.")
        elif option==3:
            if dbExists(option):
                updateRow(daba,stTest)
            else:
                print("Please create the Database before attempting to use it.")
        elif option==4:
            if dbExists(option):
                deleteRow(daba, option)
            else:
                print("Please create the Database before attempting to use it.")
        elif option==5:
            if dbExists(option):
                displayAll(daba)
            else:
                print("Please create the Database before attempting to use it.")
        elif option==6:
            if dbExists(option):
                searchPar=input("Please type the item number of the record you are looking for.")
                if (isInt(searchPar) and (len(searchPar)==5)): #right now, search only looks for item numbers.  Improve later.
                    search(daba, searchPar, option)
                else:
                    print("That is not a valid item number.  An item number has 5 numeric digits.")
            else:
                print("Please create the Database before attempting to use it.")
        else:
            print("That is not one of the options on the menu.  To select an item from the menu, type its number.")











main()
#close connection.



