class Destination:
    def __init__(
        self,
        destinations_id: int,
        name: str,
        location: str,
        base_price: float,
        description: str | None = None,
    ):
        self.destinations_id = destinations_id
        self.name = name
        self.location = location
        self.base_price = base_price
        self.description = description

    def __str__(self) -> str:
        return f"Destination({self.destinations_id}, {self.name}, {self.location})"