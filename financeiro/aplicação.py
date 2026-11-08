from financeiro.criador_importador import CriadorImportador
from financeiro.criador_leitor import CriadorLeitor
from financeiro.exportador_relatorio import ExportadorCSV
from financeiro.servico_importacao import ServicoImportacao


def montar_aplicacao() -> ServicoImportacao:
    criador_leitor = CriadorLeitor()
    criador_importador = CriadorImportador()
    exportador = ExportadorCSV()

    return ServicoImportacao(
        criador_leitor,
        criador_importador,
        exportador,
    )