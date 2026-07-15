import math
while True:
    op = input("Choose(+,-,*,/,sin,cos)or 'end':")
    if op =="end":
        print("Calculator shutting down...")
        break
    if op in ["+","-","*","/"]:
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        if op == "+":
            print("Result:", a+b)
        elif op == "-":
            print("Result:", a-b)
        elif op == "*":
            print("Result:", a*b)
        elif op =="/":
            if b == 0:
                print("Cannot divide by zero")
            else:
                print("Result:", a/b)
    elif op == "sin":
        choice = input("Degrees(d) or Radian(r):")
        num=float(input("Enter number:"))
        if choice == "d":
            num = math.radians(num)
        print("Result:", math.sin(num))
    elif op == "cos":
        choice = input("Degrees(d) or Radians(r):")
        num=float(input("Enter number:"))
        if choice == "r":
            num = math.radians(num)
            print("Result:",math.cos(num))
        else:
            print("Invalid operator")
            
                               