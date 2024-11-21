class IdGenerator:
    def __init__(self, id: int = 0):
        self.id = id

    def generate(self):
        self.id = self.id + 1
        return self.id
