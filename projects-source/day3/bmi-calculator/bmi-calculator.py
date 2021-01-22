weight_pounds = float(input("Enter your weight in pounds: "))
height_inches = int(input("Please enter a height in inches: "))
bmi = (weight_pounds/(height_inches**2))*703
if bmi < 18.5:
  print("You are under weight.")
elif 18.5 <= bmi <= 24.9:
  print("Your weight is normal.")
elif 25.0 <= bmi <= 29.9:
  print("You are overweight.")
else:
  print("You are obese.")