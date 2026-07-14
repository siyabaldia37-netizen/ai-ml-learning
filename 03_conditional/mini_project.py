print("==" * 35)

print("report card ")

print("==" * 35)

student_name = input("enter student name:")

roll_no = int(input("enter your roll no:"))

marks_english = int(input("enter your marks in english :"))

marks_maths = int(input("enter your marks in maths :"))

marks_science = int(input("enter your marks in scienece:"))

total  = marks_english + marks_science + marks_maths

percentage = (total * 100)/ 3

print( "Name \t:",student_name)

print("Roll no \t:",roll_no)

print("English \t:", marks_english)

print("Maths \t:",marks_maths)

print("science \t:",marks_science)

print('Total \t:',total )

print( "percentage \t:",percentage)

if total >= 90:
    print( "Grade\t : A+")
elif 90>total >= 80:
    print("Grade\t : A")

elif 80> total >= 70 :
    print("Grade\t: B")
elif 70>total >=60 :
    print("Grade\t: C")
elif 60> total <=35:
    print("Grade\t : D")
else:
    print("fail")

print(" Result : pass " if total >=35 else "failed")

