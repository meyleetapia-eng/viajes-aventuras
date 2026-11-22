from dao.conexion import DatabaseConnection
from models.booking import Booking


class BookingDAO:
    def __init__(self, db: DatabaseConnection | None = None):
        self.db = db if db is not None else DatabaseConnection()

    def create(self, booking: Booking) -> int:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO Bookings (
                    customer_id,
                    package_id,
                    bookings_date,
                    status,
                    amount_paid
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    booking.customer_id,
                    booking.package_id,
                    booking.bookings_date,
                    booking.status,
                    booking.amount_paid,
                ),
            )
            conn.commit()
            return cursor.lastrowid
        finally:
            self.db.close()

    def get_by_id(self, bookings_id: int) -> dict | None:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM Bookings WHERE bookings_id = ?",
                (bookings_id,),
            )
            row = cursor.fetchone()
            return dict(row) if row else None
        finally:
            self.db.close()

    def get_all(self) -> list[dict]:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Bookings")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        finally:
            self.db.close()

    def update(self, booking: Booking) -> bool:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE Bookings
                SET customer_id = ?,
                    package_id = ?,
                    bookings_date = ?,
                    status = ?,
                    amount_paid = ?
                WHERE bookings_id = ?
                """,
                (
                    booking.customer_id,
                    booking.package_id,
                    booking.bookings_date,
                    booking.status,
                    booking.amount_paid,
                    booking.bookings_id,
                ),
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            self.db.close()

    def delete(self, bookings_id: int) -> bool:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Bookings WHERE bookings_id = ?",
                (bookings_id,),
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            self.db.close()