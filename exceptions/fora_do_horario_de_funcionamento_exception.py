class ForaDoHorarioDeFuncionamentoException(Exception):

    def __init__(self):
        super().__init__("Não é possível agendar, a clínica está fechada nesse horário")