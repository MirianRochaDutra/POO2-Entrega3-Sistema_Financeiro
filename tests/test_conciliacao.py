from datetime import date

import pytest

from financeiro.categoria import Categoria
from financeiro.conciliacao import Conciliacao
from financeiro.lancamento import Lancamento


class TestConciliacao:

    def setup_method(self) -> None:
        self.categoria = Categoria("Financeiro")

        self.debito = Lancamento(
            "Transferência",
            1000.0,
            date(2026, 8, 10),
            self.categoria,
            "debito",
        )

        self.credito = Lancamento(
            "Transferência",
            1000.0,
            date(2026, 8, 10),
            self.categoria,
            "credito",
        )

    def test_conciliacao_bate(self) -> None:
        conciliacao = Conciliacao(
            [self.debito],
            [self.credito],
        )

        assert conciliacao.esta_conciliada() is True

    def test_conciliacao_nao_bate(self) -> None:
        outro_credito = Lancamento(
            "Transferência",
            500.0,
            date(2026, 8, 10),
            self.categoria,
            "credito",
        )

        conciliacao = Conciliacao(
            [self.debito],
            [outro_credito],
        )

        assert conciliacao.esta_conciliada() is False

    def test_conciliacao_bate_sem_erro(self) -> None:
        conciliacao = Conciliacao(
            [self.debito],
            [self.credito],
        )

        conciliacao.conciliar()

    def test_conciliacao_nao_bate_gera_erro(self) -> None:
        outro_credito = Lancamento(
            "Transferência",
            500.0,
            date(2026, 8, 10),
            self.categoria,
            "credito",
        )

        conciliacao = Conciliacao(
            [self.debito],
            [outro_credito],
        )

        with pytest.raises(ValueError, match="Conciliação não bate"):
            conciliacao.conciliar()

    def test_conciliacao_vazia(self) -> None:
        conciliacao = Conciliacao([], [])

        assert conciliacao.esta_conciliada() is True