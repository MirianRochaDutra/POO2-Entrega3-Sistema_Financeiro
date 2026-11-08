from financeiro.criador_importador import CriadorImportador
from financeiro.criador_leitor import CriadorLeitor
from financeiro.extrato import Extrato
from financeiro.fechamento import Fechamento
from financeiro.exportador_relatorio import ExportadorRelatorio


class ServicoImportacao:

    def __init__(
        self,
        criador_leitor: CriadorLeitor,
        criador_importador: CriadorImportador,
        exportador: ExportadorRelatorio,
    ) -> None:

        self._criador_leitor = criador_leitor
        self._criador_importador = criador_importador
        self._exportador = exportador

    def importar(
        self,
        caminho: str,
        extensao: str,
        banco: str,
        inicio,
        fim,
    ) -> str:

        leitor = self._criador_leitor.criar(extensao)

        lancamentos = leitor.ler(caminho)

        importador = self._criador_importador.criar(banco)

        lancamentos = importador.importar(lancamentos)

        fechamento = Fechamento(
            inicio,
            fim,
            lancamentos,
        )

        extrato = Extrato(
            inicio,
            fim,
            [fechamento],
        )

        return self._exportador.exportar(extrato)
