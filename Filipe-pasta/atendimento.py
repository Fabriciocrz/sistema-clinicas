from datetime import date, time
from clinica import Clinica
from paciente import Paciente
from procedimento import Procedimento
from profissional import Profissional
from tipoatendimento import TipoAtendimento


class Atendimento:
    def __init__(self, data: date, horario_inicio: time, horario_fim: time,
                 valor: float, codigo: int, clinica: Clinica,
                 tipo_atendimento: TipoAtendimento,
                 profissional: Profissional, paciente: Paciente):
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__valor = valor
        self.__codigo = codigo
        self.__clinica = clinica
        self.__tipo_atendimento = tipo_atendimento
        self.__profissional = profissional
        self.__paciente = paciente
        self.__procedimentos = []

    # ---------- clinica ----------
    @property
    def clinica(self) -> Clinica:
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica: Clinica) -> None:
        self.__clinica = clinica

    # ---------- tipo_atendimento ----------
    @property
    def tipo_atendimento(self) -> TipoAtendimento:
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento: TipoAtendimento) -> None:
        self.__tipo_atendimento = tipo_atendimento

    # ---------- profissional ----------
    @property
    def profissional(self) -> Profissional:
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: Profissional) -> None:
        self.__profissional = profissional

    # ---------- paciente ----------
    @property
    def paciente(self) -> Paciente:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente) -> None:
        self.__paciente = paciente

    # ---------- data ----------
    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date) -> None:
        self.__data = data

    # ---------- horario_inicio ----------
    @property
    def horario_inicio(self) -> time:
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio: time) -> None:
        self.__horario_inicio = horario_inicio

    # ---------- horario_fim ----------
    @property
    def horario_fim(self) -> time:
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim: time) -> None:
        self.__horario_fim = horario_fim

    # ---------- valor ----------
    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor: float) -> None:
        self.__valor = valor

    # ---------- codigo ----------
    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        self.__codigo = codigo

    # ---------- procedimentos ----------
    @property
    def procedimentos(self) -> list:
        return self.__procedimentos

    def incluir_procedimento(self, descricao: str, custo: float, codigo: int,
                             profissional: Profissional) -> None:
        procedimento = Procedimento(descricao, custo, codigo, profissional)
        self.__procedimentos.append(procedimento)

    def excluir_procedimento(self, codigo: int) -> None:
        for procedimento in self.__procedimentos:
            if procedimento.codigo == codigo:
                self.__procedimentos.remove(procedimento)
                break
