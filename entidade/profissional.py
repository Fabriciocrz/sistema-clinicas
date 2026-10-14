from entidade.pessoa import Pessoa


class Profissional(Pessoa):
    """Especialização de Pessoa que representa um profissional."""

    def __init__(self, nome: str, celular: str, cpf: str,
                 especialidade: str, registro_profissional: str):
        super().__init__(nome, celular, cpf)
        self.__especialidade = None
        self.__registro_profissional = None
        self.especialidade = especialidade
        self.registro_profissional = registro_profissional

    @property
    def especialidade(self) -> str:
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade: str) -> None:
        if isinstance(especialidade, str):
            self.__especialidade = especialidade

    @property
    def registro_profissional(self) -> str:
        return self.__registro_profissional

    @registro_profissional.setter
    def registro_profissional(self, registro_profissional: str) -> None:
        if isinstance(registro_profissional, str):
            self.__registro_profissional = registro_profissional
