from datetime import date

from financeiro.categoria import Categoria


class Lancamento:

    def __init__(
        self,
        descricao: str,
        valor: float,
        data: date,
        categoria: Categoria,
        tipo: str,
    ) -> None:

        if not descricao:
            raise ValueError("Descrição é obrigatória")

        if valor <= 0:
            raise ValueError("Valor deve ser positivo")

        if tipo not in ("debito", "credito"):
            raise ValueError("Tipo deve ser 'debito' ou 'credito'")

        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.tipo = tipo

    def eh_debito(self) -> bool:
        return self.tipo == "debito"

    def eh_credito(self) -> bool:
        return self.tipo == "credito"