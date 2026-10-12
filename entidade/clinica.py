from datetime import time
from profissional import Profissional


class Clinica:
    """Clínica que agrega profissionais."""

    def __init__(self, nome: str, cidade: str, descricao: str,
                 horario_abertura: time, horario_fechamento: time, codigo: int):
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento
        self.__codigo = codigo
        self.__profissionais: list[Profissional] = []

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

    @property
    def profissionais(self) -> list:
        # Somente leitura para que a lista interna só seja alterada por incluir/excluir.
        return list(self.__profissionais)

    def incluir_profissional(self, profissional: Profissional) -> None:
        if not isinstance(profissional, Profissional):
            raise TypeError("O objeto informado não é um Profissional.")
        if profissional not in self.__profissionais:
            self.__profissionais.append(profissional)

    def excluir_profissional(self, profissional: Profissional) -> None:
        if profissional not in self.__profissionais:
            raise ValueError("O profissional não pertence a esta clínica.")
        self.__profissionais.remove(profissional)

#criando uma instância de Clinica para testes
# clinica = Clinica(
#     nome = "Clínica Vida",
#     cidade = "Florianópolis",
#     descricao = "Clínica geral e especialidades",
#     horario_abertura = time(8, 0),
#     horario_fechamento = time(7, 0),
#     codigo = 1,
# )

#instanciando profissionais e testando inclusão e exclusão de profissionais na clínica
# p1 = Profissional("Dr. João Souza", "(48) 97777-2222", "987.654.321-00",
#                       "Cardiologia", "CRM-SC 12345")
# p2 = Profissional("Dra. Ana Lima", "(48) 96666-3333", "111.222.333-44",
#                       "Dermatologia", "CRM-SC 67890")

# clinica.incluir_profissional(p1)
# clinica.incluir_profissional(p2)
# print([p.nome for p in clinica.profissionais])

# clinica.excluir_profissional(p1)
# print([p.nome for p in clinica.profissionais])