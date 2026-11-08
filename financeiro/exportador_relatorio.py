from abc import ABC, abstractmethod

from financeiro.extrato import Extrato


class DocumentoRelatorio:

    def __init__(self) -> None:
        self._linhas: list[str] = []

    def adicionar(self, linha: str) -> None:
        self._linhas.append(linha)

    def conteudo(self) -> str:
        return "\n".join(self._linhas)


class DocumentoCSV(DocumentoRelatorio):
    pass


class DocumentoHTML(DocumentoRelatorio):
    def conteudo(self) -> str:
        linhas = ["<html>", "<body>"]

        for linha in self._linhas:
            linhas.append(f"<p>{linha}</p>")

        linhas.append("</body>")
        linhas.append("</html>")

        return "\n".join(linhas)


class ExportadorRelatorio(ABC):

    def exportar(self, relatorio: Extrato) -> str:
        documento = self.criar_documento()

        documento.adicionar("Relatório Financeiro")
        documento.adicionar(
            f"Período: {relatorio.inicio} até {relatorio.fim}"
        )
        documento.adicionar(
            f"Quantidade de lançamentos: "
            f"{relatorio.quantidade_lancamentos()}"
        )
        documento.adicionar(
            f"Total de débitos: {relatorio.total_debitos()}"
        )
        documento.adicionar(
            f"Total de créditos: {relatorio.total_creditos()}"
        )
        documento.adicionar(
            f"Saldo final: {relatorio.saldo_final()}"
        )

        return documento.conteudo()

    @abstractmethod
    def criar_documento(self) -> DocumentoRelatorio:
        ...


class ExportadorCSV(ExportadorRelatorio):

    def criar_documento(self) -> DocumentoRelatorio:
        return DocumentoCSV()


class ExportadorHTML(ExportadorRelatorio):

    def criar_documento(self) -> DocumentoRelatorio:
        return DocumentoHTML()