import random
def win():
    print ('You win!')
def lose():
    print ('You lose!')
def rock_paper_scissor():
    while True:
        player_choice = input('What do you pick? (rock, paper, scissors):')
        random_move = random.randint(0, 2)
        moves = ['rock', 'paper', 'scissors']
        computer_choice = moves[random_move]
        if player_choice == computer_choice:
            print ('Draw!')
            print(computer_choice)
        elif player_choice == 'rock' and computer_choice == 'scissors':
            win()
            print(computer_choice)
        elif player_choice == 'paper' and computer_choice == 'scissors':
            lose()
            print(computer_choice)
        elif player_choice == 'scissors' and computer_choice == 'paper':
            win()
            print(computer_choice)
        elif player_choice == 'scissors' and computer_choice == 'rock':
            lose()
            print(computer_choice)
        elif player_choice == 'paper' and computer_choice == 'rock':
            win()
            print(computer_choice)
        elif player_choice == 'rock' and computer_choice =='paper':
            lose()
            print(computer_choice)
        elif player_choice == computer_choice :
            lose()
            print(computer_choice)
        again = input('Do you want to play again? y or n ')
        if again == 'n':
            break
rock_paper_scissor()