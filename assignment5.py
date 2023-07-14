# Challenge:1 Square numbers and therir sum

class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def sqsum(self, x, y, z):
        result = sum([x**2, y**2, z**2])
        return result

num = point(2,3,4)
print("Sum of squares:",num.sqsum(2, 3, 4))

#Challenge:2 Implement a calculator class

class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a*b
    def divison(self, a,b):
        return a/b
    
obj = calculator(25,5)
print("Addition:",obj.add(25,5))
print("Substraction:",obj.subtract(25,5))
print("Multiplication:",obj.multiply(25,5))
print("Division:",obj.divison(25,5))

# Challenge:3 Complete student class

class Student:
    def __init__(self):
        self.__student = "Ajay"
        self.__rollno = 25678
    def setstudent(self, name):
        self.__student = name
    def setrollno(self, roll):
        self.__rollno = roll
    def getstudent(self):
        return self.__student
    def getrollno(self):
        return self.__rollno

stu1 = Student()
print(stu1.getstudent())
print(stu1.getrollno())
stu1.setstudent("Laxmi")
stu1.setrollno(1547)
print(stu1.getstudent())
print(stu1.getrollno())

#Challenge:4 Implement a Bank account:
class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
class Savings(Account):
    def __init__(self, title, balance, interest):
        super().__init__(title, balance)
        self.interest = interest
    def show(self):
        print("Account was created..")

obj = Savings("Anish", 2000, 5)
print(obj.show())

#Challenge:5 Handling Bank Account:
class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
    def withdraw(self, amt):
        self.cash = self.balance - amt
    def deposit(self, amount):
        self.cash = self.balance + amount
    def getbalance(self):
        return self.cash
class Savings(Account):
    def __init__(self, title, balance, interest):
        super().__init__(title, balance)
        self.interest = interest
    def interestamount(self):
        return (self.balance * self.interest)/100

acct1 = Account("Anish", 2000)
acct1.withdraw(500)
print("Remaining Balance:",acct1.getbalance())
acct1.deposit(1000)
print("Total Balance:",acct1.getbalance())
acct1 = Savings("Anish", 2000, 5)
print("Interest Amount:",acct1.interestamount())
