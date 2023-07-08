# Create Rock Paper Scissors game with against computer!
def rock_paper_scissors():
    # The program should convert this value into Rock, Paper os Scissors
    # Set variables
    r = 'Rock'                                                  # here the Letters Variables have been set
    p = 'Paper'                                                 # A Dictionary could also have been used but would also
    s = 'Scissors'                                              # have changed following code
    rps_list = ['Rock', 'Paper', 'Scissors']                    # this list was created to assign numbers from requested
#                                                               # random int(0,2) to a value
    # Prompt user to enter value: R, P or S
    print('Welcome to Rock(R) Paper(P) Scissors(S)!')
    user_input = input('To play please type R,P or S here ')

    if user_input.upper() == 'R':                                 # This sets the user input to the variable above
        print('You have selected', r)                             # the .upper means input can take upper and lower
    elif user_input.upper() == 'P':                               # args as it converts all to upper
        print('You have selected', p)
    elif user_input.upper() == 'S':
        print('You have selected', s)
    else:
        print('Invalid input. Please try again.')       # This line lets user know if they put in the wrong parameters

# Asks the computer to generate a random value between 0 and 2
    import random                                                       # had we used dictionary to store our values we
    r_num = random.randint(0, 2)                                        # could've used random.choice to pick random str
#                                                                #instructions asked for int (0,2) so found this easier

    # Convert computers choice, 0 becomes Rock; 1 becomes Paper ; 2 becomes Scissors respectively
    comp_choice = rps_list[r_num]                                          # converts rand int into str from above list
    print('Computer has guessed ' + comp_choice)                           # ie. r_num in list into comp_choice


# Compare the users choice with the computers choice to display message indicating whether user won,lost, or drew
# Rock smashes Scissors, Paper wraps Rock, Scissors cut Paper!

    if user_input.upper() == 'R' and comp_choice == 'Scissors':
        print('Your mighty Rock has smashed Scissors blade, You Win!')
    elif user_input.upper() == 'R' and comp_choice == 'Paper':
        print('Your feeble  Rock has been smothered by Paper, You loose!')
    elif user_input.upper() == 'Paper' and comp_choice == 'Scissors':
        print('Your Paper has been shredded by scissors blades, You loose!')
    elif user_input.upper() == 'Paper' and comp_choice == 'Rock':
        print('Your powerful Paper has wrapped the Rock, You Win!')
    elif user_input.upper() == 'Scissors' and comp_choice == 'Rock':
        print('Your Scissors have been blunted by the mighty Rock, You loose!')
    elif user_input.upper() == 'Scissors' and comp_choice == 'Paper':
        print('Your Scissors have shredded the Papers threat, You Win!')
    else:
        print('You have come across a worthy opponent, Draw!')


rock_paper_scissors()
# The above could have been shortened and simplified using generic you win, or you lose statements.
# as all outputs were tailored to each individual answer they all required different statements

# if user_input.upper() == comp_choice:
#     print('You have come across a worthy opponent, Draw!')
# elif user_input.upper() == 'Rock' and comp_choice == 'Scissors':
#     print('You Win!')
# elif user_input.upper() == 'Paper' and comp_choice == 'Rock':
#     print('You Win!')
# elif user_input.upper() == 'Scissors' and comp_choice == 'Paper':
#     print('You Win!')
# else:
#     print('You loose!')


# rock_paper_scissors()


# showcase what you have learnt and create your own functions
# See Rock_paper_scissor file