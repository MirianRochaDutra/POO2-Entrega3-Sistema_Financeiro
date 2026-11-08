from abc import ABC, abstractmethod

from financeiro.lancamento import Lancamento


class Importador(ABC):

    @abstractmethod
    def importar(self, lancamentos: list[Lancamento]) -> list[Lancamento]:
        ...


class ImportadorBancoX(Importador):

    def importar(self, lancamentos: list[Lancamento]) -> list[Lancamento]:
        return list(lancamentos)


class ImportadorBancoY(Importador):

    def importar(self, lancamentos: list[Lancamento]) -> list[Lancamento]:
        return list(lancamentos)