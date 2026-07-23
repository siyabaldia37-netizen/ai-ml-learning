# easy strigs problems

# Create a string containing your name and print it.

# Create a string containing your college name.

# Print the first character of "Python".

# Print the last character of "Programming" using negative indexing.

# Print the length of "Artificial Intelligence".

# Convert "python" to uppercase.

# Convert "PYTHON" to lowercase.

# Capitalize the string "hello world".

# Remove leading and trailing spaces from " OpenAI ".

# Replace "Java" with "Python" in "I love Java".

# solutionss




name = "siya baldia"
print(name)

college_name = "PES Universtiy "
print(college_name)

str = "python"
print(str[0])

print("Python"[0])

str1 = "programming "
print(str1[-1])

str3 = "Artificial Intelligence"
print(len(str3))

str4  = "python"
print(str4.upper())

str5 = "PYTHON"
print(str5.lower())

str6 = "hello world"
print(str6.capitalize())

str7 = " OpenAI"
print(str7.strip())

str8 = "I love java"
str9 = str8.replace("java", "python")
print(str9)



# medium problems on strings


# Print the first five characters of "Programming".

# Print the last four characters of "ComputerScience".

# Count how many times 'a' appears in "banana and mango".

# Check whether "AI" is present in "Learning AI with Python".

# Check whether "Java" is present in "Learning Python".

# Join the list ["Python", "is", "fun"] using spaces.

# Split "red,green,blue,yellow" into a list.

# Repeat "Hello " five times.

# Use an f-string to print your name, age, and favorite programming language.

# Check whether "report.pdf" ends with ".pdf".

# solutions

word = "Programming" 
print(word[0:4])

word2 = "Computerscience"
print(word2[-4:])

word3 = "banana and mango"
print(word3.count("a"))

word4 = "Learning AI with Python"
print("AI" in word4)

word5 = "Learning python"
print("Java" in word5)

word6 =["python" , "is" , "love"]

print(" ".join(word6))

word7 = "red,green,yellow,blue"
print(word7.split(","))

word8 = "Hello"
print(word8 *5)

love = "Siya"
old = 19
fav_language = "Python"
print(f"MY name is {love} and i am {old} years old and my favorite language is {fav_language}")

word9 = "report.pdf"
print(word9.endswith(".pdf"))

word10 = "pythons"
print(word10.startswith("py"))

word11 = "siya1"
print(word11.isalnum())

word12 = "siya123"
print(word12.isalpha())

word13  = "siya"
print(word13.isdigit())


# difficult problems on string 

# Ask the user to enter their full name and print:
# Original name
# Uppercase
# Lowercase
# Length

# Ask the user to enter a sentence and count the number of spaces.

# Ask the user to enter a word and print it in reverse using slicing.

# Ask the user to enter a sentence and check whether it starts with a vowel.

# Count the number of vowels in a user-entered string.

# Ask the user to enter an email address and check whether it ends with "@gmail.com" or ".com".

# Ask the user to enter a sentence and replace every occurrence of "Python" with "AI".

# Ask the user to enter a sentence and print each word on a new line using split().

# Ask the user to enter a sentence and print the longest word in it.

# Build a mini "Profile Formatter" that asks for a user's name, city, and profession, then displays the information in a neatly formatted sentence using an f-string, with the name in title case and the city in uppercase.


# solutions 

ask = input("enter your full name:")
print("oriinal name:" , ask)
print("uppeercase:" , ask.upper())
print("lowercase:" , ask.lower())
print("lenght:" , len(ask))

sentancee = input("enter a sentance:")
print("number of spaces:" , sentancee.count(""))

sentance1 = input("enter a sentacnce:")
print("normal:", sentance1)

print(sentance1[::-1])

vowel = input("enter a sentance")
print(vowel[0].lower() in "aeiou")

string = input("enter the string")
count = 0
for ch in string:
    if ch.lower() in "aeiou":
        count = count+1
        print(count)

email = input("enter your email:")
email1 = email.endswith("@gmail.com" or ".com")
print(email1)

string1 = input("enter your string")
string2 = string1.replace("Python" , "AI")
print(string2)

string3 = input("enter your sentance :")
string4 = " \n".split(string3)
print(string4)

love1 = input("enter your name:")
love2 = love1.title()
city  = input("enter the name:")
city1 = city.upper()

print(f"my name is {love2} and i live{city1}")




