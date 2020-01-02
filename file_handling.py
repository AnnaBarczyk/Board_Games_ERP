# Obsługa plików

def import_file(filename="games.csv"):
    '''
    Importowanie danych z pliku .csv, zwracanie listy list. Parametr: nazwa pliku.
    Docelowy format:
    [['Dixit', ' Rebel', ' 2010', ' 3', ' 6', ' imprezowa', ' 30', ' brak'], 
    ['List Miłosny', ' 2013', ' 2', ' 5', ' imprezowa', ' 20', ' brak'], 
    ['Pentago', ' Egmont', ' 2017', ' 2', ' 2', ' logiczna', ' 15', ' brak']]
    '''
    games_list_of_lists = []

    with open(filename, "r") as file:
        for line in file.readlines():
            games_list_of_lists.append(line.strip().split(';'))
    return games_list_of_lists


def export_file(games, filename="games.scv", mode="a"):
    '''
    Exortowanie danych do pliku .csv, zwracanie listy list. 
    Parametry: lista nowych gier (z game reports), nazwa pliku docelowego, 
    tryb zapisu "a" dodaje wpisy, tryb "w" nadpisuje plik .
    '''

## Opcjonalnie

# def export_results_to_new_file():