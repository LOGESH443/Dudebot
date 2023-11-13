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

def end():
    print('Congratulations, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')
    input()
    
greet('Dude', '2023') 
remind_name()
y = int(input("enter the year:"))
m = int(input("enter the month:"))
d = int(input("enter the day:"))
guess_age(y,m,d)
count()
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
calculate(a,b)
end()
