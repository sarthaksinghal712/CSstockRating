# GET CONTENT FROM USER DATA TABLE
import mysql.connector
mydb = mysql.connector.connect(host='localhost', database='MyProject', user='root', password='sarthak')
cursor = mydb.cursor()


def connectuser():
    isuser = input("Are you a registered user? (y/n): ")
    isuser.lower()
    if isuser == "y":
        return getuser()
    else:
        print("You have to register to continue")
        return registerlogin()


def getuser():
    x = ""
    while x != "True":
        username = str(input("Enter Username: "))
        password = str(input("Enter Password: "))
        x = "select * from users where username = '" + username + "' and password = '" + password + "';"
        cursor.execute(x)
        data = cursor.fetchone()
        if data is None:
            x = "False"
            mydb.commit()
            print("Login Failed")
            print("")
            print("")
        else:
            x = "True"
            mydb.commit()
            y = "select name from users where username = '" + username + "';"
            cursor.execute(y)
            naam = cursor.fetchone()
            print("Welcome,", naam[0])
            c = "select interest from users where username = '" + username + "';"
            cursor.execute(c)
            data = cursor.fetchone()
            d = "select age from users where username = '" + username + "';"
            cursor.execute(d)
            agee = cursor.fetchone()
            x, y, p = naam[0], data[0], agee[0]
            ret = [x, y, p]
            return ret


def registerlogin():
    addName = str(input("Enter Name: "))
    addUName = str(input("Choose Username: "))
    addPass = str(input("Enter Password: "))
    confirmPass = str(input("Confirm Your Passwords: "))
    if addPass == confirmPass:
        portf = input("What kind of Portfolio you desire? (low/mod/high): ")
        age = int(input("Enter your age: "))
        x = "INSERT INTO `myproject`.`users` (`username`, `password`, `name`, `interest`, `age`) VALUES ('" + addUName + "', '" + confirmPass + "', '" + addName + "', '" + portf + "', '" + str(age) + "');"
        cursor.execute(x)
        mydb.commit()
        y = "select name from users where username = '" + addUName + "';"
        cursor.execute(y)
        naam = cursor.fetchone()
        print("Welcome,", naam[0])
        c = "select interest from users where username = '" + addUName + "';"
        cursor.execute(c)
        data = cursor.fetchone()
        d = "select age from users where username = '" + addUName + "';"
        cursor.execute(d)
        agee = cursor.fetchone()
        x, y, p = naam[0], data[0], agee[0]
        ret = [x, y, p]
        return ret


    else:
        print("Err... Password Error, retry")
        print("")
        registerlogin()