from datetime import date

from financeiro.categoria import Categoria
from financeiro.importador import ImportadorBancoX, ImportadorBancoY
from financeiro.lancamento import Lancamento


class TestImportador:

    def setup_method(self) -> None:
        categoria = Categoria("Geral")
        self.lancamentos = [
            Lancamento(
                "Compra", 100.0, date(2026, 8, 10), categoria, "debito"
            )
        ]

    def test_importador_banco_x(self) -> None:
        importador = ImportadorBancoX()
        resultado = importador.importar(self.lancamentos)
        assert len(resultado) == 1
        assert resultado.descricao == "Compra"

    def test_importador_banco_y(self) -> None:
        importador = ImportadorBancoY()
        resultado = importador.importar(self.lancamentos)
        assert len(resultado) == 1
        assert resultado.descricao == "Compra"