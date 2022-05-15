import csv
import pandas

# with open("weatherData.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# with open("weatherData.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


def celsius_to_fahrenheit(temperature):
    return temperature * 9/5 + 32


data = pandas.read_csv("weatherData.csv")
temp_list = data["temp"].to_list()
print(temp_list)
max_temp = data.temp.max()
print(f"The average temperature is {data['temp'].mean():.2f}°.")
print(f"The min temperature is {data.temp.min():.2f}°.")
print(f"The max temperature is {max_temp:.2f}°.")
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
print(f"On monday the temperature is {monday_temp}°C this is {celsius_to_fahrenheit(monday_temp)}°F.")

# Dataframe from the scratch
data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
}

students = pandas.DataFrame(data_dict)
print(students)
students.to_csv("students.csv")



