class Bird:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def fly(self):
        pass


class Pigeon(Bird):
    def __init__(self, name):
        super().__init__(name, species="Pigeon")

    def fly(self):
        return "I am flying like a pigeon!"



class Eagle(Bird):
    def __init__(self, name):
        super().__init__(name, species="Eagle")

    def fly(self):
        return "I am flying like an eagle!"


class Ostrich(Bird):
    def __init__(self, name):
        super().__init__(name, species="Ostrich")

    def fly(self):
        return "I cannot fly, I am an ostrich.".
