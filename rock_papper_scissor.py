
import random
GAME_OVER = False

choice = ['Rock', 'Paper', 'Scissor']

# initially score of both player user and computer are zero
user_score = 0
computer_score = 0

while not GAME_OVER:
    computer_choice = random.randint(0, 2)
    print('--------------------------------------------------------------------------------')
    user_choice = int(input("Your choice: \nRock[0]\nPaper[1]\nScissor[2]\nQuite[3]\n"))
    if user_choice == 3:
        print('Thank bye bye!!!')
        break;
    elif user_choice <= 2 and user_choice >= 0:
        if choice[computer_choice] == 'Rock' and choice[user_choice] == 'Scissor':
            print('Computer win\n', '\nComputer choice: ', choice[computer_choice], '\nYour choice: ' , choice[user_choice])
            computer_score += 1
        elif choice[computer_choice] == 'Rock' and choice[user_choice] == 'Paper':
            print('User win\n', '\nYour choice: ' ,choice[user_choice], '\nComputer choice: ',choice[computer_choice])
            user_score += 1
        elif choice[computer_choice] == 'Paper' and choice[user_choice] == 'Rock':
            print('Computer win\n', '\nComputer choice: ',choice[computer_choice], '\nYour choice: ' ,choice[user_choice])
            computer_score += 1
        elif choice[computer_choice] == 'Paper' and choice[user_choice] == 'Scissor':
            print('User win\n', '\nYour choice: ' ,choice[user_choice], '\nComputer choice: ', choice[computer_choice])
            user_score += 1
        elif choice[computer_choice] == 'Scissor' and choice[user_choice] == 'Rock':
            print('User win\n', '\nYour choice: ' ,choice[user_choice], '\nComputer choice: ',choice[computer_choice])
            user_score += 1
        elif choice[computer_choice] == 'Scissor' and choice[user_choice] == 'Paper':
            print('Computer win\n', '\nComputer choice: ',choice[computer_choice], '\nYour choice: ' ,choice[user_choice])
            computer_score += 1
        else:
            print('Tie', '\nComputer choice: ',choice[computer_choice], '\nYour choice: ' ,choice[user_choice])
    else:
        print('\nInvalid choice, Please try again!!')

    con = input('\nContinue?? Yes[Y]/No[N]\t').upper()
    if con == 'Y':
        GAME_OVER = False
    elif con == 'N':
        print('Thank bye bye!!!')
        GAME_OVER = True
    else:
        print('Invalid input')
        GAME_OVER = True

print('\nOveral Score')
print('Computer score: ', computer_score)
print('User score: ', user_score)
print('Result: ')
if user_score > computer_score:
    print('You win')
elif user_score < computer_score:
    print('Computer win')
else:
    print('Match tie')



