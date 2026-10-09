from datetime import time


class Clinica:
    def __init__(self, nome: str, cidade: str, descricao: str,
                 horario_abertura: time, horario_fechamento: time,
                 codigo: int):
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento
        self.__codigo = codigo
        self.__profissionais = []

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def cidade(self) -> str:
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str) -> None:
        self.__cidade = cidade

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        self.__descricao = descricao

    @property
    def horario_abertura(self) -> time:
        return self.__horario_abertura

    @horario_abertura.setter
    def horario_abertura(self, horario_abertura: time) -> None:
        self.__horario_abertura = horario_abertura

    @property
    def horario_fechamento(self) -> time:
        return self.__horario_fechamento

    @horario_fechamento.setter
    def horario_fechamento(self, horario_fechamento: time) -> None:
        self.__horario_fechamento = horario_fechamento

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        self.__codigo = codigo

    def profissionais(self) -> list:
        return self.__profissionais

    def incluir_profissional(self, profissional: "Profissional") -> None:
        if profissional not in self.__profissionais:
            self.__profissionais.append(profissional)

    def excluir_profissional(self, profissional: "Profissional") -> None:
        if profissional in self.__profissionais:
            self.__profissionais.remove(profissional)
