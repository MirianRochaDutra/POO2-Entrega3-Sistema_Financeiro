from financeiro.importador import Importador, ImportadorBancoX, ImportadorBancoY


class CriadorImportador:

    def criar(self, banco: str) -> Importador:
        banco_normalizado = banco.lower().strip()
        if banco_normalizado in ("banco_x", "bancox"):
            return ImportadorBancoX()
        if banco_normalizado in ("banco_y", "bancoy"):
            return ImportadorBancoY()
        raise ValueError(f"Banco de origem desconhecido: {banco}")