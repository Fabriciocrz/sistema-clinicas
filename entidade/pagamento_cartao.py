from datetime import date

from entidade.pagamento import Pagamento


class PagamentoCartao(Pagamento):
    """Pagamento com cartão de crédito: guarda o número do cartão e a bandeira."""

    def __init__(self, data: date, valor_pago: float, codigo: int,
                 numero_cartao: str, bandeira: str):
        super().__init__(data, valor_pago, codigo)
        self.__numero_cartao = None
        self.__bandeira = None
        self.numero_cartao = numero_cartao
        self.bandeira = bandeira

    @property
    def numero_cartao(self) -> str:
        return self.__numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao: str) -> None:
        if not isinstance(numero_cartao, str):
            raise TypeError("O número do cartão deve ser texto.")
        if not (numero_cartao.isdigit() and 13 <= len(numero_cartao) <= 19):
            raise ValueError("O número do cartão deve ter de 13 a 19 dígitos.")
        self.__numero_cartao = numero_cartao

    @property
    def bandeira(self) -> str:
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira: str) -> None:
        if not isinstance(bandeira, str) or not bandeira.strip():
            raise ValueError("A bandeira do cartão é obrigatória.")
        self.__bandeira = bandeira.strip()

    def modalidade(self) -> str:
        return "Cartão"

    def detalhes(self) -> dict:
        return {"numero_cartao": self.__numero_cartao, "bandeira": self.__bandeira}
