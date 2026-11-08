from financeiro.leitor import Leitor, LeitorCSV, LeitorJSON


class CriadorLeitor:

    def criar(self, extensao: str) -> Leitor:
        if extensao.lower() == ".csv":
            return LeitorCSV()

        if extensao.lower() == ".json":
            return LeitorJSON()

        raise ValueError(f"Extensão de arquivo desconhecida: {extensao}")