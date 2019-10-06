import pyodbc

# Concept of 'Strong Params'
    # never EVER, Trust user Input
    # Avoid SQL injections
    # Filter for SQL Injections

class ConnectMicrosoftServer():
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE='+ self.database +';UID='
                                      +self.username+';PWD='+ self.password)
        self.cursor = self.conn_db.cursor()

    def filter_query(self, query):
        # Doing some filtering for some bad queries
        return self.cursor.execute(query)

    def sql_query(self, query):
        return self.filter_query(query)