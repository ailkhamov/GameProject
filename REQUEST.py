import requests



def take_game(game):
    response_game = requests.get('https://api.rawg.io/api/games/' + game)
    print(type(response_game))
    retrieve_data = response_game.json()

    # print(type(retrieve_data))
    game_name = retrieve_data['name']
    # game_rating = retrieve_data['rating']
    # game_website = retrieve_data['website']
    # game_description = retrieve_data['description_raw']
    return str(game_name)

def take_rating(game):
    response_game = requests.get('https://api.rawg.io/api/games/' + game)
    retrieve_data = response_game.json()
    game_rating = retrieve_data['rating']
    return str(game_rating)

def take_description(game):
    response_game = requests.get('https://api.rawg.io/api/games/' + game)
    retrieve_data = response_game.json()
    game_description = retrieve_data['description_raw']
    return str(game_description)

def take_website(game):
    response_game = requests.get('https://api.rawg.io/api/games/' + game)
    retrieve_data = response_game.json()
    take_website = retrieve_data['website']
    return str(take_website)







def write_to_file(file,postcode):
    try:
        with open(file, 'a') as opened_file:
            opened_file.write(postcode + '\n')
    except FileNotFoundError:
        print("File not found")

    return print(opened_file)

game_name = str(take_game("grand-theft-auto-v"))
print(game_name)

write_to_file('postcode.txt',game_name)

