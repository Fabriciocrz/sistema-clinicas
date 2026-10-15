from datetime import time

from entidade.profissional import Profissional


class Clinica:
    """Clínica que agrega profissionais."""

    def __init__(self, nome: str, cidade: str, descricao: str,
                 horario_abertura: time, horario_fechamento: time, codigo: int):
        self.__profissionais: list[Profissional] = []
        self.nome = nome
        self.cidade = cidade
        self.descricao = descricao
        self.horario_abertura = horario_abertura
        self.horario_fechamento = horario_fechamento
        self.codigo = codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise TypeError("O nome da clínica deve ser texto.")
        if not nome.strip():
            raise ValueError("O nome da clínica é obrigatório.")
        self.__nome = nome.strip()

    @property
    def cidade(self) -> str:
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str) -> None:
        if not isinstance(cidade, str):
            raise TypeError("A cidade da clínica deve ser texto.")
        if not cidade.strip():
            raise ValueError("A cidade da clínica é obrigatória.")
        self.__cidade = cidade.strip()

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        if not isinstance(descricao, str):
            raise TypeError("A descrição da clínica deve ser texto.")
        if not descricao.strip():
            raise ValueError("A descrição da clínica é obrigatória.")
        self.__descricao = descricao.strip()

    @property
    def horario_abertura(self) -> time:
        return self.__horario_abertura

    @horario_abertura.setter
    def horario_abertura(self, horario_abertura: time) -> None:
        if not isinstance(horario_abertura, time):
            raise TypeError("O horário de abertura deve ser do tipo time.")
        self.__horario_abertura = horario_abertura

    @property
    def horario_fechamento(self) -> time:
        return self.__horario_fechamento

    @horario_fechamento.setter
    def horario_fechamento(self, horario_fechamento: time) -> None:
        if not isinstance(horario_fechamento, time):
            raise TypeError("O horário de fechamento deve ser do tipo time.")
        self.__horario_fechamento = horario_fechamento

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        if not isinstance(codigo, int) or isinstance(codigo, bool):
            raise TypeError("O código da clínica deve ser inteiro.")
        if codigo <= 0:
            raise ValueError("O código da clínica deve ser positivo.")
        self.__codigo = codigo

    @property
    def profissionais(self) -> list[Profissional]:
        # Cópia: a lista interna só é alterada por incluir/excluir.
        return list(self.__profissionais)

    def incluir_profissional(self, profissional: Profissional) -> None:
        if not isinstance(profissional, Profissional):
            raise TypeError("O objeto informado não é um Profissional.")
        for p in self.__profissionais:
            if p.cpf == profissional.cpf:
                raise ValueError("O profissional já está vinculado a esta clínica.")
        self.__profissionais.append(profissional)

    def excluir_profissional(self, profissional: Profissional) -> None:
        if profissional not in self.__profissionais:
            raise ValueError("O profissional não pertence a esta clínica.")
        self.__profissionais.remove(profissional)