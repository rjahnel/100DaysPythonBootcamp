def ClearScreen():
    print("\033[H\033[J", end="")    # Bildschirm löschen

def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"What is like in {location}.")

ClearScreen()
greet_with("Jack Bauer", "New York City")
