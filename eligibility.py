#program to check a person's eligiblity to vote based on their age
# Function to check eligibility to vote
try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You can vote!")
    else:
        print("You cannot vote.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
