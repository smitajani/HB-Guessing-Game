"""A number-guessing game."""
## Author: Smita Jani, created on 4/28/2020


name_str = input("\n\nWhat's your name? ")
print("Welcome to 'The Guessing Game!' " + name_str + ".\n")

my_random_num = 45          # Set my random number
correct_guess = False       # Initialize boolean variable to identify if user guessed correctly, to FALSE
total_attempts = 1          # Number of user attempts - initialize at 1

while (not correct_guess):      # Loop through until the user either guesses the right answer or decides to quit the game.
    user_guess = int(input("\nGuess the number I have in mind (between 1 and 100)...."))       # Get the number from user and convert to integer

    if (user_guess == my_random_num):               # Compare user entry with my number, if it matches,   
        correct_guess = True;                       # set the flag to TRUE to quit the loop
        print ("\n\nCONGRATULATIONS, you got it in " + str(total_attempts) + " attempts!!!\n")   # and congratulate the user!
    else:
        try_again = input("Sorry! that's not the right number. Try again? (Y/N)  ")
        if (try_again == "N"):
            #correct_guess = True;
            print ("\n")                   
            break                  # If user does not want to try again, set boolean flag to true to quit the loop 
        else:
            total_attempts = total_attempts + 1 
            need_hint = input("Do you need a hint? (Y/N)  ")     # Check if the user needs a hint
            if (need_hint == "Y"):
                if (user_guess >= 100):                             # Check if number entered by user is 100 or higher
                    print("Hmm.. you need to pick a number between 1 and 100\n")    
                elif (user_guess > my_random_num):                  # Check if number entered by user is higher than 'my_random_num' initialized above
                    print("*** Hint *** It's a lower number\n")        
                else:                                               # Since all the conditions above failed, then the number must be lower than 'my_random_num' initialized above
                    print("*** Hint *** It's a higher number\n")  
            else: 
                print ("\n")


