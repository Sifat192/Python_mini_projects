def intro():
    print("Welcome to Calculator")
    print("Choose one operation: ")
    print(" 1. Add","\n","2. Sub","\n","3. Exit")
intro()
ops = int(input("Select the operation: "))
while(ops != 3):
    match ops:
        case 1:
            print("Let's perfome the addition operation")
            print("Give two numbers on two lines")
            a = int(input("Number 1 is: "))
            b = int(input("Number 2 is: "))
            print(f"The sum is: {a+b}")
            intro()
            ops = int(input("Select the operation: "))
        case 2:
            print("Let's perform the subtraction operation")
            print("Give two numbers on two lines")
            a = int(input("Number 1 is: "))
            b = int(input("Number 2 is: "))
            print(f"The difference is: {a-b}")
            intro()
            ops = int(input("Select the operation: "))
        case 3:
            break
print("Exiting the calculator, bye bye!")

