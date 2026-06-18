import math

print("========== Scientific Calculator ==========")

while True:
    print("\nChoose an Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Log Base 10")
    print("11. Natural Log (ln)")
    print("12. Factorial")
    print("13. Exit")

    choice = input("Enter your choice (1-13): ")

    if choice == "13":
        print("Thank you for using the Scientific Calculator!")
        break

    if choice in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result =", num1 + num2)

        elif choice == "2":
            print("Result =", num1 - num2)

        elif choice == "3":
            print("Result =", num1 * num2)

        elif choice == "4":
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Error! Cannot divide by zero.")

        elif choice == "5":
            print("Result =", math.pow(num1, num2))

    elif choice == "6":
        num = float(input("Enter a number: "))
        if num >= 0:
            print("Result =", math.sqrt(num))
        else:
            print("Error! Square root of a negative number is not possible.")

    elif choice == "7":
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.sin(math.radians(angle)))

    elif choice == "8":
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.cos(math.radians(angle)))

    elif choice == "9":
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.tan(math.radians(angle)))

    elif choice == "10":
        num = float(input("Enter a number: "))
        if num > 0:
            print("Result =", math.log10(num))
        else:
            print("Error! Log is only defined for positive numbers.")

    elif choice == "11":
        num = float(input("Enter a number: "))
        if num > 0:
            print("Result =", math.log(num))
        else:
            print("Error! Natural log is only defined for positive numbers.")

    elif choice == "12":
        num = int(input("Enter a whole number: "))
        if num >= 0:
            print("Result =", math.factorial(num))
        else:
            print("Error! Factorial is only defined for non-negative integers.")

    else:
        print("Invalid choice! Please try again.")