import pytest

from financeiro.estrategia_rendimento import (
    RendimentoCDBPreFixado,
    RendimentoPoupanca,
)


class TestRendimentoPoupanca:

    def test_calcula_rendimento(self) -> None:
        estrategia = RendimentoPoupanca(10)

        assert estrategia.calcular(1000.0) == 1100.0

    def test_percentual_negativo_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            RendimentoPoupanca(-1)

    def test_percentual_acima_de_cem_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            RendimentoPoupanca(101)


class TestRendimentoCDBPreFixado:

    def test_calcula_rendimento(self) -> None:
        estrategia = RendimentoCDBPreFixado(15)

        assert estrategia.calcular(1000.0) == 1150.0

    def test_percentual_negativo_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            RendimentoCDBPreFixado(-1)

    def test_percentual_acima_de_cem_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            RendimentoCDBPreFixado(101)