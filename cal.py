def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
print("1. Addition")
print("2. Multiplication")

choice = input("Enter choice (1/2):")

if choice == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif choice == '2':
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")
else:
    print("Invalid input")

   