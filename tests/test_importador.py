from datetime import date

import pytest

from financeiro.categoria import Categoria
from financeiro.criador_importador import CriadorImportador
from financeiro.importador import (
    ImportadorBancoX,
    ImportadorBancoY,
)
from financeiro.lancamento import Lancamento


class TestCriadorImportador:

    def test_cria_importador_banco_x(self) -> None:
        criador = CriadorImportador()

        importador = criador.criar("banco_x")

        assert isinstance(importador, ImportadorBancoX)

    def test_cria_importador_banco_y(self) -> None:
        criador = CriadorImportador()

        importador = criador.criar("banco_y")

        assert isinstance(importador, ImportadorBancoY)

    def test_banco_desconhecido(self) -> None:
        criador = CriadorImportador()

        with pytest.raises(ValueError):
            criador.criar("banco_desconhecido")


class TestImportadores:

    def setup_method(self) -> None:
        categoria = Categoria("Geral")

        self.lancamento = Lancamento(
            "Mercado",
            300.0,
            date(2026, 8, 10),
            categoria,
            "debito",
        )

    def test_importador_banco_x(self) -> None:
        importador = ImportadorBancoX()

        resultado = importador.importar([self.lancamento])

        assert len(resultado) == 1
        assert resultado[0] == self.lancamento

    def test_importador_banco_y(self) -> None:
        importador = ImportadorBancoY()

        resultado = importador.importar([self.lancamento])

        assert len(resultado) == 1
        assert resultado[0] == self.lancamento