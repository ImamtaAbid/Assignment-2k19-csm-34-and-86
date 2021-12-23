#Calculator
print("Choose your operation: ")
print("1. Add")
print("2. Substraction")
print("3. Multiply")
print("4. Divide")

operation = int(input())

if operation == 1:
    num1 = int(input("Enter your 1st value: "))
    num2 = int(input("Enter your 2nd value: "))
    print("The sum of", num1,"and" ,num2 ," is ",int(num1+num2))
elif operation == 2:
    num1 = int(input("Enter your 1st value: "))
    num2 = int(input("Enter your 2nd value: "))
    print("The substration of", num1,"and" ,num2 ," is ",int(num1-num2))
