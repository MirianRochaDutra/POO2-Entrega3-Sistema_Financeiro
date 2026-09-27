from datetime import date

import pytest

from financeiro.categoria import Categoria
from financeiro.fechamento import Fechamento
from financeiro.lancamento import Lancamento


class TestFechamento:

    def setup_method(self) -> None:
        self.categoria = Categoria("Geral")

        self.debito = Lancamento(
            "Mercado",
            300.0,
            date(2026, 8, 10),
            self.categoria,
            "debito",
        )

        self.credito = Lancamento(
            "Salário",
            5000.0,
            date(2026, 8, 5),
            self.categoria,
            "credito",
        )

    def test_criar_fechamento(self) -> None:
        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [self.debito, self.credito],
        )

        assert fechamento.quantidade_lancamentos() == 2

    def test_total_debitos(self) -> None:
        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [self.debito, self.credito],
        )

        assert fechamento.total_debitos() == 300.0

    def test_total_creditos(self) -> None:
        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [self.debito, self.credito],
        )

        assert fechamento.total_creditos() == 5000.0

    def test_saldo(self) -> None:
        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [self.debito, self.credito],
        )

        assert fechamento.saldo() == 4700.0

    def test_fechamento_vazio(self) -> None:
        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [],
        )

        assert fechamento.quantidade_lancamentos() == 0
        assert fechamento.total_debitos() == 0
        assert fechamento.total_creditos() == 0
        assert fechamento.saldo() == 0

    def test_lancamento_fora_do_periodo(self) -> None:
        lancamento = Lancamento(
            "Compra",
            100.0,
            date(2026, 9, 1),
            self.categoria,
            "debito",
        )

        with pytest.raises(ValueError):
            Fechamento(
                date(2026, 8, 1),
                date(2026, 8, 31),
                [lancamento],
            )

    def test_fechamento_copia_lista(self) -> None:
        lancamentos = [self.debito]

        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            lancamentos,
        )

        lancamentos.clear()

        assert fechamento.quantidade_lancamentos() == 1