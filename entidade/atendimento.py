from datetime import date
from datetime import time
from entidade.clinica import Clinica
from entidade.tipo_atendimento import TipoAtendimento
from entidade.profissional import Profissional
from entidade.paciente import Paciente
from entidade.procedimento import Procedimento

class Atendimento:

    def __init__(self, data: date, horario_inicio:time, horario_fim:time,
                  valor_base:float, codigo:int, numero_parcelas:int, clinica:Clinica,
                    tipo_atendimento:TipoAtendimento, profissional: Profissional, paciente:Paciente):
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__valor_base = valor_base
        self.__codigo = codigo
        self.__numero_parcelas = numero_parcelas
        self.__clinica = clinica
        self.__tipo_atendimento = tipo_atendimento
        self.__profissional = profissional
        self.__paciente = paciente
        self.__procedimentos = []
        self.__pagamentos = []

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data:date) -> None:
        self.__data = data

    @property
    def horario_inicio(self) -> time:
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio:time) -> None:
        self.__horario_inicio = horario_inicio

    @property
    def horario_fim(self) -> time:
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim:time) -> None:
        self.__horario_fim = horario_fim

    @property
    def valor_base(self) -> float:
        return self.__valor_base

    @valor_base.setter
    def valor_base(self, valor_base:float) -> None:
        self.__valor_base = valor_base

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo:int) -> None:
        self.__codigo = codigo

    @property
    def numero_parcelas(self) -> int:
        return self.__numero_parcelas

    @numero_parcelas.setter
    def numero_parcelas(self, numero_parcelas:int) -> None:
        self.__numero_parcelas = numero_parcelas

    @property
    def clinica(self) -> Clinica:
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica: Clinica) -> None:
        self.__clinica = clinica

    @property
    def tipo_atendimento(self) -> TipoAtendimento:
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento: TipoAtendimento) -> None:
        self.__tipo_atendimento = tipo_atendimento

    @property
    def profissional(self) -> Profissional:
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: Profissional) -> None:
        self.__profissional = profissional

    @property
    def paciente(self) -> Paciente:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente) -> None:
        self.__paciente = paciente

    @property
    def procedimentos(self) -> list:
        return self.__procedimentos

    @property
    def pagamentos(self) -> list:
        return self.__pagamentos

    def incluir_procedimento(self, descricao: str, custo: float, codigo: int, profissional: Profissional) -> None:
        procedimento = Procedimento(descricao, custo, codigo, profissional)
        self.__procedimentos.append(procedimento)


    def excluir_procedimento(self, codigo: int) -> None:
        for procedimento in self.__procedimentos:
            if procedimento.codigo == codigo:
                self.__procedimentos.remove(procedimento)
                return

    def incluir_pagamento(self, pagamento) -> None:
        self.__pagamentos.append(pagamento)

    def excluir_pagamento(self, codigo:int) -> None:
        for pagamento in self.__pagamentos:
            if pagamento.codigo == codigo:
                self.__pagamentos.remove(pagamento)
                return

    def valor_total(self):
        total = self.__valor_base
        for procedimento in self.__procedimentos:
            total += procedimento.custo
        return total

    def total_pago(self):
        total = 0
        for pagamento in self.__pagamentos:
            total += pagamento.valor_pago
        return total

    def valor_restante(self):
        valor = self.valor_total() - self.total_pago()
        return valor

    def valor_parcela(self):
        parcelas_faltando = self.__numero_parcelas - len(self.__pagamentos)
        if self.__numero_parcelas - len(self.__pagamentos) > 0:
            valor = self.valor_restante() / parcelas_faltando
            return valor
        else:
            return 0 
