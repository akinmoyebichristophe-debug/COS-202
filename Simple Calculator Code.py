print("================================")
print("   MATHEMATICAL CALCULATOR")
print("================================")

while True:
    print("\nSelect an Operation")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("\\  Integer Division")
    print("^  Power")
    print("%  Modulus")
    print("C  Clear")
    print("OFF  Exit")

    choice = input("\nEnter your choice: ")

    if choice == "OFF":
        print("Calculator Closed.")
        break

    elif choice == "C":
        print("\nScreen Cleared.")
        continue

    elif choice in ["+", "-", "*", "/", "\\", "^", "%"]:

        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == "+":
            answer = num1 + num2

        elif choice == "-":
            answer = num1 - num2

        elif choice == "*":
            answer = num1 * num2

        elif choice == "/":
            if num2 == 0:
                print("Division by zero is not allowed.")
                continue
            answer = num1 / num2

        elif choice == "\\":
            if num2 == 0:
                print("Division by zero is not allowed.")
                continue
            answer = num1 // num2

        elif choice == "^":
            answer = num1 ** num2

        elif choice == "%":
            if num2 == 0:
                print("Division by zero is not allowed.")
                continue
            answer = num1 % num2

        print("Answer =", answer)

    else:
        print("Invalid Choice!")
