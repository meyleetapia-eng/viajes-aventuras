from dao.conexion import DatabaseConnection
from models.booking import Booking
from models.customer import Customer
from models.destination import Destination
from models.package import Package


def main():
    client = Customer(
        customer_id=1,
        name="Camila Soto",
        email="camila@example.com",
        password="secret_password",
        phone="+56987654321",
    )

    destination = Destination(
        destinations_id=1,
        name="Valle de Elqui",
        location="Coquimbo, Chile",
        base_price=85000.0,
        description="Tour astronómico y viñedos",
    )

    package = Package(
        package_id=1,
        name="Escapada Norte Chico",
        start_date="2026-12-10",
        end_date="2026-12-13",
        total_cost=190000.0,
    )

    booking = Booking(
        bookings_id=1,
        customer_id=client.customer_id,
        package_id=package.package_id,
        bookings_date="2026-11-22",
        status="Confirmed",
        amount_paid=190000.0,
    )

    print("Modelos de Viajes Aventura cargados correctamente:")
    print(client)
    print(destination)
    print(package)
    print(booking)

    db = DatabaseConnection()
    db.connect()


if __name__ == "__main__":
    main()