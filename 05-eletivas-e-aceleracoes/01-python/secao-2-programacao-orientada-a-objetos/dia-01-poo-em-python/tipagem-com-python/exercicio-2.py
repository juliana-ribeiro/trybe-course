"""
Modifique o código abaixo para que ele seja tipado corretamente.
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height """


class Person:
    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self.age = age
        self.height = height
