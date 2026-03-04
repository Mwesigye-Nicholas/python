divider = []
try:
    number = abs(int(input("Please enter a whole number: ")))
    if number == 0:
        print("Please enter a number greater than zero")
    else:
        for i in range(1, number + 1):
            if number % i == 0:
                divider.append(i)
        print(divider)
except ValueError:
    print("Invalid Entry, please enter a whole number")