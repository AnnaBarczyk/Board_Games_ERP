# Interface programu 


def print_menu(title, commands):
    '''
    Przedstawia menu przyjazne dla użytkownika. Paramtery: commands (list), title (str).
    '''
    index_change = 1
    print(title)
    for key,value in enumerate(commands):
        print(f"{key + index_change}.{value}")
        

def print_table(games_list_of_lists):
    '''
    Przedstawia listę list jako tabelę. Parametr: games (list of lists).
    '''
    for game in games_list_of_lists:
        print(','.join(game))

def print_result(result):
    print(','.join(result))

def get_input(title, labels):
    '''
    Pobiera informacje od użytkownika i przekazuje do programu jako listę. 
    Parametry: title (str), labels (list). Zwraca listę odpowiedzi.
    '''
    print(title)
    inputs = []
    for label in labels:
        new_data = input(f"Please, enter{label}: ")
        inputs.append(new_data)
    return inputs
    

def menu_handling(first_option_number, last_option_number):
    while True:
        try:
            user_input = get_input("Select an option", [" option number. "])
            first_answear_in_list = 0
            chosen_option = int(user_input[first_answear_in_list])
            if chosen_option >= int(first_option_number) and chosen_option <= int(last_option_number):
                return chosen_option
            else:
                print_error_msg("Sorry, no such option!")
        except ValueError or TypeError:
            print_error_msg("This is not a number!")

def print_error_msg(message):
    '''
    Przedstawia użytkownikowi komunikat błędu. Parametr: Message (str).
    '''
    print(message)

