class Booking:
    def __init__(
        self,
        bookings_id: int,
        customer_id: int,
        package_id: int,
        bookings_date: str,
        status: str,
        amount_paid: float,
    ):
        self.bookings_id = bookings_id
        self.customer_id = customer_id
        self.package_id = package_id
        self.bookings_date = bookings_date
        self.status = status
        self.amount_paid = amount_paid

    def __str__(self) -> str:
        return f"Booking({self.bookings_id}, Customer={self.customer_id}, Package={self.package_id}, {self.status})"