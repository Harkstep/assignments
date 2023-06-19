# create bank pin request with suitable output and three wrong pin requests.

# use variables to set changeable parameters within the code. This allows the number of pin attempts  and the pin to be
# changed at any point without altering any code (without hard coding)
user_pin = '1234'
max_tries = 3



                                                                         # This sets a loop to repeat while there are
while max_tries > 0:                                                     # more than 0 attempts left
    if input('Enter your pin: ') == user_pin:                            # This states if input(pin attempt) is equal to
        print('Pin Correct')                                             # the user pin the print statement applies
        break                                                            # This ends the loop if statement True
    else:                                                                # else continues instructions if False
        max_tries -= 1                                                   # This counts down one from set variable
        print('Your pin is incorrect,', max_tries, 'tries remaining')    # output is strings + changing variable
        if max_tries == 0:                                               # This statement only triggers a second output
             print('Your card has been retained')                        # stating what happens now no more tries




# #Ex10  Q3 Optional extra

# import getpass   - This does not work on PYcherm but does in CMD prompt or similar
#
# user_pin = '1234'
# max_tries = 3
#
# while max_tries > 0:
#     if getpass.getpass('Enter your pin: ') == user_pin:
#         print('Correct')
#         break
#     else:
#         max_tries -= 1
#         print('Your pin is incorrect,', max_tries, 'tries remaining')
#         if max_tries == 0:
#             print('Your card has been retained')
