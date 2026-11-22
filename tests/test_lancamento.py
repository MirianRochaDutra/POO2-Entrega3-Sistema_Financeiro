from datetime import date

import pytest

from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento


class TestLancamento:

    def setup_method(self) -> None:
        self.categoria = Categoria("Alimentação")
        self.data = date(2026, 8, 20)

    def test_criar_lancamento(self) -> None:
        lancamento = Lancamento(
            "Supermercado",
            300.0,
            self.data,
            self.categoria,
            "debito",
        )

        assert lancamento.descricao == "Supermercado"
        assert lancamento.valor == 300.0
        assert lancamento.data == self.data
        assert lancamento.categoria == self.categoria
        assert lancamento.tipo == "debito"

    def test_lancamento_debito(self) -> None:
        lancamento = Lancamento(
            "Supermercado",
            300.0,
            self.data,
            self.categoria,
            "debito",
        )

        assert lancamento.eh_debito() is True
        assert lancamento.eh_credito() is False

    def test_lancamento_credito(self) -> None:
        lancamento = Lancamento(
            "Salário",
            5000.0,
            self.data,
            self.categoria,
            "credito",
        )

        assert lancamento.eh_credito() is True
        assert lancamento.eh_debito() is False

    def test_valor_invalido(self) -> None:
        with pytest.raises(ValueError):
            Lancamento(
                "Supermercado",
                0,
                self.data,
                self.categoria,
                "debito",
            )

    def test_tipo_invalido(self) -> None:
        with pytest.raises(ValueError):
            Lancamento(
                "Supermercado",
                300.0,
                self.data,
                self.categoria,
                "invalido",
            )