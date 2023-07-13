class Ventilador:
    def __init__(self, cor, modelo, preco):
        self.cor = cor
        self.modelo = modelo
        self.preco = preco
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3

    def ligar(self, velocidade):
        if velocidade > self.__velocidade_maxima or velocidade < 0:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.__velocidade_maxima}"
            )

        self.__velocidade = velocidade
        self.__ligado = True

    def desligar(self):
        if not self.__ligado & self.__velocidade == 0:
            raise ValueError("Seu ventilador já está desligado")

        self.__ligado = False
        self.__velocidade = 0


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.__saldo_na_conta = saldo_na_conta
        self.ventilador_adquirido = 0

    def comprar_ventilador(self, produto, quantidade):
        if (produto.preco * quantidade) > self.__saldo_na_conta:
            raise ValueError(
                f""""
            Não foi possível realizar a compra, saldo insuficiente.
            A compra custa R${produto.preco * quantidade}.
            Seu saldo na conta é R${self.__saldo_na_conta}.
            """
            )

        self.__saldo_na_conta -= (produto.preco * quantidade)
        self.ventilador_adquirido += quantidade
        print(
            f"""
        Compra realizada com sucesso!
        Seu saldo agora é R${self.__saldo_na_conta}.
        Você possui {self.ventilador_adquirido} ventilador(es) adquirido(s).
        """
        )


ventilador_silco_turbo = Ventilador("Vermelho", "Silco Turbo Max", 500)
consumidor = Pessoa("Juliana", 1000)
compra = consumidor.comprar_ventilador(ventilador_silco_turbo, 1)
