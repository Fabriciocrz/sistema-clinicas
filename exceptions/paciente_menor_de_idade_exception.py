class PacienteMenorDeIdadeException(Exception):
    """Paciente com menos de 18 anos na data do atendimento."""

    def __init__(self):
        super().__init__("Paciente menor de 18 anos sem responsável não pode ser atendido")
