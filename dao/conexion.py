class DatabaseConnection:
    def __init__(self, db_path: str = "database/viajes_aventura.db"):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        # Aquí se conectará el motor elegido (sqlite3, oracledb, mysql.connector, etc.)
        print(f"Preparando conexión a: {self.db_path}")
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            print("Conexión cerrada.")