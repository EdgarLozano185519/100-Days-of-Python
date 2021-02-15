# Without Pandas
#import csv

#with open("weather_data.csv") as file:
#  reader = csv.reader(file)
#  temperatures = []
#  for row in reader:
#    if row[1].isnumeric():
#      temperatures.append(int(row[1]))
#  print(temperatures)

# With pandas
import pandas

data = pandas.read_csv("weather_data.csv")
#print(data['temp'])
data_dict = data.to_dict()
#print(data_dict)
temp_list = data['temp'].to_list()
#print(temp_list)

# Get the average and max temp
#average = data['temp'].mean()
#max_temp = data['temp'].max()
#print(f"Average temperature: {average}")
#print(f"Max temperature: {max_temp}")

#print(data[data.temp == data.temp.max()])
day_celsius = data[data.day == 'Monday'].temp
day_f = (day_celsius*1.8)+32
print(day_f)