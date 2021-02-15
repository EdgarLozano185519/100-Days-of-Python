import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = data[data['Primary Fur Color'] == 'Gray']
gray_count = len(gray)
print(f"Gray: {len(gray)}")
cinnamon = data[data['Primary Fur Color'] == 'Cinnamon']
cinnamon_count = len(cinnamon)
print(f"Cinnamon: {len(cinnamon)}")
black= data[data['Primary Fur Color'] == 'Black']
black_count = len(black)
print(f"Black: {len(black)}")

colors = {
  "Fur Color": ['Gray', 'Black', 'Cinnamon'],
  "Count": [gray_count, black_count, cinnamon_count]
}
df = pandas.DataFrame(colors)
df.to_csv("data.csv")