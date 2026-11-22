from dao.booking_dao import BookingDAO
from dao.customer_dao import CustomerDAO
from dao.destination_dao import DestinationDAO
from dao.package_dao import PackageDAO
from models.booking import Booking
from models.customer import Customer
from models.destination import Destination
from models.package import Package


def main():
    customer_dao = CustomerDAO()
    destination_dao = DestinationDAO()
    package_dao = PackageDAO()
    booking_dao = BookingDAO()

    # 1. Crear un cliente
    customer = Customer(
        None,
        "Valentina Rojas",
        "valentina@ejemplo.com",
        "clave123",
    )
    customer_id = customer_dao.create(customer)
    print(f"Cliente creado con ID: {customer_id}")

    # 2. Crear un destino
    destination = Destination(
        None,
        "Valle del Elqui",
        "Coquimbo",
        "Cielos despejados y viñedos",
        65000,
    )
    destination_id = destination_dao.create(destination)
    print(f"Destino creado con ID: {destination_id}")

    # 3. Crear un paquete
    package = Package(
        None,
        "Escape al Elqui",
        "2026-12-05",
        "2026-12-08",
        195000,
    )
    package_id = package_dao.create(package)
    print(f"Paquete creado con ID: {package_id}")

    # 4. Crear una reserva vinculando cliente y paquete
    booking = Booking(
        None,
        customer_id,
        package_id,
        "2026-11-22",
        "Confirmada",
        195000,
    )
    booking_id = booking_dao.create(booking)
    print(f"Reserva creada con ID: {booking_id}")

    # 5. Consultar registros
    print("\n--- Todos los clientes ---")
    print(customer_dao.get_all())

    print("\n--- Todas las reservas ---")
    print(booking_dao.get_all())


if __name__ == "__main__":
    main()