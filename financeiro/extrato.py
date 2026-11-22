from datetime import date

from financeiro.fechamento import Fechamento


class Extrato:

    def __init__(
        self,
        inicio: date,
        fim: date,
        fechamentos: list[Fechamento],
    ) -> None:

        if inicio > fim:
            raise ValueError("Data inicial não pode ser posterior à data final")

        self.inicio = inicio
        self.fim = fim
        self._fechamentos = list(fechamentos)

    @property
    def fechamentos(self) -> list[Fechamento]:
        return list(self._fechamentos)

    def quantidade_lancamentos(self) -> int:
        return sum(
            fechamento.quantidade_lancamentos()
            for fechamento in self._fechamentos
        )

    def total_debitos(self) -> float:
        return sum(
            fechamento.total_debitos()
            for fechamento in self._fechamentos
        )

    def total_creditos(self) -> float:
        return sum(
            fechamento.total_creditos()
            for fechamento in self._fechamentos
        )

    def saldo_final(self) -> float:
        return self.total_creditos() - self.total_debitos()