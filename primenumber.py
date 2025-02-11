
number = int(input("Enter Number:"))
if number <=1:
    print("Not a prime")
if i in range (2, int(number**0.5)+1):
    if number % i == 0:
        print("Not a prime")
    else:
        print("Prime number")


