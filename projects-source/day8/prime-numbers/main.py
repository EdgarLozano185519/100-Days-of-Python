num = int(input("Enter a number to see if it is prime: "))

count = 0
for i in range(1,num):
  if num%i == 0:
    count += 1

if count > 1:
  print(f"{num} is not a prime number.")
else:
  print(f"{num} is a prime number.")
