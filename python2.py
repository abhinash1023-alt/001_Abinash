# Mini Calculator with fixed numbers

print("Welcome to Mini Calculator!")

# Directly assign numbers here
num1 = 5
num2 = 3

# Show operation options
print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Choose which operation you want
choice = '1'  # you can change this to '2', '3', or '4'

# Perform calculation
if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid choice!")
