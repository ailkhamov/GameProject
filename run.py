from DatabaseConnection import *
from Game import *
from GameRequest import *

server = 'localhost,1433'
database = 'Games'
username = 'SA'
password = 'Passw0rd2018'

db_now = Game(server,database,username,password)



print("Welcome to the Game Database")
print("Choose one of the following options")
print("Option 1 - Create A Game and Save it to Our Database")
print("Option 2 - Get One Game from the database")
print("Option 3 - Get All Games from the database")
print("Option 4 - Destroy a Game from a database")
print("Option 5 - Export a Receipe to a Text File")

choice = int(input("Please enter your choice: "))
total_credit = 100
while True:
    if choice == 1:
        id_number = int(input("Enter id number for your game: "))
        game_now = input("Which game would you like to add to the database?: ")
        game_name = GameReguest.take_game(game_now)
        game_rating = GameReguest.take_rating(game_now)
        game_website = GameReguest.take_website(game_now)
        game_description = GameReguest.take_description(game_now)

        game_name_new = "'" + game_name + "'"
        game_rating_new = "'" + game_rating + "'"
        game_website_new = "'" + game_website + "'"
        game_description = "'" + game_description + "'"

        db_now.createGame(id_number,game_name_new,game_rating_new,game_website_new,game_description)
        print("That's all been saved for you!")
        db_now.readOneGame(id_number)
        choice = int(input("Enter your choice again or type 9 to exit: "))
    elif choice == 2:
        id_number = int(input("Enter the id number of the Game you wish to see: "))
        game = db_now.readOneGame(id_number)
        print(game)
        choice = int(input("Enter your choice again or type 9 to exit: "))
    elif choice == 3:
         db_now.print_all_games()
         choice = int(input("Enter your choice again or type 9 to exit: "))
         if choice == 9:
             print("Enjoy the rest of your day! Goodbye for now!")
             break
    elif choice == 4:
        id_number = int(input("Enter the id number of game you wish to delete: "))
        db_now.deleteRecord(id_number)
        db_now.print_all_games()
        print("That's all been deleted for you!")
        choice = int(input("Enter your choice again or type 9 to exit: "))
        if choice == 9:
            print("Enjoy the rest of your day! Goodbye for now!")
            break
    elif choice ==5:
        game_choice = input("Enter the game you wish to write to text file")
        game_name = str(GameReguest.take_wholeGame(game_choice))

        GameReguest.write_to_file('game.txt',game_name)
    # elif choice ==5:
    #      id_number = int(input("Enter the id number of game you wish to buy: "))
    #      post_code = db_now.readOneGame(id_number)
    #
    else:
        print("You have entered the wrong number!")




