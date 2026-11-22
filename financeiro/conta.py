class Conta:

    def __init__(self, nome: str, saldo: float = 0.0) -> None:
        if not nome:
            raise ValueError("Nome da conta é obrigatório")

        self.nome = nome
        self.saldo = saldo

    def debitar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Valor do débito deve ser positivo")

        self.saldo -= valor

    def creditar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Valor do crédito deve ser positivo")

        self.saldo += valor


        