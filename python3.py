# All-in-one Mini calculator

print("Welcome to All-in-one Calculator!")

# you can change these numbers
num1 = 5
num2 = 3
 
 # Perform all operations
print(f"\nNumbers: {num1} and {num2}")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
 print("Division:", num1 / num2)
else:
 print("Division: Error (cannot divide by zero)")