even_sum = 0
for number in range(1,101):
  if number%2 == 0:
    even_sum += number

print("The even sum from 1 to 100 is " + str(even_sum))