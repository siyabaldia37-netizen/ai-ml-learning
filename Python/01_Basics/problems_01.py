# # Create two integers and print their sum.

# # Print the difference of two numbers.

# # Multiply two numbers.

# # Divide two numbers using /.

# # Find the remainder using %.

# # Find the floor division using //.

# # Calculate 7 ** 3.

# # Check whether 15 > 10.

# # Check whether 25 == 30.

# # Check whether "Python" contains "thon" using in.

# # solutions

a = 10
b = 12
print(a+b)

c = 54
d = 45
print(c-d)

e = 10
f= 56
print(e*f)

g = 10
h  =2
print(g/h)

i = 32
j = 6
print(i%j)

k  = 45
l = 3
print(k//l)

print(7**3)

m = 15
n = 10
if m > n :
    print(" 15 is greater")
else:
    print("10 is greater")

print(m>n)
print(15>10)

print(25 == 30)

str = "python"

print("thon" in str)

# # medium level problems 

# # input two numbers and print all arithmetic operations.

# # Check whether a number is even using %.

# # Check whether a number is divisible by both 3 and 5.

# # Ask the user for two numbers and compare them using all comparison operators.

# # Use += to add 25 to a variable.

# # Use *= to double a number.

# # Check whether "AI" is not present in "Python Programming".

# # Create two lists with the same values and compare them using both == and is.

# # Ask the user for their age and check whether they are between 18 and 60 using and.


# # solutions

a1 = int(input("enter your first number:"))
a2 = int(input("enter your second number:"))

print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1%a2)
print(a1/a2)
print(a1//a2)
print(a1**a2)

a3 = 2
print("even" if  a3 % 2 == 0 else "odd" )

a4 = 15
print( "divisible by both " if a4 % 3  == 0 and a4 % 5 == 0 else  "not by both ")

a5 = int(input("enter your first digit :"))
a6 = int(input("enter your second digit :"))

print(a5 != a6)
print(a5 == a6)
print(a5 > a6)
print( a5 < a6)
print(a5 >= a6)
print(a5 <= a6)

a7  = 2
a7 += 25
print(a7)

a8 = 2
a8*= 2
print(a8)

str2 = "Python Programming"
print(str2 in"AI")

list = [1,2,3,4]
list1 = [1,2,3,4]
print(list == list1)
print(list is list1)

age = int(input("enter your age:"))
print("eligible" if age >= 18 and age <= 60 else "not eligible")

password = input("enter your password:")
print("greater" if len(password) >= 8 else "lesser")

# # difficult problems

# # Build a simple calculator that takes two numbers and an operator (+, -, *, /) and performs the operation.

# # Ask the user for three numbers and print the largest using comparison operators (don't use max()).

# # Check whether a year entered by the user is divisible by 4.

# # Ask the user for a number and determine whether it is positive, negative, or zero using comparison operators.

# # Check whether a user-entered character is a vowel using the in operator.

# # Ask the user for a sentence and check whether it contains the word "Python" using a membership operator.

# # Create two variables referring to the same list and demonstrate the difference between == and is.

# # Ask the user to enter two strings and check whether they are exactly equal and whether they are the same object.

# # Build a mini login check where the username must equal "admin" and the password must equal "python123" to print "Login Successful".

# # Ask the user to enter a number and determine whether it is divisible by both 2 and 7 using logical and arithmetic operators.


# # solutions 


print("calculator:")
num1 = int(input("enter your first number:"))
num2 = int(input("enter your second number:"))

operator = input("enteryour operator:")

print(num1+num2 if operator == '+'else "wrong operator")
print(num1-num2 if operator == '-' else "worng operator")
print(num1*num2 if operator == '*' else "worng operator")
print(num1/num2 if operator == '/' else "worng operator")

num4 = int(input("enter your first number:"))
num3 = int(input("enter your seconf number:"))
num5= int(input("enter your third number:"))

print("num4 is greater" if num4 > num5 and num4> num3 else "lesses")
print("num3 is greter" if num3>num4 and num3>num5 else "lesser")
print("num5 is greater" if num5>num4 and num5>num4 else "lesser")

year = 2024
print('divisible' if year % 4 == 0 else "not divisible")

number = int(input("enter your number:"))
print("positive"  if number > 0  else "negative")
print("zero " if number == 0 else "wrong input")

character = input("enter your character:")
print( character.lower() in "aeiou")

sentance = input("enter your sentance:")
print("python" in sentance.lower())

list2 = [1,2,3,4]
list3 = list2

print(list2 == list3)
print(list2 is list3)

string1 = input("enter tour string:")
string2= input("enter your string:")
print(string1 == string2)
print(string1 is string2)
print(len(string1) == len(string2))

username = input("enter your username:")
password1 = input("enter your password:")

print("login sucessgull" if username == "admin" and password1  == "python123" else 'worng nformation')

num7 = int(input("enter your number:"))

print("divisible by both " if num7 %2 == 0 and num7 % 7 == 0 else "not by both ")




