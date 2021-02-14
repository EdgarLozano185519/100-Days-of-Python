#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

starting_path = "input/Letters/starting_letter.txt"
names_path = "input/Names/invited_names.txt"

names = []

# Open names file
with open(names_path) as file:
  temp = file.readlines()
  for line in temp:
    names.append(line.strip())

# Open sample letter
sample = []
with open(starting_path) as file:
  sample = file.readlines()

# Write letters to files using names
#print(sample)
for name in names:
  with open("Output/ReadyToSend/"+name+".txt", "w") as file:
    file.write(sample[0].replace("[name]", name))
    for i in range(1,len(sample)):
      file.write(sample[i])

print("Letters have been created and saved.")