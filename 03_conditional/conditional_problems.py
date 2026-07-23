#  easy problems on if else conditions

# Check if a number is positive.

# Check if a number is negative.

# Check if a number is zero.

# Check if a person is eligible to vote (18 or above).

# Check whether a number is even or odd.

# Check if a number is divisible by 5.

# Compare two numbers and print the greater one.

# Check whether a character is a vowel or consonant.

# Check whether a person is eligible for a driving license (age ≥ 18).

# Ask the user for a password. If it is "python123", print "Access Granted"; otherwise print "Access Denied".

# solutions\
 
# problem 1

number1 = 24
if number1 > 0 :
    print(f"{number1} is positive")

# problem 2

number2 = -34
if number2 < 0:
    print("number2 is negative")

# problem 3

number3 = 0 
if number3 == 0:
    print("number3 is zero ")

# problem 4

age = 19
if age >= 18 :
    print("eligible to vote")
else:
    print("not eligile to vote")

# problem 5

number4 = 24
if number4 % 2 == 0:
    print("number4 is even ")
else :
    print("number4 is odd")

# problem 6

number5 = 25
if number5 % 5 == 0:
    print("divisible by 5")

# problem 7

number6 = 23
number7 = 43
if number6 > number7 :
    print("number6 is greater")
elif number7 > number6:
    print("number7 is greater")
else:
    print("both are equal ")

# problem 8

character1  = "a"
if character1.lower() in "aeiou" :
    print("character1 is vowel ")
else:
    print("character1 is consonent")

# problem 9 

age1 = 22
has_licence = True
if age1 >= 18:
    if has_licence:
        print("eligible to drive")
    else:
        print("not eligible to drive")
else:
    print("too young to drive")

# problem 10

password = input("enter your password")
if password == "python123":
    print("access granted")
else:
    print("access denied")

# medium difficult 


# Find the largest of three numbers.

# Check whether a year is a leap year (use the basic rule: divisible by 4).

# Print the absolute value of a number (without using abs()).

# Check whether a number is between 1 and 100 (inclusive).

# Ask the user for marks and assign grades:
# 90–100 → A
# 75–89 → B
# 50–74 → C
# Below 50 → Fail

# Check if a username is "admin" and the password is "python123".

# Ask the user for a day number (1–7) and print the corresponding weekday.

# Build a simple calculator using if, elif, and else for +, -, *, and /.

# Check whether a person can donate blood (age ≥ 18 and weight ≥ 50 kg).

# Ask the user for a temperature in Celsius and classify it:
# Below 0 → Freezing
# 0–15 → Cold
# 16–30 → Pleasant
# Above 30 → Hot


# solutions

# problem 1

first_number = int(input('enter your number:'))
second_number= int(input("enter your number:"))
third_number = int(input("enter your number:"))

if first_number > second_number and first_number > third_number :
    print("first number is greater")
elif second_number > first_number and second_number > third_number :
    print("seconnd number is greater ")
else:
    print("third number is greater")

# problem 2

year = 2024

if year % 4 == 0 :
    print("leap year")

else :
    print("not a leap year")

# problem 3

num1 = -23

if num1 < 0:
    absolute_value = -num1
    print(absolute_value)
else :
    absolute_value = num1
    print(absolute_value)

# problem 4 

num2 = 34
if 1 < num2 < 100 :
    print("in between 1 and 100")
else :
    print("out of box delivery ")

# problem 5 

marks = int(input("enter your marks :"))
if 90 <= marks <= 100 :
    print("grade A")
elif 75 <= marks <=89 :
    print("grade B")

elif 50 <= marks <= 74:
    print("grade C ")
else :
    print("you failed the exam ")

# problem 6 

username = "admin"
password1 = "python123"

username1 = input('enter your username ;')
password2 = input('enter your password:')

if username1 == username and password2 == password1:
    print("both are correct ")
else :
    print("one is incorrect ")

# problem 7

daynumber = int(input("enter your day number:"))

if daynumber == 1:
    print("sunday")
elif daynumber == 2:
    print("monday")
elif daynumber == 3:
    print("tuesday")
elif daynumber == 4:
    print("wenesday")
elif daynumber == 5:
    print("thursday")
elif daynumber == 6:
    print("friday")
elif daynumber == 7:
    print("saturday")
else : 
    print("invalid daynumber ")


# problem 8 

first_digit = int(input("enter your first number:"))
second_digit = int(input("enter your second number :"))
operator = input("enter your operator:")

if operator == '+':
    print(first_digit + second_digit)
elif operator == '-':
    print(first_digit - second_digit)
elif operator == '*':
    print(first_digit * second_digit)
elif  operator == '/':
    print(first_digit/ second_digit)
else :
    print("wrong operator")


# problem 10

temperatur = int(input("enter your temperautr:"))
if temperatur <= 0:
    print("Freezing")
