import random
score = 0
while(1):
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    print("Score is " + str(score))
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            score += 1
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            score += 1
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            score += 1
        else:
            print("Rock smashes scissors! You lose.")
    print("Your Final Score is " + str(score))

    option = int(input("Do you want to continue the Game , If yes then Type 1 e, If no then Type 2 \n"))
    if(option == 1):
        continue
    else:
        exit()
