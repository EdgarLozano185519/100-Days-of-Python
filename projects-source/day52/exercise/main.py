# Create the logging_decorator() function 👇
def logging_decorator(function):
  def wrapper(*args, **kwargs):
    function(args[0])
    print(f"Function called: {function.__name__}")
    print(f"Function args: {args[0]}")
    # End of inner function
  return wrapper

# Use the decorator 👇
@logging_decorator
def hello(user):
  print("Hello user.")

hello("edgar")