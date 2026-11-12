from abc import ABC

class Item(ABC):
    Name: str

    def __init__(self):
        self.Name = "Unnamed Item"