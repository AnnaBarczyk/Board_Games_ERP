# Główna część programu wykorzystująca pozostałe funkcje. Za pomocą tego liku włączam program.
import ui
import file_handling
import game_reports
import searching_functions

def main_menu_handling():
    while True:
        try:
            user_input = ui.get_input("Select an option", [" option number. "])
            first_answear_in_list = 0
            chosen_option = int(user_input[first_answear_in_list])
            if chosen_option > 0 and chosen_option < 9:
                return chosen_option
            else:
                ui.print_error_msg("Sorry, no such option!")
        except ValueError or TypeError:
            ui.print_error_msg("This is not a number!")
    

def main():
    main_menu_commands = ["Show games list","Add game", "Remove game", "Update game","Searching functions menu", "Statistic functions menu", "Sorting functions menu", "Exit"]
    games_list_of_lists = file_handling.import_file(filename="games.csv")
    

    ui.print_menu("Main menu", main_menu_commands)
    chosen_option = main_menu_handling()
    while True:
        if chosen_option == 1: #Pokazuje aktualną listę
            ui.print_table(games_list_of_lists)
            main()
        elif chosen_option == 2: # Dodaje nową grę do listy
            game_reports.add_new_game(games_list_of_lists)
            main()
        elif chosen_option == 3: # Usuwa grę z listy
            game_reports.remove_game_by_title(games_list_of_lists)
            main()
        elif chosen_option == 4: # Aktualizuje grę na liście
            game_reports.update_game_by_title(games_list_of_lists)
            main()
        elif chosen_option == 5: # Menu wyszukiwania
            searching_functions.start_searching_functions()
        elif chosen_option == 6:
            pass
        elif chosen_option == 7:
            pass
        elif chosen_option == 8:
            exit()


if __name__ == '__main__':
    main()