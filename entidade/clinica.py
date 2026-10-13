from datetime import time

from entidade.profissional import Profissional


class Clinica:
    """Clínica que agrega profissionais."""

    def __init__(self, nome: str, cidade: str, descricao: str,
                 horario_abertura: time, horario_fechamento: time, codigo: int):
        self.__nome = None
        self.__cidade = None
        self.__descricao = None
        self.__horario_abertura = None
        self.__horario_fechamento = None
        self.__codigo = None
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
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cidade(self) -> str:
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str) -> None:
        if isinstance(cidade, str):
            self.__cidade = cidade

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def horario_abertura(self) -> time:
        return self.__horario_abertura

    @horario_abertura.setter
    def horario_abertura(self, horario_abertura: time) -> None:
        if isinstance(horario_abertura, time):
            self.__horario_abertura = horario_abertura

    @property
    def horario_fechamento(self) -> time:
        return self.__horario_fechamento

    @horario_fechamento.setter
    def horario_fechamento(self, horario_fechamento: time) -> None:
        if isinstance(horario_fechamento, time):
            self.__horario_fechamento = horario_fechamento

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        if isinstance(codigo, int):
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
