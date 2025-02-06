def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+,-,*,/): ")
    num2 = float(input("Enter second number: "))
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        return "Invalid operation"
        
    return f"Result: {result}"

print(calculator())

def advanced_calculator():
    history = []
    
    while True:
        print("\nAdvanced Calculator")
        print("1. Calculate")
        print("2. View History")
        print("3. Exit")
        
        choice = input("Choose option (1-3): ")
        
        if choice == '1':
            try:
                num1 = float(input("Enter first number: "))
                operation = input("Enter operation (+,-,*,/): ")
                num2 = float(input("Enter second number: "))
                
                if operation == "+":
                    result = num1 + num2
                elif operation == "-":
                    result = num1 - num2
                elif operation == "*":
                    result = num1 * num2
                elif operation == "/":
                    if num2 == 0:
                        print("Error: Cannot divide by zero")
                        continue
                    result = num1 / num2
                else:
                    print("Invalid operation")
                    continue
                
                calculation = f"{num1} {operation} {num2} = {result}"
                history.append(calculation)
                print(f"Result: {result}")
                
            except ValueError:
                print("Please enter valid numbers")
                
        elif choice == '2':
            print("\nCalculation History:")
            for calc in history:
                print(calc)
                
        elif choice == '3':
            break

print(advanced_calculator())
