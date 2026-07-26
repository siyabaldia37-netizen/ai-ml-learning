print("=" * 35)

print(" Student Report Card ")

print("=" * 35)

student_name = input("enter student name:")

roll_no = int(input("enter your roll no:"))

marks_english = int(input("enter your marks in english :"))

marks_maths = int(input("enter your marks in maths :"))

marks_science = int(input("enter your marks in scienece:"))

total  = marks_english + marks_science + marks_maths

percentage = (total  / 300) * 100

print( f"Name :{student_name}")

print(f"Roll no :{roll_no}")

print(f"English :{marks_english}")

print(f"Maths :{marks_maths}")

print(f"science :{marks_science}")

print(f'Total :{total} ')

print(f"percentage :{percentage}")

if percentage >= 90:
    print( "Grade\t : A+")
elif 90>percentage>= 80:
    print("Grade\t : A")

elif 80> percentage >= 70 :
    print("Grade\t: B")
elif 70>percentage >=60 :
    print("Grade\t: C")
elif  35<=percentage <60:
    print("Grade\t : D")
else:
    print("fail")

print(" Result : pass " if percentage >=35 else "failed")

print("=" * 35)
print("Thank you !!1")
print("=" * 35)