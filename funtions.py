# Built-in functions?Standard-Library function

y = max(67,39,56,78, 87)
print("the maximum value is",y)

x = min(67,56,59,39,3)
print("the minimum value is",x)

# User-defined functions
def name ():
    print("Joseph")
name()# calling a function

def product():
    x = 2
    y = 3
    print(x*y)

product()

#Parameter/variable and Argument/Value
def add(a,b):
    print(a+b)
add(34,45)
add(6,7)

#
def employee(name,gender,position,salary,age):
    print(name,gender,position,salary,age)
employee("joseph","male","CEO",120000,26)
employee("john","male","Managing director",120000,26)
employee("Mary","Female","HR",120000,30)

# A program that displays detailes of 5 students.
# fullname , age , course,gender

def student (Fullname,age,course,gender):
    print(Fullname,age,course,gender)
student("Ian Mwaura",18,"Ethicalhacking","Male")
student("Ken Sahwman",20,"MIT","Male")
student("Mary wanjiru",17,"MIT","female")
student("Dennis Gitau",18,"Fullstack","Male")
student("Joylene mutua",19,"Cybersecurity","female")