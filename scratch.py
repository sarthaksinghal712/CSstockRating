"""
    Made by @Sarthak Singhal
    Infinito Rating Algorithm
"""
import matplotlib.pyplot as plt
import mysql.connector
from infinito import calcu
from getuser import connectuser, registerlogin, getuser
print()
nameandint = connectuser()
print()
sec = ["Consumer Discretionary", "Staples", "IT", "Healthcare", "Energy", "Finance"]
plt.style.use('ggplot')

# def showGraphs(shg):
#     if shg == 1:
#         cursor.execute("select * from stocks order by rating asc")
#     elif shg == 2:
#         cursor.execure("select * from stocks where rating between 0 and 1")
#     records = cursor.fetchall()
#     names = []
#     ratings = []
#     for row in records:
#         names.append(row[1])
#         ratings.append(row[2])
#     plt.figure(figsize=(14, 6))
#     plt.ylabel("Infinito Rating\n", fontsize=12)
#     plt.suptitle('Stock v/s Rating')
#     plt.bar(names, ratings)
#     for a, b in zip(names, ratings):
#         plt.text(a, b, str(b))
#     plt.show()
#     names.clear()
#     ratings.clear()
#

def showInputs():
    betaval = float(input("Enter Beta Value: "))
    floatshortval = float(input("Enter % short floated: "))
    roeval = float(input("Enter ROE%: "))
    roaval = float(input("Enter ROA%: "))
    roceval = float(input("Enter ROCE%: "))
    growthrateval = float(input("Enter 3 years sales growth: "))
    return betaval, floatshortval, roeval, roaval, roceval, growthrateval

def cd(x):
    betaavg = 1.17
    floatshort = 2
    roeavg = 17.41
    roaavg = 8.06
    roceavg = 57
    growthrateavg = 23.29
    b = [betaavg, floatshort, roeavg, roaavg, roceavg, growthrateavg]
    return x, b


def st(x):
    betaavg = 0.48
    floatshort = 2
    roeavg = 17.93
    roaavg = 17.35
    roceavg = 24.1
    growthrateavg = 5.60
    b = [betaavg, floatshort, roeavg, roaavg, roceavg, growthrateavg]
    return x, b


def it(x):
    betaavg = 0.85
    floatshort = 2
    roaavg = 1.25
    roeavg = 9.08
    growthrateavg = 7.53
    roceavg = 200
    b = [betaavg, floatshort, roeavg, roaavg, roceavg, growthrateavg]
    return x, b


def hc(x):
    betaavg = 0.67
    floatshort = 2
    roaavg = 7.48
    roeavg = 19.95
    growthrateavg = 2.27
    roceavg = 3.08
    b = [betaavg, floatshort, roeavg, roaavg, roceavg, growthrateavg]
    return x, b


def en(x):
    betaavg = 1.17
    floatshort = 2
    roaavg = 4.88
    roeavg = 9.63
    growthrateavg = 16.53
    roceavg = 20.52
    b = [betaavg, floatshort, roeavg, roaavg, roceavg, growthrateavg]
    return x, b


def fi(x):
    betaavg = 0.98
    floatshort = 1.16
    roaavg = 1.4
    roeavg = 21.15
    growthrateavg = 13.32
    roceavg = 15.56
    b = [betaavg, floatshort, roeavg, roaavg, roceavg, growthrateavg]
    return x, b


mydb = mysql.connector.connect(host='localhost', database='MyProject', user='root', password='sarthak')
cursor = mydb.cursor()


def addrecd(h, k, l):
    j = str(k)
    strr = "INSERT INTO `myproject`.`stocks` (`stocks`, `rating`, `cat`) VALUES (" + "'" + h + "'" + "," + "'" + j + "'" + "," + "'" + l + "'" + ")"
    print(strr)
    cursor.execute(strr)
    mydb.commit()


