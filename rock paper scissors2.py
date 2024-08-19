import random
def tas_kagit_makas_AYŞENUR_SALAR():
    print("Welcome to Rock, Paper, Scissors Game!")
    print("Rules:")
    print("1. Rock beats Scissors.")
    print("2. Scissors beat Paper.")
    print("3. Paper beats Rock.")
    print("First to get 2 wins wins!")
    print("You can win, lose or draw.")
    print("You can type 'exit' to exit the game.\n")

    while True:
        computer_wins=0
        player_wins=0
        round=0
        while player_wins<2 and computer_wins<2:
            options=['rock','paper','scissors']
            player_choice=input("please choose 'rock','paper','scissors' or (type 'exit' to quit): ").lower()
            computer_choice=random.choice(options)
            print(f"computer chose: {computer_choice}")
            if player_choice=='exit':
                print('Game Over!')
                return
            if player_choice not in options:
                print("please choose 'rock','paper','scissors' or (type 'exit' to quit):  ")
                continue
            if computer_choice==player_choice:
                print("It's a tie")
                round+=1
                print(f"round:{round}")
                continue
            if player_choice=='rock' and computer_choice=='scissors':
                print('You won this round!')
                player_wins+=1
                round += 1
                print(f"round:{round}")
                print(f"player:{player_wins}")
                print(f"computer:{computer_wins}")
            elif player_choice=='paper' and computer_choice=='rock':
                print('You won this round!')
                player_wins+=1
                round += 1
                print(f"round:{round}")
                print(f"player:{player_wins}")
                print(f"computer:{computer_wins}")
            elif player_choice=='scissors' and computer_choice=='paper':
                print('You won this round!')
                player_wins+=1
                round += 1
                print(f"round:{round}")
                print(f"player:{player_wins}")
                print(f"computer:{computer_wins}")
            else:
                print('Computer won this round!')
                computer_wins += 1
                round += 1
                print(f"round:{round}")
                print(f"player:{player_wins}")
                print(f"computer:{computer_wins}")
        if player_wins == 2:
            print("Congratulations! You won the game!")
        elif computer_wins == 2:
            print("The computer won the game. Try again!")
        replay = input("Do you want to play another game? (yes/no): ").lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye.")
            break

        computer_replay = random.choice(['yes', 'no'])
        print(f"Computer wants to {'play again' if computer_replay == 'yes' else 'quit'}.")


        if computer_replay != 'yes':
            print("The computer has decided to quit. Game over.")
            break
tas_kagit_makas_AYŞENUR_SALAR()