import pytest

from financeiro.criador_leitor import CriadorLeitor
from financeiro.leitor import LeitorCSV, LeitorJSON


class TestCriadorLeitor:

    def setup_method(self) -> None:
        self.criador = CriadorLeitor()

    def test_cria_leitor_csv(self) -> None:
        leitor = self.criador.criar(".csv")
        assert isinstance(leitor, LeitorCSV)

    def test_cria_leitor_json(self) -> None:
        leitor = self.criador.criar(".json")
        assert isinstance(leitor, LeitorJSON)

    def test_cria_leitor_independe_de_caixa_e_espacos(self) -> None:
        leitor = self.criador.criar("  .CSV  ")
        assert isinstance(leitor, LeitorCSV)

    def test_extensao_desconhecida_gera_erro(self) -> None:
        with pytest.raises(
            ValueError, match="Extensão de arquivo desconhecida"
        ):
            self.criador.criar(".txt")