elif  0<temperatur <= 15 :
    print("Cold")
elif 16<=  temperatur <=30: 
    print("Pleasant")
elif temperatur > 30 :
    print("Hot")
else :
    print("very hot")

# difficutl problems 

# Build an ATM PIN checker (3 attempts).

# Calculate an electricity bill using slabs:
# First 100 units → ₹5/unit
# Next 100 units → ₹7/unit
# Above 200 units → ₹10/unit

# Check whether a triangle is Equilateral, Isosceles, or Scalene based on three sides.

# Build a BMI calculator and classify:
# Underweight
# Normal
# Overweight
# Obese

# Ask the user for a shopping amount:
# ₹5000 or more → 20% discount
# ₹2000–4999 → 10% discount
# Below ₹2000 → No discount

# Create a menu-driven restaurant ordering system (3 food items).

# Build a movie ticket price calculator:
# Child (<12)
# Adult (12–59)
# Senior (60+)

# Ask the user for three subject marks. If any mark is below 35, print "Fail"; otherwise print the average.

# Build a login system that blocks access after three incorrect password attempts.

# Create a menu-driven calculator with options:
# Addition
# Subtraction
# Multiplication
# Division
# Exit

# solutions 


# problem 1 

correct_pin = "python123"

pin1 = input("enter your pin:")

if pin1 == correct_pin : 
    print("loginned sucessfully")
else :
    print("try again seconsd time ")

pin2 = input("enter your pin2 :")

if pin2 == correct_pin:
    print("logged in sucessfully ")
else :
    print("try again last time ")

pin3  = input("enter your pin3 :")
if pin3 == correct_pin:
    print("logged in sucessfully ")
else :
    print("try again after soem time ")


# problem 2 

enter_units = int(input("enter your cureent units:"))

if enter_units <= 100 :
    print(enter_units * 5)

elif 100 < enter_units <= 200:
    print(enter_units*7)
elif enter_units > 200:
    print(enter_units*10)
else :
    print("enter total unist again ")


# problem 3 

side1 = int(input("enter your first side:"))
side2 = int(input("enter your second side :"))
side3 = int(input("enter your third side:"))

if side1 == side2 and side2 == side3 :
    print("equilatoral triangle")
elif side1 == side2 and side2!= side3:
    print("isolaseous tiangle ")
else:
    print("scalane triangle ")

# problem 4
print("BMI calculator :")

weight = int(input("enter your wieght:"))
height = input("enter your height:")

bmi = (weight) / (height *height )
if weight == 100:
    if height == 6:
        print("normal")
    elif height == 5.5:
        print("overweight")
    elif height == 7:
        print("underweight")
    else:
        print("height is less and weight is high")
else :
    print("obese")


# problem 5

shopping_amount = int(input("enter your shopping amount:"))

if shopping_amount >=  5000:
    print(shopping_amount / 1.2)
elif 2000 < shopping_amount <=4999:
    print(shopping_amount / 1.1)
elif 2000> shopping_amount:
    print(shopping_amount)
else:
    print("too much expensive")

# problem 6 

print("menu:")

orderd = "panner tikka"

item1 = input("enter your dish name:")

if item1 == orderd:
    print("order confiremed")
else :
    print("order again")

item2 = input("enter your dish name again:")

if item2 == orderd:
    print("order confirmed")
else :
    print("order again")

item3 = input("enter your third order:")

if item3 == orderd:
    print("order confirmed")
else:
    print("not ordered")


# problem 7

price = int(input("enter your price:"))
age = int(input("enter your age:"))

if age < 12:
    print("childrens ticket " , price + 12)
elif 12< age < 60:
    print("adults ticket", price + 59)
else:
    print("sneior citizen ", price -60)


# problem 8 

subject1= int(input("enter your first subjects marks :"))
subject2 = int(input("enter your second subjects marks:"))
subject3= int(input("enter your third subject marks :"))

average = (subject1+subject2+subject3) / 3

if subject1< 35 or subject2<35 or subject3 < 35:
    print("failed")
else :
    print(average)

# problem 9 

correct_password = "python12345"

try1 = input("enter your password ")

if try1 == correct_password :
    print("access granted ")
else:
    print("acess denied try again ")

try2 = input('enter your pin again:')

if try2 == correct_password:
    print("acess granted")
else:
    print("try again last time")

try3 = input("enter your password:")

if try3 == correct_password:
    print("acess granted")
else :
    print("access blocked")

# problem 10 

first_value = int(input("enter your first digit :"))

second_value = int(input("enter your second digit:"))

addition = '+' 
substraction ='-'
multiplication =  '*'
division =  '/'

choice = input("enter your choice:")

if choice == addition:
    print(first_value + second_value)
elif  choice == substraction:
    print(first_value - second_value)
elif choice == multiplication:
    print(first_value*second_value)
elif choice == division:
    print(first_value/ second_value)

else :
    print("exit")




