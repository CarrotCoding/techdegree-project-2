import constants
import pdb


def show_menu():
    print("THE BASKETBALL TEAM CREATOR TOOL")
    print("VERSION 0.1\n")
    print("*** MENU ***\n")
    print("""
Please make your choice:\n
A: Display Teams
B: Quit\n
Enter 'HELP' for more info.
        """)

def show_submenu():
    print("The Teams of the season are:\n")

    for index, team in enumerate(constants.TEAMS):
        #the 1 is an optional argument where enumerate starts so it's not zero-index
        print(chr(index+65) + "  " f'{team}')
        #using the chr() with thanks to https://www.geeksforgeeks.org/chr-in-python/#:~:text=The%20chr()%20method%20returns,code%20point%20is%20an%20integer.&text=The%20chr()%20method%20takes,point%20is%20num%2C%20an%20integer.





    print("\nPlease make a choice which team you'd like more info on.")


#def show_team():


def show_help():
    print("""
This Tool is created to provide an overview of the teams\n
By providing "A" as input you'll go into the team submenu
By providing "B" as input you'll quit the application
""")
    user_input()


def user_input():
    while True:
        user_choice = input("Enter an option:    ")
        try:
            if user_choice.lower() == 'help':
                show_help()
                continue

            elif user_choice.lower() == 'a':
                show_submenu()

            elif user_choice.lower() == 'b':
                print('Thank you for trying out the application')
                break
            else:
                raise ValueError
                continue
        except:
            print("""
    Oh no! It seems you filled in something other than 'A', 'B' or 'HELP'.\n
    Please try again.
                """)

show_menu()
user_input()



#create an application that gives an overview option to:
#    Check the current team stats
#        Show the current teams
#        Loop back to start of application
#    Quit


#create 3 empty team lists
#Panthers
#Bandits
#Warriors

#create function to:
#    read the player data while not changing it
#    store it to a new collection with
#        height set as an integer
#        experience set as a boolean

#create a balance_teams function to:
#    fill the 3 teams with an equal amount of players
#        ensure that each team has equal experienced and inexperienced
#    print out the 3 different teams in a readable manner
#        include team's name as a string
#        total players on that team
#            divided by experienced & inexperienced
#        the player names as strings separated by commas
#            (not as a list object but as a flattened string)
#        the guardians of these players
#            (when a player has 2 guardians it should be "name and name")
#        display the average height of the team