while True:
    print("1. Add Stock \n2. View Stocks \n3. Show Graphs\n4. Show Profile and suggest stocks")
    inich = int(input("Enter Choice: "))
    print()
    if inich == 1:
        print("\n1. Consumer Discretionary \n2. Staples\n3. IT\n4. Health Care\n5. Energy\n6. Finance\n")
        stock_name = input("Enter Stock Name: ")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            a = list(showInputs())
            x, b = cd(a)
            res = calcu(x, b)
            if 0 < res < 1:
                z = "low"
            elif 1 < res < 2:
                z = "mod"
            elif 2 < res < 3:
                z = "high"
            if z != nameandint[1]:
                print("Your Profile says you are interested in " + nameandint[1] + " risk stock\n")
                print("However, the stock:", stock_name, "lies in", z, "risk category\n")
                print("")
            confirm = input("Are you sure you want to add the stock to the list? (y/n): ")
            if confirm == "y":
                addrecd(stock_name, res, z)
            else:
                pass
        elif choice == 2:
            a = list(showInputs())
            x, b = st(a)
            res = calcu(x, b)
            if 0 < res < 1:
                z = "low"
            elif 1 < res < 2:
                z = "mod"
            elif 2 < res < 3:
                z = "high"
            if z != nameandint[1]:
                print("Your Profile says you are interested in " + nameandint[1] + " risk stock\n")
                print("However, the stock:", stock_name, "lies in", z, "risk category\n")
                confirm = input("Are you sure you want to add the stock to the list? (y/n): ")
                print("")
            confirm = input("Are you sure you want to add the stock to the list? (y/n): ")
            if confirm == "y":
                addrecd(stock_name, res, z)
            else:
                pass
        elif choice == 3:
            a = list(showInputs())
            x, b = it(a)
            res = calcu(x, b)
            if 0 < res < 1:
                z = "low"
            elif 1 < res < 2:
                z = "mod"
            elif 2 < res < 3:
                z = "high"
            if z != nameandint[1]:
                print("Your Profile says you are interested in " + nameandint[1] + " risk stock\n")
                print("However, the stock:", stock_name, "lies in", z, "risk category\n")
                confirm = input("Are you sure you want to add the stock to the list? (y/n): ")
                print("")
            confirm = input("Are you sure you want to add the stock to the list? (y/n): ")
            if confirm == "y":
                addrecd(stock_name, res, z)
            else:
                pass
        elif choice == 4:
            a = list(showInputs())
            x, b = hc(a)
            res = calcu(x, b)
            if 0 < res < 1:
                z = "low"
            elif 1 < res < 2:
                z = "mod"
            elif 2 < res < 3:
                z = "high"
            if z != nameandint[1]:
                print("Your Profile says you are interested in " + nameandint[1] + " risk stock\n")
                print("However, the stock:", stock_name, "lies in", z, "risk category\n")
                confirm = input("Are you sure you want to add the stock to the list? (y/n): ")
                print("")
            confirm = input("Are you sure you want to add the stock to the list? (y/n): ")
            if confirm == "y":
                addrecd(stock_name, res, z)
            else:
                pass
        elif choice == 5:
            a = list(showInputs())
            x, b = en(a)
            res = calcu(x, b)
            if 0 < res < 1:
                z = "low"
            elif 1 < res < 2:
                z = "mod"
            elif 2 < res < 3:
                z = "high"
            if z != nameandint[1]:
                print("Your Profile says you are interested in " + nameandint[1] + " risk stock\n")
                print("However, the stock:", stock_name, "lies in", z, "risk category\n")
                confirm = input("Are you sure you want to add the stock to the list? (y/n): ")
                print("")
            confirm = input("Are you sure you want to add the stock to the list? (y/n): ")
            if confirm == "y":
                addrecd(stock_name, res, z)
            else:
                pass
        elif choice == 6:
            a = list(showInputs())
            x, b = fi(a)
            res = calcu(x, b)
            if 0 < res < 1:
                z = "low"
            elif 1 < res < 2:
                z = "mod"
            elif 2 < res < 3:
                z = "high"
            if z != nameandint[1]:
                print("Your Profile says you are interested in " + nameandint[1] + " risk stock\n")
                print("However, the stock:", stock_name, "lies in", z, "risk category\n")
                confirm = input("Are you sure you want to add the stock to the list? (y/n): ")
                print("")
            confirm = input("Are you sure you want to add the stock to the list? (y/n): ")
            if confirm == "y":
                addrecd(stock_name, res, z)
            else:
                pass
    elif inich == 2:
        print("")
        cursor.execute("select * from stocks order by rating asc")
        records = cursor.fetchall()
        for row in records:
            print("Name = ", row[0])
            print("Rating = ", row[1], "\n")
        r = int(input("Enter Your Choice: "))
        # chooserecd(r)
    elif inich == 3:
        # shg = int(input("Which Category Do You Want To View?:-\n1. General\n2. Low Risk\n3. Moderate Risk\n4. High Risk"))
        # showGraphs(shg)
        cursor.execute("select * from stocks order by rating asc")
        records = cursor.fetchall()
        names = []
        ratings = []
        for row in records:
            names.append(row[0])
            ratings.append(row[1])
        plt.figure(figsize=(14, 6))
        plt.ylabel("Infinito Rating\n", fontsize=12)
        plt.suptitle('Stock v/s Rating')
        plt.bar(names, ratings)
        for a, b in zip(names, ratings):
            plt.text(a, b, str(b))
        plt.show()
        names.clear()
        ratings.clear()
    elif inich == 4:
        print("Hi, " + nameandint[0] + "\nAge: " + str(nameandint[2]) + "\nInterest: " + nameandint[1] + " risk stock\n")
        print("Stocks we would like to suggest on\nthe basis of your profile:-\n")
        x = "SELECT * FROM myproject.stocks where cat = '" + nameandint[1] + "';"
        cursor.execute(x)
        alll = cursor.fetchall()
        for i in alll:
            print("Stock Name:", i[0])
        print()
    elif inich == 0:
        break
    else:
        continue

