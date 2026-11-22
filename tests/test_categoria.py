import pytest

from financeiro.categoria import Categoria


class TestCategoria:

    def test_criar_categoria(self) -> None:
        categoria = Categoria("Alimentação")

        assert categoria.nome == "Alimentação"

    def test_nome_obrigatorio(self) -> None:
        with pytest.raises(ValueError):
            Categoria("")