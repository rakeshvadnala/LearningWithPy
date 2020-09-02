from datetime import date
x=int(input('Enter birth year: '))
def calc(x=x,y=date.today()):
	return y.year-x
print(calc())
