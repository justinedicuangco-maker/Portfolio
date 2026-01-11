names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search = input("Enter a name to search: ")

if search in names:
    print(f"{search} was found in the list.")
else:
    print(f"{search} was not found in the list.")