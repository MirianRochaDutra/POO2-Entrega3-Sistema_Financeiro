import pytest

from financeiro.estrategia_correcao_monetaria import (
    CorrecaoINPC,
    CorrecaoIPCA,
)


class TestCorrecaoIPCA:

    def test_calcula_correcao(self) -> None:
        estrategia = CorrecaoIPCA(5)

        assert estrategia.calcular(1000.0) == 1050.0

    def test_percentual_negativo_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            CorrecaoIPCA(-1)

    def test_percentual_acima_de_cem_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            CorrecaoIPCA(101)


class TestCorrecaoINPC:

    def test_calcula_correcao(self) -> None:
        estrategia = CorrecaoINPC(8)

        assert estrategia.calcular(1000.0) == 1080.0

    def test_percentual_negativo_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            CorrecaoINPC(-1)

    def test_percentual_acima_de_cem_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            CorrecaoINPC(101)