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


