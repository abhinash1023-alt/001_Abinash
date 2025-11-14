import os

# Smart Mini Calculator with File History + Count

HISTORY_FILE = "history.txt"

# Load old history if file exists
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as file:
        history = [line.strip() for line in file.readlines() if line.strip()]
else:
    history = []

# Count of past calculations
calc_count = len(history)

print("Welcome to Smart Mini Calculator (with saved history & count)!")
print("Type 'exit' anytime to quit, 'history' to view results, or 'clear' to clear saved history.\n")
print(f"You have done {calc_count} calculation(s) so far.\n")

while True:
    # Ask for first number
    num1 = input("Enter first number (or 'history'/'clear'/'exit'): ").strip()
    if num1.lower() == "exit":
        break
    if num1.lower() == "history":
        if history:
            print("\n--- Calculation History ---")
            for i, item in enumerate(history, 1):
                print(f"{i}. {item}")
            print("---------------------------\n")
        else:
            print("History is empty.\n")
        continue
    if num1.lower() == "clear":
        history.clear()
        open(HISTORY_FILE, "w").close()  # clear file
        calc_count = 0
        print("History cleared. Count reset to 0.\n")
        continue

    # Ask for second number
    num2 = input("Enter second number (or 'history'/'clear'/'exit'): ").strip()
    if num2.lower() == "exit":
        break
    if num2.lower() == "history":
        if history:
            print("\n--- Calculation History ---")
            for i, item in enumerate(history, 1):
                print(f"{i}. {item}")
            print("---------------------------\n")
        else:
            print("History is empty.\n")
        continue
    if num2.lower() == "clear":
        history.clear()
        open(HISTORY_FILE, "w").close()
        calc_count = 0
        print("History cleared. Count reset to 0.\n")
        continue

    # Validate numbers
    try:
        num1f = float(num1)
        num2f = float(num2)
    except ValueError:
        print("Invalid number(s). Please enter valid numeric values.\n")
        continue

    # Operation menu
    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("Type 'history' to view results, 'clear' to clear history, or 'exit' to quit.\n")

    choice = input("Enter your choice (1/2/3/4): ").strip()
    if choice.lower() == "exit":
        break
    if choice.lower() == "history":
        if history:
            print("\n--- Calculation History ---")
            for i, item in enumerate(history, 1):
                print(f"{i}. {item}")
            print("---------------------------\n")
        else:
            print("History is empty.\n")
        continue
    if choice.lower() == "clear":
        history.clear()
        open(HISTORY_FILE, "w").close()
        calc_count = 0
        print("History cleared. Count reset to 0.\n")
        continue

    # Perform calculation
    if choice == '1':
        result = num1f + num2f
        op = '+'
    elif choice == '2':
        result = num1f - num2f
        op = '-'
    elif choice == '3':
        result = num1f * num2f
        op = '*'
    elif choice == '4':
        if num2f != 0:
            result = num1f / num2f
            op = '/'
        else:
            print("Error: Division by zero!\n")
            continue
    else:
        print("Invalid choice!\n")
        continue

    result_str = f"{num1f} {op} {num2f} = {result}"
    print("Result:", result, "\n")

    # Save to history list and file, update count
    history.append(result_str)
    with open(HISTORY_FILE, "a") as file:
        file.write(result_str + "\n")

    calc_count += 1
    print(f"You have done {calc_count} calculation(s) so far.")
    print("---------------------------------\n")

print(f"Calculator closed. Total calculations done this session (including past saved): {calc_count}. Goodbye! 👋")
