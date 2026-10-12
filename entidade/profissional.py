from pessoa import Pessoa


class Profissional(Pessoa):
    """Especialização de Pessoa que representa um profissional."""

    def __init__(self, nome: str, celular: str, cpf: str,
                 especialidade: str, registro_profissional: str):
        super().__init__(nome, celular, cpf)
        self.__especialidade = especialidade
        self.__registro_profissional = registro_profissional

    @property
    def especialidade(self) -> str:
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade: str) -> None:
        self.__especialidade = especialidade

    @property
    def registro_profissional(self) -> str:
        return self.__registro_profissional

    @registro_profissional.setter
    def registro_profissional(self, registro_profissional: str) -> None:
        self.__registro_profissional = registro_profissional

# Exemplo de uso da classe Profissional
# profissional = Profissional(
#     nome = "Dr. João Souza",
#     celular = "(48) 97777-2222",
#     cpf = "987.654.321-00",
#     especialidade = "Cardiologia",
#     registro_profissional = "CRM-SC 12345"
# )
# print(profissional.nome, profissional.especialidade, profissional.registro_profissional)

# profissional.especialidade = "Clínica Geral"
# print(profissional.especialidade)