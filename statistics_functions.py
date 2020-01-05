# Funkcje podmenu statystyk

import os
import ui
import main_program
import file_handling


def start_statistics_functions():
    title = "Statistics menu"
    commands = ["Count average game time", "Most common type", "Shortest game", "Longest game of type"]
    games_list_of_lists = file_handling.import_file(filename="games.csv")
    ui.print_menu(title, commands)
    chosen_option = ui.menu_handling(1,5)

    while True:
        if chosen_option == 1: # Podlicza średni czas rozgrywki wszystkich gier
            os.system("clear")
            average_game_time(games_list_of_lists)
            start_statistics_functions()
        elif chosen_option == 2: # Pokazuje najczęściej występujący typ
            os.system("clear")
            most_common_type(games_list_of_lists)
            start_statistics_functions()
        elif chosen_option == 3: # Pokazuje najkrótszą grę
            os.system("clear")
            shortest_game(games_list_of_lists)
            start_statistics_functions()
        elif chosen_option == 4: # Pokazuje najdłuższą grę danego typu
            os.system("clear")
            longest_game_of_type(games_list_of_lists)
            start_statistics_functions()
        elif chosen_option == 5: # Powrót do głównego menu
            main_program.main()

def average_game_time(games_list_of_lists):
    '''
    Oblicza i pokazuje średnią długość rozgrywki dla wszystkich gier.
    '''
    time_list = []
    whole_time = 0

    for game in games_list_of_lists:
        try:
            time_list.append(int(game[6]))
        except TypeError or ValueError:
            continue
    for time in time_list:
        whole_time = time + whole_time

    average_time = whole_time / len(time_list)
    ui.print_answear(f"The average game time in minutes: {average_time}.")


    
def most_common_type(games_list_of_lists):
    '''
    Oblicza i pokazuje najczęściej występujący typ gier oraz ich ilość.
    '''
    types_of_games = []
    counted_types = []
    

    for game in games_list_of_lists:
        type_column = game[5]
        if type_column not in types_of_games:
            types_of_games.append(type_column)
    
    for type_of_game in types_of_games:
        counter = 0
        for game in games_list_of_lists:
            type_column = game[5]
            if type_of_game == type_column == game[5]:
                counter += 1
        counted_types.append([type_of_game,counter])

    max_type = 0
    most_common_types = []

    for counted_type in counted_types:
        if counted_type[1] > max_type:
            max_type = counted_type[1]

    for counted_type in counted_types:
        if max_type == counted_type[1] :
            most_common_types.append(counted_type)

    ui.print_answear(f"Most common types: {most_common_types}")



def shortest_game(games_list_of_lists):
    '''
    Pokazuje grę z najmniejszym czasem rozgrywki (lub kilka jeśli mają ten sam czas)
    '''
    a_lot_of_time = 10000
    min_time = a_lot_of_time
    shortest_games = []

    for game in games_list_of_lists:
        time_column = int(game[6])
        if time_column < min_time:
            min_time = time_column

    for game in games_list_of_lists:
        time_column = int(game[6])
        if time_column == min_time:
            shortest_games.append(game)

    ui.print_table(shortest_games)


def longest_game_of_type(games_list_of_lists):
    '''
    Pokazuje najdłuższą grę konkretnego typu podanego przez użytkownika(lub kilka jeśli mają ten sam czas).
    '''
    max_time = 0
    longest_games = []
    games_of_wanted_type = []
    inputs = ui.get_input("Longest game of a specific type", ["Enter type: "])
    type_to_search = inputs[0]

    for game in games_list_of_lists:
        type_column = game[5]
        if type_column == type_to_search:
            games_of_wanted_type.append(game)
        
    for game in games_of_wanted_type:
        time_column = int(game[6])
        if time_column > max_time:
            max_time = time_column

    for game in games_of_wanted_type:
        time_column = int(game[6])
        if time_column == max_time :
            longest_games.append(game)

    ui.print_table(longest_games)

### Opcjonanie
#def show_games_with_notes():
#'''
#Pokazuje tylko gry z notatkami.
#'''

#def most_common_phrases():
#'''
#Pokazuje 10 najpopularniejszych wyszukiwań wraz z liczbami.
#'''