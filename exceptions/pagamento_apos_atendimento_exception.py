class PagamentoAposAtendimentoException(Exception):

    def __init__(self):
        super().__init__("Pagamento não pode ser feito após a data do atendimento")