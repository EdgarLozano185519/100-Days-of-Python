print("Welcome to the tip calculator.\n\n")
total = int(input("Cost of total bill?"))
people = int(input("Split between how many people?"))
tip = float(input("How much do you want to tip (in percentage)?"))/100
each_person_tip = (total*tip)/people
each_person_pays = float((total/people)+each_person_tip)
print("Each person will have to pay $" + str(each_person_pays))