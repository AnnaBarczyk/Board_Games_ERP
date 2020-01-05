# Funkcje podmenu wyszukiwania
import ui
import file_handling
import main_program
import os

def start_searching_functions():
    title = "Searching menu"
    commands = ["Search for games by number of players", "Search by title", "Search by type", "Back to main menu"]
    games_list_of_lists = file_handling.import_file(filename="games.csv")
    ui.print_menu(title, commands)
    chosen_option = ui.menu_handling(1,4)

    while True:
        if chosen_option == 1: # Wyszukuje gry dla określonej liczby graczy
            os.system("clear")
            number = ui.get_input("Search for games for how many peaople?", ["Enter number of playing people"])
            results = search_for_games_by_number_of_players(games_list_of_lists, number)
            ui.print_table(results)
            start_searching_functions()
        elif chosen_option == 2: # Wyszukuje grę na podstawie tytułu
            os.system("clear")
            search_by_title(games_list_of_lists)
            start_searching_functions()
        elif chosen_option == 3: # Wyszukuje grę danego typu
            os.system("clear")
            search_by_type(games_list_of_lists)
            start_searching_functions()
        elif chosen_option == 4: # Powrót do głównego menu
            main_program.main()


def search_for_games_by_number_of_players(games_list_of_lists, number_of_plr):
    '''
    Wyszykuje i przedstawia tylko gry dla określonej liczby graczy.
    '''
    list_of_game_for_number_of_plr = []
    minimum_players_column = 3
    maximum_players_column = 4
    number_to_look = int(number_of_plr[0])

    for game in games_list_of_lists:
        if number_to_look >= int(game[minimum_players_column]) and number_to_look <= int(game[maximum_players_column]):
            list_of_game_for_number_of_plr.append(game)
    return list_of_game_for_number_of_plr

def search_by_title(games_list_of_lists):
    '''
    Wyszykuje wpis dla określonego tytułu.
    '''
    inputs = ui.get_input("Search by title", ["Enter title to search"])
    title = inputs[0]
    result = []

    for game in games_list_of_lists:
        if game[0] == title:
            result.append(game)

    if len(result)<1:
        ui.print_error_msg("Sorry, no such title!")
    else:
        ui.print_table(result)

def search_by_type(games_list_of_lists):
    '''
    Wyszykuje i przedstawia gry określonego typu.
    '''
    inputs = ui.get_input("Search by type", ["Enter type to search"])
    type_of_game = inputs[0]
    result = []

    for game in games_list_of_lists:
        if game[5] == type_of_game:
            result.append(game)

    if len(result)<1:
        ui.print_error_msg("Sorry, no such type!")
    else:
        ui.print_table(result)