from datetime import date
from atendimento import Atendimento
from paciente import Paciente
from pagamento import Pagamento


class PagamentoDinheiro(Pagamento):
    def __init__(self, data: date, valor_pago: float, codigo: int,
                 atendimento: Atendimento, paciente: Paciente):
        super().__init__(data, valor_pago, codigo, atendimento, paciente)

    def modalidade(self) -> str:
        return "Dinheiro"
