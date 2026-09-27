import pytest

from financeiro.conta import Conta


class TestConta:

    def test_criar_conta(self) -> None:
        conta = Conta("Conta corrente", 1000.0)

        assert conta.nome == "Conta corrente"
        assert conta.saldo == 1000.0

    def test_criar_conta_com_saldo_zero(self) -> None:
        conta = Conta("Carteira")

        assert conta.saldo == 0.0

    def test_debitar(self) -> None:
        conta = Conta("Conta corrente", 1000.0)

        conta.debitar(200.0)

        assert conta.saldo == 800.0

    def test_creditar(self) -> None:
        conta = Conta("Conta corrente", 1000.0)

        conta.creditar(500.0)

        assert conta.saldo == 1500.0

    def test_debito_invalido(self) -> None:
        conta = Conta("Conta corrente", 1000.0)

        with pytest.raises(ValueError):
            conta.debitar(0)

    def test_credito_invalido(self) -> None:
        conta = Conta("Conta corrente", 1000.0)

        with pytest.raises(ValueError):
            conta.creditar(0)