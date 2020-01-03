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

def print_error_msg(message):
    '''
    Przedstawia użytkownikowi komunikat błędu. Parametr: Message (str).
    '''
    print(message)

