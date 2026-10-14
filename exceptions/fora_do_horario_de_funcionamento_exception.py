class ForaDoHorarioDeFuncionamentoException(Exception):

    def __init__(self):
        super().__init__("Não é possivel agendar, a clinica está fechada nesse horário")