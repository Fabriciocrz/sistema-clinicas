from abc import ABC, abstractmethod


class Pessoa(ABC):
    """Dados comuns a pacientes e profissionais. Os setters garantem que
    nenhuma pessoa fique com dado obrigatório vazio ou de tipo errado."""

    @abstractmethod
    def __init__(self, nome: str, celular: str, cpf: str):
        self.nome = nome
        self.celular = celular
        self.cpf = cpf

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser texto.")
        if not nome.strip():
            raise ValueError("O nome é obrigatório.")
        self.__nome = nome.strip()

    @property
    def celular(self) -> str:
        return self.__celular

    @celular.setter
    def celular(self, celular: str) -> None:
        if not isinstance(celular, str):
            raise TypeError("O celular deve ser texto.")
        if not celular.strip():
            raise ValueError("O celular é obrigatório.")
        self.__celular = celular.strip()

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str) -> None:
        if not isinstance(cpf, str):
            raise TypeError("O CPF deve ser texto.")
        cpf = cpf.strip()
        if not (cpf.isdigit() and len(cpf) == 11):
            raise ValueError("O CPF deve ter 11 dígitos.")
        self.__cpf = cpf
