class Eletrodomestico:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0

    def ligar(self, velocidade):
        if velocidade > self.__velocidade_maxima or velocidade < 0:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.__velocidade_maxima}"
            )

        self.__velocidade = velocidade
        self.__corrente_atual_no_motor = (
            (self._potencia / self._tensao) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return self.__ligado

    def qual_velocidade(self):
        return self.__velocidade

    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor


# Acessando a superclasse diretamente
class Secador(Eletrodomestico):
    def mostrar_dados(self):
        print(
            f"""
        SECADOR
        - Cor: {self.cor}
        - Preço: R${self.preco}
        - Potência: {self._potencia}
        - Tensão: {self._tensao}
        """
        )

    # Chamando explicitamente métodos da superclasse
    def secagem_rápida(self):
        print("Temperatura máxima ativada.")
        Eletrodomestico.ligar(self, velocidade=3)
        print(f"Velocidade {Eletrodomestico.qual_velocidade(self)}.")


# Acessando a superclasse pelo método super()
class Batedeira(Eletrodomestico):
    def mostrar_dados(self):
        print(
            f"""
        BATEDEIRA
        - Cor: {self.cor}
        - Preço: R${self.preco}
        - Potência: {self._potencia}
        - Tensão: {self._tensao}
        """
        )

    # Uma vez que super() retorna uma instância direta
    # da superclasse vinculada ao objeto atual
    # não é necessário usar self
    def fazer_massa(self):
        print("Batedeira ligada na programação massas.")
        super().ligar(velocidade=2)
        print(f"Velocidade {super().qual_velocidade()}.")


# Usando o comando pass para criar a subclasse sem execuções adicionais
class MaquinaDeLavar(Eletrodomestico):
    pass


secador = Secador("Branco", 450, 127, "400")
secador.mostrar_dados()
secador.secagem_rápida()

batedeira = Batedeira("Prata", 200, 127, "290")
batedeira.mostrar_dados()
batedeira.fazer_massa()

maquina_de_lavar = MaquinaDeLavar("Preta", 6000, 127, "1300")

# Imprimindo dados explicitamente pela instância do objeto atual
print(
    f"""
        MÁQUINA DE LAVAR
        - Cor: {maquina_de_lavar.cor}
        - Preço: R${maquina_de_lavar.preco}
        - Potência: {maquina_de_lavar._potencia}
        - Tensão: {maquina_de_lavar._tensao}
        """
)
