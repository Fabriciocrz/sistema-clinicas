from datetime import date
from entidade.pagamento import Pagamento


class PagamentoPix(Pagamento):

    def __init__(self, data: date, valor_pago: float, codigo: int, cpf_pagador: str):
        super().__init__(data, valor_pago, codigo)
        self.__cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self) -> str:
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador: str) -> None:
        self.__cpf_pagador = cpf_pagador

    def modalidade(self) -> str:
        return "Pix"
