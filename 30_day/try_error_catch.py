# try except - finally

fruits = ["Apple", "Pear", "Banana", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print(f"Index: {index} out of range!")
    else:
        print(fruit + "pie")


#File not found
FILE_NAME = "test_file.txt"

try:
    file = open(FILE_NAME)
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
    
except FileNotFoundError:
    file = open(FILE_NAME, "w")
    file.write("Test-Entry")
    
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

else:
    content = file.read()
    print(content)
    make_pie(1)
    
finally:
    file.close()
    print("File was closed.")
    
        
    
    # raise TypeError("This is an errer thet I made up!")
    