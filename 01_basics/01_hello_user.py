
try:
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    
    if age < 0:
        print("Age cannot be negative")
    elif age >= 100:
        print(f"Congs {name}, you have made 100 years, your are beyond our programme service")
    else:
        remaing_years = 100 - age
        print(f"Hello, {name}, your remaining with {remaing_years} years to make 100 years.")
except ValueError:
    print("Invalid input!, Please Enter a whole number for age.")