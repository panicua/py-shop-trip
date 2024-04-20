from dataclasses import dataclass


@dataclass
class Shop:
    name: str = None
    location: list[int] = None
    products: dict[str:float] = None
