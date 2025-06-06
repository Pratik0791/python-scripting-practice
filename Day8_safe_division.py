def safe_division():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2
    except ValueError:
        print(f"❌ {ValueError}Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        print(f"❌ {ZeroDivisionError}Cannot divide by zero!")
    else:
        print(f"✅ Result: {result}")

# Run the function
safe_division()
