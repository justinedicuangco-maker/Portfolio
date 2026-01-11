# only one question (What is the capital of france?)
answer = input("What is the capital of France? ")

if answer == "Paris":
    print("Correct!")
else:
    print("Wrong!")

# advanced requirement
questions = {
    "France": "paris",
    "Germany": "berlin",
    "Italy": "rome",
    "Spain": "madrid",
    "Portugal": "lisbon",
    "Netherlands": "amsterdam",
    "Belgium": "brussels",
    "Austria": "vienna",
    "Sweden": "stockholm",
    "Norway": "oslo"
}

for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ").strip().lower()

    if answer == capital:
        print("Correct!")
    else:
        print("Wrong!")