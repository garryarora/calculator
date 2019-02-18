def add():
    print("Sum of ",a," and ",b," is ",a+b)
def sub():
    print("Difference of ",a," and ",b," is ",a-b)
def pod():
    print("Product of ",a," and ",b," is ",a*b)
def div():
    try:
        print("Sum of ",a," and ",b," is ",a/b)
    except ZeroDivisionError:
        print("Division by zero error. Try different input")
def mod():
    try:
        print("Remainder when ",b," is divided with ",a," is ",a%b)
    except ZeroDivisionError:
        print("Division by zero error. Try different input")


a=int(input("Enter 1st number : "))
op=input("Enter operator (+ - * / %) : ")
b=int(input("Enter 2nd number : "))


if op=='+':
    add()
elif op=='-':
    sub()
elif op=='*':
    pod()
elif op=='/':
    div()
elif op=='%':
    mod()
else:
    print("Please enter a valid operator")
