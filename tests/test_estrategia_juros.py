import pytest

from financeiro.estrategia_juros import JurosCompostos, JurosSimples


class TestJurosSimples:

    def test_calcula_juros_simples(self) -> None:
        estrategia = JurosSimples()

        assert estrategia.calcular(1000.0, 0.10, 2) == 1200.0

    def test_capital_negativo_lanca_erro(self) -> None:
        estrategia = JurosSimples()

        with pytest.raises(ValueError):
            estrategia.calcular(-1000.0, 0.10, 2)

    def test_taxa_negativa_lanca_erro(self) -> None:
        estrategia = JurosSimples()

        with pytest.raises(ValueError):
            estrategia.calcular(1000.0, -0.10, 2)

    def test_tempo_negativo_lanca_erro(self) -> None:
        estrategia = JurosSimples()

        with pytest.raises(ValueError):
            estrategia.calcular(1000.0, 0.10, -1)


class TestJurosCompostos:

    def test_calcula_juros_compostos(self) -> None:
        estrategia = JurosCompostos()

        assert estrategia.calcular(1000.0, 0.10, 2) == 1210.0

    def test_capital_negativo_lanca_erro(self) -> None:
        estrategia = JurosCompostos()

        with pytest.raises(ValueError):
            estrategia.calcular(-1000.0, 0.10, 2)

    def test_taxa_negativa_lanca_erro(self) -> None:
        estrategia = JurosCompostos()

        with pytest.raises(ValueError):
            estrategia.calcular(1000.0, -0.10, 2)

    def test_tempo_negativo_lanca_erro(self) -> None:
        estrategia = JurosCompostos()

        with pytest.raises(ValueError):
            estrategia.calcular(1000.0, 0.10, -1)