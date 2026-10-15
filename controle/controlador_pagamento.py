from entidade.pagamento_cartao import PagamentoCartao
from entidade.pagamento_dinheiro import PagamentoDinheiro
from entidade.pagamento_pix import PagamentoPix
from exceptions.pagamento_apos_atendimento_exception import PagamentoAposAtendimentoException
from limite.tela_pagamento import TelaPagamento


class ControladorPagamento:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pagamento = TelaPagamento(self)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_pagamento, 2: self.alterar_pagamento,
                        3: self.excluir_pagamento, 4: self.listar_pagamentos,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_pagamento.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def incluir_pagamento(self):
        self.__controlador_sistema.controlador_atendimento.listar_atendimentos()
        codigo_atendimento = self.__tela_pagamento.seleciona_atendimento()
        atendimento = self.__controlador_sistema.controlador_atendimento.pega_atendimento_por_codigo(codigo_atendimento)

        if atendimento == None:
            self.__tela_pagamento.mostra_mensagem("Atendimento não encontrado")
            return

        if len(atendimento.pagamentos) >= atendimento.numero_parcelas:
            self.__tela_pagamento.mostra_mensagem("Todas as parcelas desse atendimento já foram pagas")
            return

        dados = self.__tela_pagamento.pega_dados_pagamento()

        for pagamento in atendimento.pagamentos:
            if pagamento.codigo == dados["codigo"]:
                self.__tela_pagamento.mostra_mensagem("Já existe um pagamento com esse código nesse atendimento")
                return

        try:
            if dados["data"] > atendimento.data:
                raise PagamentoAposAtendimentoException()
        except PagamentoAposAtendimentoException as erro:
            self.__tela_pagamento.mostra_mensagem(str(erro))
            return

        valor = atendimento.valor_parcela()

        if dados["modalidade"] == 1:
            pagamento = PagamentoDinheiro(dados["data"], valor, dados["codigo"])
        elif dados["modalidade"] == 2:
            pagamento = PagamentoCartao(dados["data"], valor, dados["codigo"], dados["numero_cartao"], dados["bandeira"])
        else:
            pagamento = PagamentoPix(dados["data"], valor, dados["codigo"], dados["cpf_pagador"])

        atendimento.incluir_pagamento(pagamento)
        self.__tela_pagamento.mostra_mensagem(f"Pagamento de R$ {valor:.2f} incluído. Restante: R$ {atendimento.valor_restante():.2f}")

    def alterar_pagamento(self):
        self.__controlador_sistema.controlador_atendimento.listar_atendimentos()
        codigo_atendimento = self.__tela_pagamento.seleciona_atendimento()
        atendimento = self.__controlador_sistema.controlador_atendimento.pega_atendimento_por_codigo(codigo_atendimento)

        if atendimento == None:
            self.__tela_pagamento.mostra_mensagem("Atendimento não encontrado")
            return

        for pagamento in atendimento.pagamentos:
            self.__tela_pagamento.mostra_pagamento({"codigo": pagamento.codigo, "modalidade": pagamento.modalidade(),
                                                    "data": pagamento.data.strftime("%d/%m/%Y"), "valor_pago": pagamento.valor_pago})

        codigo = self.__tela_pagamento.seleciona_pagamento()
        pagamento_escolhido = None
        for pagamento in atendimento.pagamentos:
            if pagamento.codigo == codigo:
                pagamento_escolhido = pagamento

        if pagamento_escolhido == None:
            self.__tela_pagamento.mostra_mensagem("Pagamento não encontrado")
            return

        dados = self.__tela_pagamento.pega_dados_pagamento()

        for pagamento in atendimento.pagamentos:
            if pagamento.codigo == dados["codigo"] and pagamento != pagamento_escolhido:
                self.__tela_pagamento.mostra_mensagem("Já existe um pagamento com esse código nesse atendimento")
                return

        try:
            if dados["data"] > atendimento.data:
                raise PagamentoAposAtendimentoException()
        except PagamentoAposAtendimentoException as erro:
            self.__tela_pagamento.mostra_mensagem(str(erro))
            return

        valor = pagamento_escolhido.valor_pago

        if dados["modalidade"] == 1:
            novo_pagamento = PagamentoDinheiro(dados["data"], valor, dados["codigo"])
        elif dados["modalidade"] == 2:
            novo_pagamento = PagamentoCartao(dados["data"], valor, dados["codigo"], dados["numero_cartao"], dados["bandeira"])
        else:
            novo_pagamento = PagamentoPix(dados["data"], valor, dados["codigo"], dados["cpf_pagador"])

        atendimento.excluir_pagamento(pagamento_escolhido.codigo)
        atendimento.incluir_pagamento(novo_pagamento)
        self.__tela_pagamento.mostra_mensagem("Pagamento alterado")

    def excluir_pagamento(self):
        self.__controlador_sistema.controlador_atendimento.listar_atendimentos()
        codigo_atendimento = self.__tela_pagamento.seleciona_atendimento()
        atendimento = self.__controlador_sistema.controlador_atendimento.pega_atendimento_por_codigo(codigo_atendimento)

        if atendimento == None:
            self.__tela_pagamento.mostra_mensagem("Atendimento não encontrado")
            return

        for pagamento in atendimento.pagamentos:
            self.__tela_pagamento.mostra_pagamento({"codigo": pagamento.codigo, "modalidade": pagamento.modalidade(),
                                                    "data": pagamento.data.strftime("%d/%m/%Y"), "valor_pago": pagamento.valor_pago})

        codigo = self.__tela_pagamento.seleciona_pagamento()
        for pagamento in atendimento.pagamentos:
            if pagamento.codigo == codigo:
                atendimento.excluir_pagamento(codigo)
                self.__tela_pagamento.mostra_mensagem("Pagamento excluído")
                return

        self.__tela_pagamento.mostra_mensagem("Pagamento não encontrado")

    def listar_pagamentos(self):
        self.__controlador_sistema.controlador_atendimento.listar_atendimentos()
        codigo_atendimento = self.__tela_pagamento.seleciona_atendimento()
        atendimento = self.__controlador_sistema.controlador_atendimento.pega_atendimento_por_codigo(codigo_atendimento)

        if atendimento == None:
            self.__tela_pagamento.mostra_mensagem("Atendimento não encontrado")
            return

        if len(atendimento.pagamentos) == 0:
            self.__tela_pagamento.mostra_mensagem("Nenhum pagamento registrado nesse atendimento")
            return

        for pagamento in atendimento.pagamentos:
            self.__tela_pagamento.mostra_pagamento({"codigo": pagamento.codigo, "modalidade": pagamento.modalidade(),
                                                    "data": pagamento.data.strftime("%d/%m/%Y"), "valor_pago": pagamento.valor_pago})
