from datetime import date
from pessoa import Pessoa


class Paciente(Pessoa):
    """Especialização de Pessoa que representa um paciente."""

    def __init__(self, nome: str, celular: str, cpf: str,
                 data_nascimento: date, tem_responsavel: bool):
        super().__init__(nome, celular, cpf)
        self.__data_nascimento = data_nascimento
        self.__tem_responsavel = tem_responsavel

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date) -> None:
        self.__data_nascimento = data_nascimento

    @property
    def tem_responsavel(self) -> bool:
        return self.__tem_responsavel

    @tem_responsavel.setter
    def tem_responsavel(self, tem_responsavel: bool) -> None:
        self.__tem_responsavel = tem_responsavel


# Exemplo de uso da classe Paciente
# paciente = Paciente(
#     nome = "Maria Silva",
#     celular = "(48) 99999-0000",
#     cpf = "123.456.789-00",
#     data_nascimento = date(2010, 5, 20),
#     tem_responsavel = True,
# )
# print(paciente.nome, paciente.data_nascimento, paciente.tem_responsavel)

# paciente.celular = "(48) 98888-1111"
# print(paciente.celular)