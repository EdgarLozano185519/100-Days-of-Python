def calculate(first, operation, second):
  if operation == "+":
    return first + second
  elif operation == "-":
    return first - second
  elif operation == "*":
    return first*second
  elif operation == "/":
    return first/second

while True:
  first = float(input("Enter first number: "))
  print("+\n*\n-\n/")
  operation = input("Pick an operation: ")
  second = float(input("Enter second number: "))
  result = calculate(first, operation, second)
  print(f"The result is {result}")
  answer = input("Do you want to use the result in another calculation? ")
  while answer == "y":
    operation = input("Enter an operation to use with last result: ")
    second = float(input("Enter another number: "))
    result = calculate(result, operation, second)
    print(f"The result is {result}")
    answer = input("Do you want to use the result in another calculation? ")
    