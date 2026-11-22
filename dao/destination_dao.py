from dao.conexion import DatabaseConnection
from models.destination import Destination


class DestinationDAO:
    def __init__(self, db: DatabaseConnection | None = None):
        self.db = db if db is not None else DatabaseConnection()

    def create(self, destination: Destination) -> int:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO Destinations (name, location, description, base_price)
                VALUES (?, ?, ?, ?)
                """,
                (
                    destination.name,
                    destination.location,
                    destination.description,
                    destination.base_price,
                ),
            )
            conn.commit()
            return cursor.lastrowid
        finally:
            self.db.close()

    def get_by_id(self, destinations_id: int) -> dict | None:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM Destinations WHERE destinations_id = ?",
                (destinations_id,),
            )
            row = cursor.fetchone()
            return dict(row) if row else None
        finally:
            self.db.close()

    def get_all(self) -> list[dict]:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Destinations")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        finally:
            self.db.close()

    def update(self, destination: Destination) -> bool:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE Destinations
                SET name = ?, location = ?, description = ?, base_price = ?
                WHERE destinations_id = ?
                """,
                (
                    destination.name,
                    destination.location,
                    destination.description,
                    destination.base_price,
                    destination.destinations_id,
                ),
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            self.db.close()

    def delete(self, destinations_id: int) -> bool:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Destinations WHERE destinations_id = ?",
                (destinations_id,),
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            self.db.close()