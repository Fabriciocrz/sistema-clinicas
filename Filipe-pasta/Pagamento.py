from abc import ABC, abstractmethod
from datetime import date

from atendimento import Atendimento
from paciente import Paciente


class Pagamento(ABC):

    def __init__(
        self,
        data: date,
        valor_pago: float,
        codigo: int,
        atendimento: Atendimento,
        paciente: Paciente
    ):
        self.__data = data
        self.__valor_pago = valor_pago
        self.__codigo = codigo
        self.__atendimento = atendimento
        self.__paciente = paciente

    @property
    def atendimento(self) -> Atendimento:
        return self.__atendimento

    @atendimento.setter
    def atendimento(self, atendimento: Atendimento) -> None:
        self.__atendimento = atendimento

    @property
    def paciente(self) -> Paciente:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente) -> None:
        self.__paciente = paciente

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date) -> None:
        self.__data = data

    @property
    def valor_pago(self) -> float:
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor_pago: float) -> None:
        self.__valor_pago = valor_pago

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        self.__codigo = codigo

    @abstractmethod
    def modalidade(self) -> str:
        pass
