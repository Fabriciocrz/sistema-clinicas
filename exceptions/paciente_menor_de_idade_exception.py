class PacienteMenorDeIdadeException(Exception):

    def __init__(self):
        super().__init__("Paciente menor de 18 anos sem responsável não pode ser atendido")