from financeiro.aplicacao import montar_aplicacao
from financeiro.servico_importacao import ServicoImportacao


class TestAplicacao:

    def test_montar_aplicacao_retorna_servico_configurado(self) -> None:
        servico = montar_aplicacao()
        assert isinstance(servico, ServicoImportacao)
