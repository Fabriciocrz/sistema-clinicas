from datetime import date

from entidade.pagamento import Pagamento


class PagamentoPix(Pagamento):
    """Pagamento via Pix: guarda o CPF de quem pagou."""

    def __init__(self, data: date, valor_pago: float, codigo: int, cpf_pagador: str):
        super().__init__(data, valor_pago, codigo)
        self.__cpf_pagador = None
        self.cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self) -> str:
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador: str) -> None:
        if not isinstance(cpf_pagador, str):
            raise TypeError("O CPF do pagador deve ser texto.")
        if not (cpf_pagador.isdigit() and len(cpf_pagador) == 11):
            raise ValueError("O CPF do pagador deve ter 11 dígitos.")
        self.__cpf_pagador = cpf_pagador

    def modalidade(self) -> str:
        return "Pix"

    def detalhes(self) -> dict:
        return {"cpf_pagador": self.__cpf_pagador}
