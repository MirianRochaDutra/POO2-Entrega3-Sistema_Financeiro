class Categoria:

    def __init__(self, nome: str) -> None:
        if not nome:
            raise ValueError("Nome da categoria é obrigatório")

        self.nome = nome

        