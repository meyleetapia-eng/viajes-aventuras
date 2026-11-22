from dao.conexion import DatabaseConnection
from models.customer import Customer


class CustomerDAO:
    def __init__(self, db: DatabaseConnection | None = None):
        self.db = db if db is not None else DatabaseConnection()

    def create(self, customer: Customer) -> int:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO Customers (name, email, password)
                VALUES (?, ?, ?)
                """,
                (customer.name, customer.email, customer.password),
            )
            conn.commit()
            return cursor.lastrowid
        finally:
            self.db.close()

    def get_by_id(self, customer_id: int) -> dict | None:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM Customers WHERE customer_id = ?",
                (customer_id,),
            )
            row = cursor.fetchone()
            return dict(row) if row else None
        finally:
            self.db.close()

    def get_all(self) -> list[dict]:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customers")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        finally:
            self.db.close()

    def update(self, customer: Customer) -> bool:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE Customers
                SET name = ?, email = ?, password = ?
                WHERE customer_id = ?
                """,
                (customer.name, customer.email, customer.password, customer.customer_id),
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            self.db.close()

    def delete(self, customer_id: int) -> bool:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Customers WHERE customer_id = ?",
                (customer_id,),
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            self.db.close()