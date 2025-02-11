from random import choice

x = float(input("Enter x:"))
y = float(input("Enter y:"))

def add(x , y):
    print(x+y)
def Sub(x , y):
    print(x-y)
def pro(x , y):
    print(x*y)
def quo(x , y):
    if y == 0:
        print("Zero division Error.")
    print(x/y)

print("Select operator")
print("1.add")
print("2.Sub")
print("3.pro")
print("4.quo")

while True:
    choice = input("Enter Choice(1/2/3/4):")

    if choice == '1':
        print(add(x,y))
    elif choice == '2':
        print(Sub(x,y))
    elif choice == '3':
        print(pro(x,y))
    elif choice == '4':
        print(quo(x,y))
