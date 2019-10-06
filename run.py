from DatabaseConnection import *
from Game import *
from GameRequest import *

server = 'localhost,1433'
database = 'Games'
username = 'SA'
password = 'Passw0rd2018'

db_now = Game(server,database,username,password)


game_name = GameReguest.take_game('grand-theft-auto-v')
game_name_new = "'" + game_name + "'"
print(game_name)

game1 = 'grand-theft-auto-v'
print(game1)

db_now.createGame(3,game_name_new,"'2'","'Test'","'Test2'")
