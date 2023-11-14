class Group:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
    
    def __str__(self) -> str:
        return self.name