def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("Enter a choice : \n1.Add\n2.Substraction\n3.Multiplication\n4.Division")
# input part
i=int(input('Choose a number (1/2/3/4): '))
x1=int(input('Enter 1st no.: '))
x2=int(input('Enter 2nd no.: '))
if i==1:
    print(add(x1,x2))
elif i==2:
    print(substract(x1,x2))
elif i==3:
    print(mul(x1,x2))
elif i==4:
    print(div(x1,x2))
