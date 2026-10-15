class PacienteMenorDeIdadeException(Exception):

    def __init__(self):
        self.mensagem = "Paciente menor de 18 anos sem responsável não pode ser atendido"
        super().__init__(self.mensagem)