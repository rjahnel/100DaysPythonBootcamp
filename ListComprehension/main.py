import random
import pandas

# create list [2, 3, 4, ...]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [n+1 for n in numbers]
print(new_list)

# create list ['J', 'A', 'H', ...]
name = "Jahnel"
name_list = [letter.upper() for letter in name]
print(name_list)

# create list [2, 4, 6, 8]
double_list = [n * 2 for n in range(1, 5)]
print(double_list)

# create list [4, 8, 12, 16] with condition (even number)
num2_list = [n * 2 for n in range(1, 10) if n % 2 == 0]
print(num2_list)

# create list ['SUSANNE', 'HANNAH-SOFIE']
names = ["Susanne", "Rolf", "Finn", "Hannah-Sofie", "Marco", "Lucy"]
cap_names = [name.upper() for name in names if len(name) > 5]
print(cap_names)

# create list [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
square_nums = [n**2 for n in nums]
print(square_nums)

# create list [2, 8, 34]
result = [n for n in nums if n % 2 == 0]
print(result)

# create list [3, 6, 13, 5, 3, 7, 5, 12, 33, 42]
numbers_1 = [int(line.strip()) for line in open("file1.txt", "r")]
numbers_2 = [int(line.strip()) for line in open("file2.txt", "r")]
result2 = [number for number in numbers_1 if number in numbers_2]
print(result2)

# create dictionary:
# new_scores: {'Susanne': 50, 'Rolf': 84, 'Finn': 88, 'Hannah-Sofie': 55, 'Marco': 43, 'Lucy': 49}
# passed_students: {'Susanne': 50, 'Rolf': 84, 'Finn': 88, 'Hannah-Sofie': 55, 'Marco': 43, 'Lucy': 49}
import random
students = ["Susanne", "Rolf", "Finn", "Hannah-Sofie", "Marco", "Lucy"]
new_scores = {student: random.randint(1, 100) for student in students}
passed_students = {student: score for (student, score) in new_scores.items() if score > 25}
print(passed_students)

# create dictionary:
# result: {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# create dictionary: 
# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}

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

# Looping through a dictionary
# Output:
# key: student, value: ['Susanne', 'Rolf', 'Hannah-Sofie', 'Finn']
# key: score, value: [56, 33, 44, 72]

student_dict = {
    "student": ["Susanne", "Rolf", "Hannah-Sofie", "Finn"],
    "score": [56, 33, 44, 72]
}

# Lopping through dictionary
for (key, value) in student_dict.items():
     print(f"key: {key}, value: {value}")

# create Dataframe from dictionary
# and print values

import pandas
student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# Output:
#         student  score
# 0       Susanne     56
# 1          Rolf     33
# 2  Hannah-Sofie     44
# 3          Finn     72

for (key, value) in student_dataframe.items():
    print(value)

# Output:
# Name: student, dtype: object
# 0    56
# 1    33
# 2    44
# 3    72
# Name: score, dtype: int64

# iter rows
for (index, row) in student_dataframe.iterrows():
    print(f"{index}. {row.student} = {row.score}")

# Output:  
# 0. Susanne = 56
# 1. Rolf = 33
# 2. Hannah-Sofie = 44
# 3. Finn = 72
