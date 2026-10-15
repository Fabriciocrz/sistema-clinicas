class PagamentoAposAtendimentoException(Exception):

    def __init__(self):
        self.mensagem = "Pagamento não pode ser feito após a data do atendimento"
        super().__init__(self.mensagem)