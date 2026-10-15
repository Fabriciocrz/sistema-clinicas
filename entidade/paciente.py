from datetime import date

from entidade.pessoa import Pessoa


class Paciente(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str,
                 data_nascimento: date, tem_responsavel: bool):
        super().__init__(nome, celular, cpf)
        self.data_nascimento = data_nascimento
        self.tem_responsavel = tem_responsavel

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date) -> None:
        if not isinstance(data_nascimento, date):
            raise TypeError("A data de nascimento deve ser do tipo date.")
        if data_nascimento > date.today():
            raise ValueError("A data de nascimento não pode estar no futuro.")
        self.__data_nascimento = data_nascimento

    @property
    def tem_responsavel(self) -> bool:
        return self.__tem_responsavel

    @tem_responsavel.setter
    def tem_responsavel(self, tem_responsavel: bool) -> None:
        if not isinstance(tem_responsavel, bool):
            raise TypeError("Tem responsável deve ser verdadeiro ou falso.")
        self.__tem_responsavel = tem_responsavel
