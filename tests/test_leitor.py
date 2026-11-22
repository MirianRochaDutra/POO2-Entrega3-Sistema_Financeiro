import json
from datetime import date

import pytest

from financeiro.leitor import LeitorCSV, LeitorJSON


class TestLeitorCSV:

    def test_ler_arquivo_csv(self, tmp_path) -> None:
        arquivo = tmp_path / "lancamentos.csv"
        arquivo.write_text(
            "descricao,valor,data,categoria,tipo\n"
            "Mercado,300.0,2026-08-10,Alimentação,debito\n"
            "Salário,5000.0,2026-08-05,Renda,credito\n",
            encoding="utf-8",
        )
        leitor = LeitorCSV()
        lancamentos = leitor.ler(str(arquivo))

        assert len(lancamentos) == 2
        assert lancamentos.descricao == "Mercado"
        assert lancamentos.valor == 300.0
        assert lancamentos.data == date(2026, 8, 10)
        assert lancamentos.categoria.nome == "Alimentação"
        assert lancamentos.eh_debito() is True

        assert lancamentos[1].descricao == "Salário"
        assert lancamentos[1].valor == 5000.0
        assert lancamentos[1].eh_credito() is True


class TestLeitorJSON:

    def test_ler_arquivo_json(self, tmp_path) -> None:
        arquivo = tmp_path / "lancamentos.json"
        dados = [
            {
                "descricao": "Mercado",
                "valor": 300.0,
                "data": "2026-08-10",
                "categoria": "Alimentação",
                "tipo": "debito",
            },
            {
                "descricao": "Salário",
                "valor": 5000.0,
                "data": "2026-08-05",
                "categoria": "Renda",
                "tipo": "credito",
            },
        ]
        arquivo.write_text(json.dumps(dados), encoding="utf-8")

        leitor = LeitorJSON()
        lancamentos = leitor.ler(str(arquivo))

        assert len(lancamentos) == 2
        assert lancamentos.descricao == "Mercado"
        assert lancamentos.valor == 300.0
        assert lancamentos[1].descricao == "Salário"
        assert lancamentos[1].valor == 5000.0