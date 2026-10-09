class PacienteMenorDeIdadeException(Exception):
    """Paciente com menos de 18 anos na data do atendimento."""

    def __init__(self, mensagem: str = "Paciente com menos de 18 anos na data do atendimento."):
        super().__init__(mensagem)
