HISTORY_FILE = "Python Projects\Project_2\history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No history found!")
    else: 
        for line in reversed(lines):
            print(line.strip())

    file.close()

def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("History cleared.")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()
    print("Result saved to history.")
    
def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use format: number operator number (e.g., 2 + 3)")
        return

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. USE ONLY + - * /")
        return

    if int(result) == result:
        result = int(result)

    print(f"Result: {result}")
    save_to_history(user_input, result)
    
def main():
    print('---SIMPLE CALCULATOR (type history, clear or exit)')
    while True:
        user_input = input("Enter calculation (+ - * /) or command (history, clear or exit): ")
        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

if __name__ == "__main__":
    main()
    
    
    
'''
# NEW CODE FOR REFERENCE isme space nhi dena padta h no. and operator ke bich me old wala me dena padta h
def calculate(user_input):
    for operator in ["+", "-", "*", "/"]:
        if operator in user_input:
            parts = user_input.split(operator)
            if len(parts) == 2:
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())

                if operator == "+":
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "*":
                    result = num1 * num2
                elif operator == "/":
                    if num2 == 0:
                        print("Cannot divide by zero.")
                        return
                    result = num1 / num2

                if int(result) == result:
                    result = int(result)

                print(f"Result: {result}")
                save_to_history(user_input, result)
                return
    print("Invalid input. Use format: number operator number (e.g., 2+3 or 2 + 3)")
'''

