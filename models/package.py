class Package:
    def __init__(
        self,
        package_id: int,
        name: str,
        start_date: str,
        end_date: str,
        total_cost: float,
    ):
        self.package_id = package_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = total_cost

    def __str__(self) -> str:
        return f"Package({self.package_id}, {self.name}, ${self.total_cost})"