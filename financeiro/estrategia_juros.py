from abc import ABC, abstractmethod


class EstrategiaJuros(ABC):

    @abstractmethod
    def calcular(self, capital: float, taxa: float, tempo: int) -> float:
        ...


class JurosSimples(EstrategiaJuros):

    def calcular(self, capital: float, taxa: float, tempo: int) -> float:
        if capital < 0:
            raise ValueError("Capital não pode ser negativo")

        if taxa < 0:
            raise ValueError("Taxa não pode ser negativa")

        if tempo < 0:
            raise ValueError("Tempo não pode ser negativo")

        juros = capital * taxa * tempo
        return capital + juros


class JurosCompostos(EstrategiaJuros):

    def calcular(self, capital: float, taxa: float, tempo: int) -> float:
        if capital < 0:
            raise ValueError("Capital não pode ser negativo")

        if taxa < 0:
            raise ValueError("Taxa não pode ser negativa")

        if tempo < 0:
            raise ValueError("Tempo não pode ser negativo")

        return round(capital * ((1 + taxa) ** tempo), 2)