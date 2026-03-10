input_string = input("please Enter a word and i will tell whether its a palindrome or not: ").lower().replace(" ","")

reversed_string = input_string[::-1]

if input_string != reversed_string:
    print(f"Provided word {input_string} is not a palindrome")
else:
      print(f"Provided word {input_string} is a palindrome")

