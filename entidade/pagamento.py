from abc import ABC, abstractmethod
from datetime import date


class Pagamento(ABC):
    """Pagamento abstrato. Cada modalidade concreta define modalidade();
    as regras que envolvem o atendimento ficam em Atendimento."""

    @abstractmethod
    def __init__(self, data: date, valor_pago: float, codigo: int):
        self.data = data
        self.valor_pago = valor_pago
        self.codigo = codigo

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date) -> None:
        if not isinstance(data, date):
            raise TypeError("A data do pagamento deve ser do tipo date.")
        self.__data = data

    @property
    def valor_pago(self) -> float:
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor_pago: float) -> None:
        if not isinstance(valor_pago, (int, float)) or isinstance(valor_pago, bool):
            raise TypeError("O valor pago deve ser numérico.")
        if valor_pago <= 0:
            raise ValueError("O valor pago deve ser maior que zero.")
        self.__valor_pago = float(valor_pago)

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        if not isinstance(codigo, int) or isinstance(codigo, bool):
            raise TypeError("O código do pagamento deve ser inteiro.")
        if codigo <= 0:
            raise ValueError("O código do pagamento deve ser positivo.")
        self.__codigo = codigo

    @abstractmethod
    def modalidade(self) -> str:
        """Nome da modalidade (Dinheiro, Cartão, Pix)."""
