class Customer:
    def __init__(
        self,
        customer_id: int,
        name: str,
        email: str,
        password: str,
        phone: str | None = None,
    ):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    def __str__(self) -> str:
        return f"Customer({self.customer_id}, {self.name}, {self.email})"