""" Com base na classe Car do exercício anterior,
crie um método identify que imprima “Meu carro é um model,
da brand. Ele é do ano year e tem a cor color“. """


class Car:
    def identify(self, model: str, brand: str, year: str, color: str) -> str:
        print(
            f"""
        Meu carro é um {model}, da {brand}.
        Ele é do ano {year} e tem a cor {color}.
        """
        )


car_1 = Car()
car_1.identify("Maverick", "Ford", "1977", "vermelha")
