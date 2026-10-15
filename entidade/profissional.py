from entidade.pessoa import Pessoa


class Profissional(Pessoa):
    """Especialização de Pessoa que representa um profissional."""

    def __init__(self, nome: str, celular: str, cpf: str,
                 especialidade: str, registro_profissional: str):
        super().__init__(nome, celular, cpf)
        self.especialidade = especialidade
        self.registro_profissional = registro_profissional

    @property
    def especialidade(self) -> str:
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade: str) -> None:
        if not isinstance(especialidade, str):
            raise TypeError("A especialidade deve ser texto.")
        if not especialidade.strip():
            raise ValueError("A especialidade é obrigatória.")
        self.__especialidade = especialidade.strip()

    @property
    def registro_profissional(self) -> str:
        return self.__registro_profissional

    @registro_profissional.setter
    def registro_profissional(self, registro_profissional: str) -> None:
        if not isinstance(registro_profissional, str):
            raise TypeError("O registro profissional deve ser texto.")
        if not registro_profissional.strip():
            raise ValueError("O registro profissional é obrigatório.")
        self.__registro_profissional = registro_profissional.strip()
