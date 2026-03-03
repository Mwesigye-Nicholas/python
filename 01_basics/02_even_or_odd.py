try:
    number = int(input("Please enter a whole number and i will tell whether its even or odd: "))
    
   
    if number % 2 == 0:
        print(f"{number} is un even number")
    else:
     print(f"{number} is un odd number")
except ValueError:
    print("Invalid input, please enter a whole number.")