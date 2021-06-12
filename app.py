import constants
import copy
import time


def show_menu():
    print("*** MENU ***")
    print("""
Please make your choice:\n
A: Display Teams
B: Quit\n
Enter 'HELP' for more info.
        """)

def show_submenu():
    print("The Teams of the season are:\n")

    for index, team in enumerate(constants.TEAMS):
        print(chr(index+65) + "  " f'{team}')
        #using the chr() with thanks to https://www.geeksforgeeks.org/chr-in-python/#:~:text=The%20chr()%20method%20returns,code%20point%20is%20an%20integer.&text=The%20chr()%20method%20takes,point%20is%20num%2C%20an%20integer.

    print("\nPlease make a choice which team you'd like more info on.")
    team_selection()


def team_selection():
    while True:
        team_choice = input("Enter your team choice:    ")
        try:
            if team_choice.lower() == 'a' or team_choice.lower() == constants.TEAMS[0].lower():
                print("\n---TEAM PANTHERS STATISTICS---\n")
                show_team_statistics(team_panthers)
                time.sleep(3)
                show_menu()
                user_input()
                break


            elif team_choice.lower() == 'b' or team_choice.lower() == constants.TEAMS[1].lower():
                print("\n---TEAM BANDITS STATISTICS---\n")
                show_team_statistics(team_bandits)
                time.sleep(3)
                show_menu()
                user_input()
                break

            elif team_choice.lower() == 'c' or team_choice.lower() == constants.TEAMS[2].lower():
                print("\n---TEAM WARRIORS STATISTICS---\n")
                show_team_statistics(team_warriors)
                time.sleep(3)
                show_menu()
                user_input()
                break

            else:
                raise ValueError
                continue
        except:
            print("""
    Oh no! It seems you filled in something other than the team name or 'A', 'B', 'C'.\n
    Please try again.
                """)


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
                break

            elif user_choice.lower() == 'b' or user_choice.lower() == 'quit':
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


def clean_data(players_copy):
    index = 0
    for player in players_copy:
        players_copy[index]['height'] = int(players_copy[index]['height'][0:2])
        players_copy[index]['guardians'] = players_copy[index]['guardians'].split(' and ')
        if players_copy[index]['experience'].lower() == "yes":
            players_copy[index]['experience'] = True
        else:
            players_copy[index]['experience'] = False
        index += 1

    return players_copy


def balance_teams(players):
    for player in players:
        if player['experience'] == True:
            if len(team_panthers) == len(team_bandits):
                team_panthers.append(player)
            elif len(team_warriors) < len(team_panthers):
                team_warriors.append(player)
            else:
                team_bandits.append(player)
    for player in players:
        if player['experience'] == False:
            if len(team_panthers) == len(team_bandits):
                team_panthers.append(player)
            elif len(team_warriors) < len(team_panthers):
                team_warriors.append(player)
            else:
                team_bandits.append(player)


def average_height(team):
    team_average_height = sum([player['height'] for player in team]) / len(team)
    return team_average_height


def number_of_experienced_players(team):
    #https://www.kite.com/python/answers/how-to-count-the-number-of-true-booleans-in-a-list-in-python#:~:text=Use%20sum()%20to%20count,True%20booleans%20in%20the%20list.
    team_number_of_experienced_players = sum(player['experience'] == True for player in team)
    return team_number_of_experienced_players


def number_of_inexperienced_players(team):
    team_number_of_inexperienced_players = sum(player['experience'] == False for player in team)
    return team_number_of_inexperienced_players


def names(team):
    team_names = [player['name'] for player in team]
    print(", ".join(team_names))


def guardians(team):
    team_guardians_list = [player['guardians'] for player in team]
    #https://careerkarma.com/blog/python-flatten-list/
    team_guardians_flattened = [guardian for guardians in team_guardians_list for guardian in guardians]
    print(", ".join(team_guardians_flattened))


def show_team_statistics(team):
    print("The players in the team are:\n")
    names(team)
    print()
    print("Total players: {}".format(number_of_experienced_players(team)+number_of_inexperienced_players(team)))
    print("---------------------------------")
    print("{} experienced players".format(number_of_experienced_players(team)))
    print("{} inexperienced players".format(number_of_inexperienced_players(team)))
    print("The team average height is {}.".format(average_height(team)))
    print("\nThe guardians for the team are:\n")
    guardians(team)
    print()



team_panthers = []
team_bandits = []
team_warriors = []

if __name__ == '__main__':
    players_copy = copy.deepcopy(constants.PLAYERS)
    clean_data(players_copy)
    balance_teams(players_copy)
    print("THE BASKETBALL TEAM CREATOR TOOL")
    print("VERSION 0.3\n")
    show_menu()
    user_input()
