import random

thegame = ("rock", "paper", "scissors")
user_score = 0
computer_score = 0
#rounds = 1
Repeat = True
response = "Yes"
while Repeat == True:
    your_guess = input( "Choose: rock, paper, or scissors? " )
    computer_guess = random.choice(thegame)
    print("The computer picked: " + computer_guess + ".")

    user_rps = your_guess[0]
    computer_rps = computer_guess[0]
    #debug line
    #print(f"{your_guess} + {user_rps} + {computer_guess}")
    if user_rps == computer_rps:
        print("Tie, you both picked " + computer_guess)
    elif user_rps == 'r':
        if computer_rps == 's':
            print("ROCK beats SCISSORS; you WIN this round")
            user_score += 1
        elif computer_rps == 'p':
            print("PAPER beats ROCK; you LOSE this round")
            computer_score += 1

    elif  user_rps == "p":
        if computer_rps == 's':
            print("SCISSORS beats PAPER; you LOSE this round")
            computer_score += 1
        elif computer_rps == 'r':
            print("PAPER beats ROCK; you WIN this round")
            user_score += 1

    elif  user_rps == "s":
        if computer_rps == 'p':
            print("SCISSORS beats PAPER; you WIN this round")
            user_score += 1
        elif computer_rps == 'r':
            print("ROCK beats SCISSORS; you LOSE this round")
            computer_score += 1
    else:
        print("invalid choice.")

    print(f"The score is you: {user_score} computer: {computer_score}")
    response = input("Go again? ")
    Repeat = (response.lower()[0] == 'y')
    #rounds = rounds + 1

