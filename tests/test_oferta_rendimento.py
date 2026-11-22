from datetime import date, timedelta
import pytest
from financeiro.estrategia_rendimento import RendimentoPoupanca
from financeiro.oferta_rendimento import OfertaRendimento


class TestOfertaRendimento:

    def setup_method(self) -> None:
        self.hoje = date.today()
        self.amanha = self.hoje + timedelta(days=1)
        self.ontem = self.hoje - timedelta(days=1)
        self.estrategia = RendimentoPoupanca(10.0)  # 10%

    def test_criar_oferta_com_sucesso(self) -> None:
        oferta = OfertaRendimento("BLACK_FRIDAY", self.amanha, self.estrategia)
        assert oferta.codigo == "BLACK_FRIDAY"
        assert oferta.validade == self.amanha
        assert oferta.estrategia is self.estrategia

    def test_codigo_obrigatorio(self) -> None:
        with pytest.raises(ValueError, match="Código da oferta é obrigatório"):
            OfertaRendimento("", self.amanha, self.estrategia)

    def test_oferta_valida(self) -> None:
        oferta = OfertaRendimento("PROMO10", self.amanha, self.estrategia)
        assert oferta.esta_valida(self.hoje) is True

    def test_oferta_expirada(self) -> None:
        oferta = OfertaRendimento("PROMO_ANTIGA", self.ontem, self.estrategia)
        assert oferta.esta_valida(self.hoje) is False

    def test_calcular_rendimento_oferta_valida(self) -> None:
        oferta = OfertaRendimento("PROMO10", self.amanha, self.estrategia)
        assert oferta.calcular_rendimento(1000.0) == 1100.0

    def test_calcular_rendimento_oferta_expirada_gera_erro(self) -> None:
        oferta = OfertaRendimento("PROMO_ANTIGA", self.ontem, self.estrategia)
        with pytest.raises(ValueError, match="expirada"):
            oferta.calcular_rendimento(1000.0)