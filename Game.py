from DatabaseConnection import *
import requests

class Game(ConnectMicrosoftServer):

    def print_all_games(self):
        query_rows = self.filter_query(f'SELECT * From dbo.GamesData')
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(
                f'Game ID: {record[0]}, Game Name:{record[1]}, Game Rating: {record[2]}, Game Website: {record[3]}, Game Description: {record[4]}')

    def readOneGame(self, id):
        query_rows = self.filter_query(f'SELECT * From dbo.GamesData WHERE game_id = {id}')
        record = query_rows.fetchone()
        print(f'Game ID: {record[0]}, Game Name:{record[1]}, Game Rating: {record[2]}, Game Website: {record[3]}, Game Description : {record[4]}')


    def createGame(self, id,name,rating,website,description):
        query_rows = self.filter_query(f' INSERT INTO dbo.GamesData(game_id,game_name,rating,website,description) VALUES({id},{name},{rating},{website},{description})')
        self.conn_db.commit()

    def deleteRecord(self, id):
        query_rows = self.filter_query(f' DELETE FROM dbo.GamesData WHERE game_id = {id}')
        self.conn_db.commit()







