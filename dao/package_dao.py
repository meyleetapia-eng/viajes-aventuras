from dao.conexion import DatabaseConnection
from models.package import Package


class PackageDAO:
    def __init__(self, db: DatabaseConnection | None = None):
        self.db = db if db is not None else DatabaseConnection()

    def create(self, package: Package) -> int:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO Packages (name, start_date, end_date, total_cost)
                VALUES (?, ?, ?, ?)
                """,
                (
                    package.name,
                    package.start_date,
                    package.end_date,
                    package.total_cost,
                ),
            )
            conn.commit()
            return cursor.lastrowid
        finally:
            self.db.close()

    def get_by_id(self, package_id: int) -> dict | None:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM Packages WHERE package_id = ?",
                (package_id,),
            )
            row = cursor.fetchone()
            return dict(row) if row else None
        finally:
            self.db.close()

    def get_all(self) -> list[dict]:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Packages")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        finally:
            self.db.close()

    def update(self, package: Package) -> bool:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE Packages
                SET name = ?, start_date = ?, end_date = ?, total_cost = ?
                WHERE package_id = ?
                """,
                (
                    package.name,
                    package.start_date,
                    package.end_date,
                    package.total_cost,
                    package.package_id,
                ),
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            self.db.close()

    def delete(self, package_id: int) -> bool:
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Packages WHERE package_id = ?",
                (package_id,),
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            self.db.close()