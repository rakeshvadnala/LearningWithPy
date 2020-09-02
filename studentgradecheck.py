marks =input('Plase Enter Marks: ')
while  (not marks.isnumeric() or int(marks)>100 ):
        marks=input("Please enter valid marks: ")
marks=int(marks)
if  marks>=70:
    print('Grade "A"')
elif marks>=60:
    print('Grade "B"')
elif marks>=50:
    print('Grade "C"')
elif marks>=35:
    print('Grade "F"')
else:
    print("Failed in Exam")
