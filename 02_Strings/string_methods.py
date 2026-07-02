"""a = input()
print(a)

b = str(input("enter your name: "))
print(b)

c = int(input("enter a number: "))

d= int(input("enter a number: "))
print(c+d)"""


"""a = int (input("enter a number:"))
b = int (input("enter a number:"))

print(a+b)"""


# accessing string using index 
"""
a = "siya"
print(a[1])

b = "hello world"
print(b[0:7])
"""


# loop thrugh the string using for loop
"""
name = "siya"
print("lets make a for loop")

for character in name:
    print(character)"""


# string slicing and operations

'''name = " python programming "

print(name[0:5])
print(name[3:5])
print(name[0:6:2])
print(name[5:])

print(len(name))

print(name.strip())
print(name.replace("python", "c"))

print(name.upper())
print(name.capitalize())

print(name.split())
print(name.split("o"))
print(name[-1:-3:-1])
print(name[:])
print(name[::-1])
print(name[-1:-8:-1])
'''


# string operations 

# strings are immutable in python 

name  = "siya jangir !"

print(len(name))

print(name.upper())

print(name.lower())

print(name.replace("s", "M"))

print(name.strip())

print(name.rstrip("!"))

print(name.lstrip())

print(name.split("y"))

print(name.title())

print(name.find("j"))

print(name.find("x"))

print(name.count("i"))

print(name.startswith("siya"))

print(name.startswith("j"))

print(name.endswith("!"))

print(name.endswith('ir'))

words = ["hello" , "world"]
print("".join(words))

print(name.capitalize())
print(name.center(50, "*"))