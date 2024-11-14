import pyodbc

class Database:
    def __init__(self, driver, server, port, database, user, password):
        self.driver = driver
        self.server = server
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            connection_string = (
                f"Driver={{{self.driver}}};"
                f"Server={self.server};Port={self.port};"
                f"Database={self.database};"
                f"Uid={self.user};"
                f"Pwd={self.password};"
            )
            self.connection = pyodbc.connect(connection_string)
            self.cursor = self.connection.cursor()
            print("Connection successful!")
        except pyodbc.Error as e:
            print(f"Error connecting to the database: {e}")
            self.connection = None
            self.cursor = None

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed.")

    def get_cursor(self):
        if self.cursor:
            return self.cursor
        else:
            print("Error: No active connection.")
            return None