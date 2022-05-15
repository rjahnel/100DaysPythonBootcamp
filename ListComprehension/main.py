import random

import pandas

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [n+1 for n in numbers]
print(new_list)
name = "Jahnel"
name_list = [letter.upper() for letter in name]
print(name_list)
double_list = [n * 2 for n in range(1, 5)]
print(double_list)
num2_list = [n * 2 for n in range(1, 10) if n % 2 == 0]
print(num2_list)
names = ["Susanne", "Rolf", "Finn", "Hannah-Sofie", "Marco", "Lucy"]
cap_names = [name.upper() for name in names if len(name) > 5]
print(cap_names)

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
square_nums = [n**2 for n in nums]
print(square_nums)
result = [n for n in nums if n % 2 == 0]
print(result)

numbers_1 = [int(line.strip()) for line in open("file1.txt", "r")]
numbers_2 = [int(line.strip()) for line in open("file2.txt", "r")]
result2 = [number for number in numbers_1 if number in numbers_2]
print(result2)

students = ["Susanne", "Rolf", "Finn", "Hannah-Sofie", "Marco", "Lucy"]
new_scores = {student: random.randint(1, 100) for student in students}
passed_students = {student: score for (student, score) in new_scores.items() if score > 25}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)


def c_to_f(celsius):
    return celsius * 9/5 + 32


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: c_to_f(temp) for (day, temp) in weather_c.items()}
print(weather_f)

student_dict = {
    "student": ["Susanne", "Rolf", "Hannah-Sofie", "Finn"],
    "score": [56, 33, 44, 72]
}

# # Lopping through dictionary
# for (key, value) in student_dict.items():
#     print(key, value)
#
student_dataframe = pandas.DataFrame(student_dict)
# print(student_dataframe)
#
# for (key, value) in student_dataframe.items():
#     print(value)

# iter rows
for (index, row) in student_dataframe.iterrows():
    print(f"{index}. {row.student} = {row.score}")