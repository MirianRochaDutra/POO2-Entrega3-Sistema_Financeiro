from datetime import date

from financeiro.criador_importador import CriadorImportador
from financeiro.criador_leitor import CriadorLeitor
from financeiro.exportador_relatorio import ExportadorCSV
from financeiro.servico_importacao import ServicoImportacao


class LeitorFake:

    def ler(self, caminho: str) -> list:
        return []


class CriadorLeitorFake:

    def criar(self, extensao: str) -> LeitorFake:
        return LeitorFake()


class CriadorImportadorFake:

    def criar(self, banco: str):
        class ImportadorFake:

            def importar(self, lancamentos: list) -> list:
                return lancamentos

        return ImportadorFake()


class ExportadorFake:

    def exportar(self, relatorio) -> str:
        return "relatorio gerado"


class TestServicoImportacao:

    def test_importar_com_colaboradores_reais(self, tmp_path) -> None:
        arquivo = tmp_path / "lancamentos.csv"

        arquivo.write_text(
            "descricao,valor,data,categoria,tipo\n"
            "Mercado,300.0,2026-08-10,Geral,debito\n",
            encoding="utf-8",
        )

        servico = ServicoImportacao(
            CriadorLeitor(),
            CriadorImportador(),
            ExportadorCSV(),
        )

        resultado = servico.importar(
            str(arquivo),
            ".csv",
            "banco_x",
            date(2026, 8, 1),
            date(2026, 8, 31),
        )

        assert "Relatório Financeiro" in resultado

    def test_substituir_colaboradores_por_dubles(self, tmp_path) -> None:
        arquivo = tmp_path / "arquivo.csv"
        arquivo.write_text("", encoding="utf-8")

        servico = ServicoImportacao(
            CriadorLeitorFake(),
            CriadorImportadorFake(),
            ExportadorFake(),
        )

        resultado = servico.importar(
            str(arquivo),
            ".csv",
            "banco_x",
            date(2026, 8, 1),
            date(2026, 8, 31),
        )

        assert resultado == "relatorio gerado"