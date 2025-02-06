import math

def advanced_calculator():
    history = []
    memory = 0
    
    while True:
        print("\nCalculator with Memory")
        print("1. Basic Operation")
        print("2. Square Root")
        print("3. Power")
        print("4. Memory Options")
        print("5. History")
        print("6. Exit")
        
        choice = input("Choose (1-6): ")
        
        if choice == '1':
            try:
                num1 = float(input("First number: "))
                op = input("Operation (+,-,*,/): ")
                num2 = float(input("Second number: "))
                
                if op == "/" and num2 == 0:
                    print("Error: Cannot divide by zero")
                    continue
                    
                result = eval(f"{num1}{op}{num2}")
                print(f"Result: {result}")
                history.append(f"{num1} {op} {num2} = {result}")
                
            except:
                print("Invalid input")
                
        elif choice == '2':
            try:
                num = float(input("Enter number: "))
                result = math.sqrt(num)
                print(f"Square root: {result}")
                history.append(f"√{num} = {result}")
            except:
                print("Invalid input")
                
        elif choice == '3':
            try:
                base = float(input("Base: "))
                power = float(input("Power: "))
                result = math.pow(base, power)
                print(f"Result: {result}")
                history.append(f"{base}^{power} = {result}")
            except:
                print("Invalid input")
                
        elif choice == '4':
            print("\nMemory Options:")
            print("1. Store current result")
            print("2. Recall memory")
            print("3. Clear memory")
            mem_choice = input("Choose (1-3): ")
            
            if mem_choice == '1' and 'result' in locals():
                memory = result
                print(f"Stored: {memory}")
            elif mem_choice == '2':
                print(f"Memory: {memory}")
            elif mem_choice == '3':
                memory = 0
                print("Memory cleared")
                
        elif choice == '5':
            print("\nHistory:")
            for calc in history:
                print(calc)
                
        elif choice == '6':
            break

if __name__ == "__main__":
    advanced_calculator()