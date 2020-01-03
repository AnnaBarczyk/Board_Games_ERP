# Obsługa plików

import ui

def import_file(filename="games.csv"):
    '''
    Importowanie danych z pliku .csv, zwracanie listy list. Parametr: nazwa pliku.
    Docelowy format:
    [['Dixit', 'Rebel', '2010', '3', '6', 'imprezowa', '30', 'brak'], 
    ['List Miłosny', '2013', '2', '5', 'imprezowa', '20', 'brak']]
    '''

    games_list_of_lists = []

    with open(filename, "r") as file:
        for line in file.readlines():
            games_list_of_lists.append(line.strip().split(';'))
    return games_list_of_lists


def export_file(games_list_of_lists, filename="games.scv", mode="a"):
    '''
    Exortowanie danych do pliku .csv, zwracanie listy list. 
    Parametry: lista nowych gier (z game reports), nazwa pliku docelowego, 
    tryb zapisu "a" dodaje wpisy, tryb "w" nadpisuje plik .
    '''
    if mode not in ['a','w']:
        ui.print_error_msg('Wrong write mode')
    with open(filename, mode) as file:
        for line in games_list_of_lists:
            file.write(';'.join(line) + '\r\n')

## Opcjonalnie

# def export_results_to_new_file(result, filename):
#    with open(filename, "w") as file:
#        for line in result:
#            file.write(';'.join(line) + '\r\n')