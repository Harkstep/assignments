class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print('woof')

    def run(self):
        print('run' + self.name)


class Bulldog(Dog):
    def __init__(self, name, breed):
        super().__init__(name.strip(), breed.strip())

    def bark(self):
        print('wooo')

    def breed(self):
        print('Bulldog')

    def run(self):
        super().run()