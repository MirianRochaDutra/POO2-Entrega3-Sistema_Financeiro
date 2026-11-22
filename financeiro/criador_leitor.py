from financeiro.leitor import Leitor, LeitorCSV, LeitorJSON


class CriadorLeitor:

    def criar(self, extensao: str) -> Leitor:
        extensao_normalizada = extensao.lower().strip()
        if extensao_normalizada == ".csv":
            return LeitorCSV()
        if extensao_normalizada == ".json":
            return LeitorJSON()
        raise ValueError(f"Extensão de arquivo desconhecida: {extensao}")