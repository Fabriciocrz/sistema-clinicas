class ForaDoHorarioDeFuncionamentoException(Exception):

    def __init__(self):
        self.mensagem = "Não é possível agendar, a clínica está fechada nesse horário"
        super().__init__(self.mensagem)