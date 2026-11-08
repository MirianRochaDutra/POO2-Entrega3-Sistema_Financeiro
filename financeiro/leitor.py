import csv
import json
from abc import ABC, abstractmethod
from datetime import date

from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento


class Leitor(ABC):

    @abstractmethod
    def ler(self, caminho: str) -> list[Lancamento]:
        ...


class LeitorCSV(Leitor):

    def ler(self, caminho: str) -> list[Lancamento]:
        lancamentos = []

        with open(caminho, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                categoria = Categoria(linha["categoria"])

                lancamento = Lancamento(
                    linha["descricao"],
                    float(linha["valor"]),
                    date.fromisoformat(linha["data"]),
                    categoria,
                    linha["tipo"],
                )

                lancamentos.append(lancamento)

        return lancamentos


class LeitorJSON(Leitor):

    def ler(self, caminho: str) -> list[Lancamento]:
        lancamentos = []

        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        for linha in dados:
            categoria = Categoria(linha["categoria"])

            lancamento = Lancamento(
                linha["descricao"],
                float(linha["valor"]),
                date.fromisoformat(linha["data"]),
                categoria,
                linha["tipo"],
            )

            lancamentos.append(lancamento)

        return lancamentos