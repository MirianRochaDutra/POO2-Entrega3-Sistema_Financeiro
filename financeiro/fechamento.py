from datetime import date

from financeiro.lancamento import Lancamento


class Fechamento:

    def __init__(
        self,
        inicio: date,
        fim: date,
        lancamentos: list[Lancamento],
    ) -> None:

        if inicio > fim:
            raise ValueError("Data inicial não pode ser posterior à data final")

        self.inicio = inicio
        self.fim = fim
        self._lancamentos = list(lancamentos)

        self._validar_lancamentos()

    @property
    def lancamentos(self) -> list[Lancamento]:
        return list(self._lancamentos)

    def _validar_lancamentos(self) -> None:
        for lancamento in self._lancamentos:
            if not (self.inicio <= lancamento.data <= self.fim): #"Se a data do lançamento NÃO estiver entre a data de início e a data de fim..."
                raise ValueError(
                    "Existe lançamento fora do período do fechamento"
                )

    def quantidade_lancamentos(self) -> int:
        return len(self._lancamentos)

    def total_debitos(self) -> float:
        return sum(
            lancamento.valor
            for lancamento in self._lancamentos
            if lancamento.eh_debito()
        )

    def total_creditos(self) -> float:
        return sum(
            lancamento.valor
            for lancamento in self._lancamentos
            if lancamento.eh_credito()
        )

    def saldo(self) -> float:
        return self.total_creditos() - self.total_debitos()