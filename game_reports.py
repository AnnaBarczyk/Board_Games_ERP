# Główne funkcje programu
import file_handling
import ui

def add_new_game(games_list_of_lists):
    '''
    Dodaje nową grę na końcu listy list i zapisuje do pliku.
    '''
    title = "Please, enter informations to add game to the list."
    labels = ["Name", "Publisher", "Publish date", "Minimal amount of players", "Maximum amount of players", "Type", "Notes"]
    new_data = ui.get_input(title, labels)
    games_list_of_lists.append(new_data)
    file_handling.export_file(games_list_of_lists, filename="games.csv", mode="w")

def remove_game_by_title(games_list_of_lists):
    '''
    Usuwa grę na podstawie podanego przez użytkownika tytułu z listy gier.
    '''
    title = "Please, enter name of the game you want to remove."
    labels = ["Name"]
    new_data = ui.get_input(title, labels)
    first_answear_in_list = 0
    title_to_remove = new_data[first_answear_in_list]
    
    for game in games_list_of_lists:
        if title_to_remove in game:
            games_list_of_lists.remove(game)
            file_handling.export_file(games_list_of_lists, filename="games.csv", mode="w")
            break
        else:
            ui.print_error_msg("Sorry, no such game in list")

    
def update_game_by_title(games_list_of_lists):
    '''
    Aktualizuje cały wpis na podstawie podanego przez użytkownika tytułu z listy gier.
    '''
    title = "Please, enter informations to update game informations."
    labels = ["Name of the game to update","Name", "Publisher", "Publish date", "Minimal amount of players", "Maximum amount of players", "Time", "Type", "Notes"]
    inputs = ui.get_input(title, labels)
    game_to_update = inputs[0]
    new_informations = inputs[1:]
    counter = 0

    if game_to_update in games_list_of_lists:
        for game in games_list_of_lists:
            if game_to_update == game[0]:
                break
            else:
                counter += 1
    else:
        ui.print_error_msg("Sorry, no such game!")

    games_list_of_lists[counter] = new_informations
    file_handling.export_file(games_list_of_lists, filename="games.csv", mode="w")