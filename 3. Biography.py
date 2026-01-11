# hardcoded values
bio = {
    "name": "Justine",
    "hometown": "Manila",
    "age": 18
}

print(bio["name"])
print(bio["hometown"])
print(bio["age"])

# advanced requirements
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age! Please enter a number.")
    age = 0

info = {
    "name": name,
    "hometown": hometown,
    "age": age
}
print(info["name"] + "\n" + info["hometown"] + "\n" + str(info["age"]))