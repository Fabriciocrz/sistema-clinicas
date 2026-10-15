from datetime import date

from entidade.pagamento import Pagamento


class PagamentoDinheiro(Pagamento):
    """Pagamento em dinheiro: não possui atributos próprios."""

    def __init__(self, data: date, valor_pago: float, codigo: int):
        super().__init__(data, valor_pago, codigo)

    def modalidade(self) -> str:
        return "Dinheiro"
