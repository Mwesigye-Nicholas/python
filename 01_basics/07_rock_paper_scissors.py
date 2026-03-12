
allowed_answers = ["rock", "paper","scissors"]

player_one = input("Enter value for player one , please choose among(rock, paper or scissors): ").lower()

player_two = input("Enter value for player two , please choose among(rock, paper or scissors): ").lower()



    
if player_one not in allowed_answers or player_two not in allowed_answers:
    raise ValueError("Invalid input please, run the program again")
elif player_one == "rock" and player_two == "scissors":
    print("Player one won")
elif player_one == "scissors" and player_two == "paper":
    print("Player one won")
elif player_one == "paper" and  player_two == "rock":
    print("Player one won")
elif  player_two == "rock" and  player_one == "scissors":
    print("Player two won")
elif player_two == "scissors" and  player_one == "paper":
    print("Player two won")
elif  player_two == "paper" and  player_one == "rock":
    print("Player two won")
elif player_one == player_two:
    print("Its a tie.")

    

    
    