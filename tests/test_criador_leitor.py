import pytest

from financeiro.criador_leitor import CriadorLeitor
from financeiro.leitor import LeitorCSV, LeitorJSON


class TestCriadorLeitor:

    def test_cria_leitor_csv(self) -> None:
        criador = CriadorLeitor()

        leitor = criador.criar(".csv")

        assert isinstance(leitor, LeitorCSV)

    def test_cria_leitor_json(self) -> None:
        criador = CriadorLeitor()

        leitor = criador.criar(".json")

        assert isinstance(leitor, LeitorJSON)

    def test_extensao_desconhecida(self) -> None:
        criador = CriadorLeitor()

        with pytest.raises(ValueError):
            criador.criar(".txt")