from datetime import date

from financeiro.categoria import Categoria
from financeiro.extrato import Extrato
from financeiro.fechamento import Fechamento
from financeiro.lancamento import Lancamento


class TestExtrato:

    def setup_method(self) -> None:
        categoria = Categoria("Geral")

        debito = Lancamento(
            "Mercado",
            300.0,
            date(2026, 8, 10),
            categoria,
            "debito",
        )

        credito = Lancamento(
            "Salário",
            5000.0,
            date(2026, 8, 5),
            categoria,
            "credito",
        )

        self.fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [debito, credito],
        )

    def test_criar_extrato(self) -> None:
        extrato = Extrato(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [self.fechamento],
        )

        assert len(extrato.fechamentos) == 1

    def test_quantidade_lancamentos(self) -> None:
        extrato = Extrato(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [self.fechamento],
        )

        assert extrato.quantidade_lancamentos() == 2

    def test_total_debitos(self) -> None:
        extrato = Extrato(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [self.fechamento],
        )

        assert extrato.total_debitos() == 300.0

    def test_total_creditos(self) -> None:
        extrato = Extrato(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [self.fechamento],
        )

        assert extrato.total_creditos() == 5000.0

    def test_saldo_final(self) -> None:
        extrato = Extrato(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [self.fechamento],
        )

        assert extrato.saldo_final() == 4700.0

    def test_extrato_sem_fechamentos(self) -> None:
        extrato = Extrato(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [],
        )

        assert extrato.quantidade_lancamentos() == 0
        assert extrato.total_debitos() == 0
        assert extrato.total_creditos() == 0
        assert extrato.saldo_final() == 0
    