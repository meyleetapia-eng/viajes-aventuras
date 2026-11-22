import sqlite3
from pathlib import Path


class DatabaseConnection:
    def __init__(self, db_path: str | None = None):
        if db_path is None:
            base_dir = Path(__file__).resolve().parent.parent
            db_dir = base_dir / "database"
            db_dir.mkdir(parents=True, exist_ok=True)
            db_path = str(db_dir / "viaje_aventura.db")
        self.db_path = db_path
        self.connection: sqlite3.Connection | None = None

    def connect(self) -> sqlite3.Connection:
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row
            self.connection.execute("PRAGMA foreign_keys = ON;")
        return self.connection

    def close(self) -> None:
        if self.connection is not None:
            self.connection.close()
            self.connection = None