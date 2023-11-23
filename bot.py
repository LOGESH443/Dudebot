#DUDE BOT 

import pyqrcode 
import png 
from pyqrcode import QRCode 
    
    
def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I was created in {0}.".format(birth_year))


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))


def guess_age(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)

    print("Your age is {0}; that's a good time to start programming!".format(age))


def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())

    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1
def calculate(a,b):
    result =0 
    print("Press 1 for Addittion \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")
    option = int(input("Enter your option: "))
    if option == 1:
        result = a+b
        print("Addition : ", result)
    elif option == 2:
        result = a-b
        print("Subtraction : ",result)
    elif option == 3:
        result = a*b
        print("Multiplication : ", result)
    elif option == 4:
        result = a/b
        print("Division : ",result)
    else:
        print("Invalid Value")

"""def Qrcode():
    s = input("enter your website:")
    url = pyqrcode.create(s) 
    url.svg("myqr.svg", scale = 10) 
    url.png('myqr.png', scale = 8)"""

def end():
    print('Congratulations, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')
    input()
    
greet('Dude', '2023') 
remind_name()

print("you want the help to find a age Press 1")
choice1 = int(input())
if(choice1 == 1):
    y = int(input("enter the year:"))
    m = int(input("enter the month:"))
    d = int(input("enter the day:"))
    guess_age(y,m,d)


print("you want the help to count a numbers Press 1")
choice2 = int(input())
if(choice2 == 1):
    count()


print("you want the help to solve Mathematical equation Press 1")
choice3 = int(input())
if(choice3 == 1):
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))
    calculate(a,b)

""" print("you are interested to generate Qr code for your website Press 1")
choice4 = int(input())
if(choice4 == 1):
    Qrcode() """

end()
