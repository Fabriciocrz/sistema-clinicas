from entidade.pagamento import Pagamento
from entidade.atendimento import Atendimento
from entidade.pagamento_cartao import PagamentoCartao
from entidade.pagamento_dinheiro import PagamentoDinheiro
from entidade.pagamento_pix import PagamentoPix
from exceptions.pagamento_apos_atendimento_exception import PagamentoAposAtendimentoException
from limite.tela_pagamento import TelaPagamento

# Erros que o Model (Atendimento) lança quando uma regra é violada.
ERROS_DE_NEGOCIO = (PagamentoAposAtendimentoException, ValueError, TypeError)


class ControladorPagamento:
    """Controla os pagamentos. Não guarda lista própria: cada pagamento
    pertence a um Atendimento (agregação Atendimento 1 --- * Pagamento).
    As regras (data e valor) ficam em Atendimento."""

    def __init__(self, controlador_sistema):
        self.__tela_pagamento = TelaPagamento(self)
        self.__controlador_sistema = controlador_sistema

    def retornar(self) -> None:
        # O controle volta ao menu principal quando abre_tela() termina.
        pass

    def abre_tela(self) -> None:
        opcoes = {
            1: self.incluir_pagamento,
            2: self.alterar_pagamento,
            3: self.excluir_pagamento,
            4: self.listar_pagamentos,
        }
        while True:
            opcao = self.__tela_pagamento.mostra_tela_opcoes()
            if opcao == 0:
                self.retornar()
                return
            opcoes[opcao]()

    def incluir_pagamento(self) -> None:
        atendimento = self.__seleciona_atendimento()
        if atendimento is None:
            return

        if round(atendimento.valor_restante() * 100) <= 0:
            self.__tela_pagamento.mostra_mensagem("ATENÇÃO: este atendimento já está quitado.")
            return

        dados = self.__tela_pagamento.pega_dados_pagamento()
        if self.__codigo_em_uso(dados["codigo"]):
            self.__tela_pagamento.mostra_mensagem("ATENÇÃO: já existe um pagamento com esse código.")
            return

        try:
            atendimento.incluir_pagamento(self.__cria_pagamento(dados))
        except ERROS_DE_NEGOCIO as erro:
            self.__tela_pagamento.mostra_mensagem(f"ATENÇÃO: {erro}")
            return
        self.__tela_pagamento.mostra_mensagem("Pagamento incluído com sucesso.")
        self.__tela_pagamento.mostra_resumo(self.__resumo(atendimento))

    def alterar_pagamento(self) -> None:
        atendimento = self.__seleciona_atendimento()
        if atendimento is None:
            return
        pagamento = self.__seleciona_pagamento(atendimento)
        if pagamento is None:
            return

        dados = self.__tela_pagamento.pega_dados_pagamento()
        if self.__codigo_em_uso(dados["codigo"], ignorar=pagamento):
            self.__tela_pagamento.mostra_mensagem("ATENÇÃO: já existe um pagamento com esse código.")
            return

        # A modalidade pode mudar (ex.: Pix -> Cartão), então o objeto é
        # substituído; se o Model recusar, o pagamento antigo é mantido.
        try:
            atendimento.substituir_pagamento(pagamento.codigo, self.__cria_pagamento(dados))
        except ERROS_DE_NEGOCIO as erro:
            self.__tela_pagamento.mostra_mensagem(f"ATENÇÃO: {erro}")
            return
        self.__tela_pagamento.mostra_mensagem("Pagamento alterado com sucesso.")

    def excluir_pagamento(self) -> None:
        atendimento = self.__seleciona_atendimento()
        if atendimento is None:
            return
        pagamento = self.__seleciona_pagamento(atendimento)
        if pagamento is None:
            return

        try:
            atendimento.excluir_pagamento(pagamento.codigo)
        except ERROS_DE_NEGOCIO as erro:
            self.__tela_pagamento.mostra_mensagem(f"ATENÇÃO: {erro}")
            return
        self.__tela_pagamento.mostra_mensagem("Pagamento excluído com sucesso.")
        self.__tela_pagamento.mostra_resumo(self.__resumo(atendimento))

    def listar_pagamentos(self) -> None:
        atendimento = self.__seleciona_atendimento()
        if atendimento is None:
            return
        self.__lista_pagamentos_de(atendimento)
        self.__tela_pagamento.mostra_resumo(self.__resumo(atendimento))

    # --------------------------------------------------- métodos auxiliares

    def __seleciona_atendimento(self) -> Atendimento | None:
        """Lista os atendimentos, pede o código e devolve o atendimento (ou None)."""
        controlador_atendimento = self.__controlador_sistema.controlador_atendimento
        if not controlador_atendimento.atendimentos:
            self.__tela_pagamento.mostra_mensagem("Nenhum atendimento cadastrado.")
            return None
        controlador_atendimento.listar_atendimentos()
        atendimento = controlador_atendimento.pega_atendimento_por_codigo(
            self.__tela_pagamento.seleciona_atendimento())
        if atendimento is None:
            self.__tela_pagamento.mostra_mensagem("ATENÇÃO: atendimento não encontrado.")
        return atendimento

    def __seleciona_pagamento(self, atendimento: Atendimento) -> Pagamento | None:
        """Lista os pagamentos do atendimento, pede o código e devolve o pagamento (ou None)."""
        if not atendimento.pagamentos:
            self.__tela_pagamento.mostra_mensagem("Nenhum pagamento neste atendimento.")
            return None
        self.__lista_pagamentos_de(atendimento)
        codigo = self.__tela_pagamento.seleciona_pagamento()
        for pagamento in atendimento.pagamentos:
            if pagamento.codigo == codigo:
                return pagamento
        self.__tela_pagamento.mostra_mensagem("ATENÇÃO: pagamento não encontrado neste atendimento.")
        return None

    @staticmethod
    def __resumo(atendimento: Atendimento) -> dict:
        """Números puros para a tela formatar (o enunciado pede o paciente
        no registro do pagamento e o cálculo do valor restante)."""
        return {
            "codigo_atendimento": atendimento.codigo,
            "paciente": atendimento.paciente.nome,
            "valor_total": atendimento.valor_total(),
            "total_pago": atendimento.total_pago(),
            "valor_restante": atendimento.valor_restante(),
        }
    
    def __lista_pagamentos_de(self, atendimento: Atendimento) -> None:
        if not atendimento.pagamentos:
            self.__tela_pagamento.mostra_mensagem("Nenhum pagamento neste atendimento.")
            return
        for pagamento in atendimento.pagamentos:
            dados = {
                "codigo": pagamento.codigo,
                "modalidade": pagamento.modalidade(),   # polimorfismo
                "data": pagamento.data,
                "valor_pago": pagamento.valor_pago,
            }
            dados.update(pagamento.detalhes())          # polimorfismo, sem isinstance
            self.__tela_pagamento.mostra_pagamento(dados)

    def __codigo_em_uso(self, codigo: int, ignorar: Pagamento | None = None) -> bool:
        """O código do pagamento deve ser único no sistema inteiro (regra que
        envolve vários atendimentos, por isso fica no controlador que tem acesso a todos)."""
        for atendimento in self.__controlador_sistema.controlador_atendimento.atendimentos:
            for pagamento in atendimento.pagamentos:
                if pagamento.codigo == codigo and pagamento is not ignorar:
                    return True
        return False

    @staticmethod
    def __cria_pagamento(dados: dict) -> Pagamento:
        """Cria a subclasse concreta conforme a chave de modalidade
        ('dinheiro', 'cartao' ou 'pix') devolvida pela tela."""
        modalidade = dados["modalidade"]
        if modalidade == "cartao":
            return PagamentoCartao(dados["data"], dados["valor_pago"], dados["codigo"],
                                   dados["numero_cartao"], dados["bandeira"])
        if modalidade == "pix":
            return PagamentoPix(dados["data"], dados["valor_pago"], dados["codigo"],
                                dados["cpf_pagador"])
        if modalidade == "dinheiro":
            return PagamentoDinheiro(dados["data"], dados["valor_pago"], dados["codigo"])
        raise ValueError(f"Modalidade de pagamento desconhecida: {modalidade}")
