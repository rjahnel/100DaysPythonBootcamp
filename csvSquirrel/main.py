import pandas

COLUMN = "Primary Fur Color"
colors = ["Gray", "Cinnamon", "Black"]

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_count = []
for color in colors:
    color_count.append(len(data[data[COLUMN] == color]))

squirrels_dict = {
    "Fur Color": colors,
    "Count": color_count
}

df = pandas.DataFrame(squirrels_dict)
df.to_csv("squirrel_count.csv")
