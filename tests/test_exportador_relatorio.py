from datetime import date

from financeiro.categoria import Categoria
from financeiro.exportador_relatorio import (
    ExportadorCSV,
    ExportadorHTML,
)
from financeiro.extrato import Extrato
from financeiro.fechamento import Fechamento
from financeiro.lancamento import Lancamento


class TestExportadorRelatorio:

    def setup_method(self) -> None:
        categoria = Categoria("Geral")

        debito = Lancamento(
            "Mercado",
            300.0,
            date(2026, 8, 10),
            categoria,
            "debito",
        )

        credito = Lancamento(
            "Salário",
            5000.0,
            date(2026, 8, 5),
            categoria,
            "credito",
        )

        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [debito, credito],
        )

        self.extrato = Extrato(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [fechamento],
        )

    def test_exportador_csv(self) -> None:
        exportador = ExportadorCSV()

        resultado = exportador.exportar(self.extrato)

        assert "Relatório Financeiro" in resultado
        assert "Total de débitos: 300.0" in resultado
        assert "Total de créditos: 5000.0" in resultado

    def test_exportador_html(self) -> None:
        exportador = ExportadorHTML()

        resultado = exportador.exportar(self.extrato)

        assert "<html>" in resultado
        assert "<body>" in resultado
        assert "Relatório Financeiro" in resultado
        assert "</html>" in resultado