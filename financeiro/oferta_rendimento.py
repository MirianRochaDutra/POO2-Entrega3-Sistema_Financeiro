from datetime import date
from financeiro.estrategia_rendimento import EstrategiaRendimento


class OfertaRendimento:
    """Entidade que possui um código, uma data de validade e aplica uma

    estratégia de rendimento via composição enquanto estiver válida.
    """

    def __init__(
        self,
        codigo: str,
        validade: date,
        estrategia: EstrategiaRendimento,
    ) -> None:
        if not codigo:
            raise ValueError("Código da oferta é obrigatório")

        self._codigo = codigo
        self._validade = validade
        self._estrategia = estrategia

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def validade(self) -> date:
        return self._validade

    @property
    def estrategia(self) -> EstrategiaRendimento:
        return self._estrategia

    def esta_valida(self, hoje: date | None = None) -> bool:
        """Verifica se a oferta está dentro do prazo de validade.

        Se a data `hoje` não for informada, utiliza a data atual do sistema.
        """
        hoje = hoje if hoje is not None else date.today()
        return hoje <= self._validade

    def calcular_rendimento(self, valor: float) -> float:
        """Calcula o rendimento utilizando a estratégia associada.

        Lança ValueError caso a oferta esteja expirada.
        """
        if not self.esta_valida():
            raise ValueError(f"Oferta '{self._codigo}' está expirada")

        return self._estrategia.calcular(valor)