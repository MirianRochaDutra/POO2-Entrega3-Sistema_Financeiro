import pytest

from financeiro.criador_importador import CriadorImportador
from financeiro.importador import ImportadorBancoX, ImportadorBancoY


class TestCriadorImportador:

    def setup_method(self) -> None:
        self.criador = CriadorImportador()

    def test_criar_importador_banco_x(self) -> None:
        importador = self.criador.criar("banco_x")
        assert isinstance(importador, ImportadorBancoX)

    def test_criar_importador_banco_y(self) -> None:
        importador = self.criador.criar("banco_y")
        assert isinstance(importador, ImportadorBancoY)

    def test_criar_importador_independe_de_caixa_e_espacos(self) -> None:
        importador = self.criador.criar("  BANCO_X  ")
        assert isinstance(importador, ImportadorBancoX)

    def test_banco_desconhecido_lanca_erro(self) -> None:
        with pytest.raises(ValueError, match="Banco de origem desconhecido"):
            self.criador.criar("banco_z")