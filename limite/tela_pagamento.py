from datetime import datetime


class TelaPagamento:

    def __init__(self, controlador):
        self.__controlador = controlador

    def le_numero_tela(self, mensagem=" ", numeros_validos=None):
        while True:
            valor_registrado = input(mensagem)
            try:
                valor_int = int(valor_registrado)
                if numeros_validos and valor_int not in numeros_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor Incorreto - Verifique as opções disponíveis")
                if numeros_validos:
                    print("Opções disponíveis: ", numeros_validos)

    def mostra_tela_opcoes(self):
        print("-------- Pagamentos ---------")
        print("Escolha sua opcao")
        print("1 - Incluir pagamento")
        print("2 - Alterar pagamento")
        print("3 - Excluir pagamento")
        print("4 - Listar pagamentos de um atendimento")
        print("0 - Retornar")
        opcao = self.le_numero_tela("Escolha a opcao:", [0, 1, 2, 3, 4])
        return opcao

    def seleciona_modalidade(self):
        print("1 - Dinheiro")
        print("2 - Cartão")
        print("3 - Pix")
        modalidade = self.le_numero_tela("Modalidade: ", [1, 2, 3])
        return modalidade

    def pega_dados_pagamento(self):
        print("-------- Dados do Pagamento ---------")
        modalidade = self.seleciona_modalidade()
        codigo = self.le_numero_tela("Código do pagamento: ")
        data = self.__le_data("Data do pagamento (dd/mm/aaaa): ")
        dados = {"modalidade": modalidade, "codigo": codigo, "data": data}
        if modalidade == 2:
            dados["numero_cartao"] = input("Número do cartão: ")
            dados["bandeira"] = input("Bandeira: ")
        if modalidade == 3:
            dados["cpf_pagador"] = input("CPF do pagador: ").replace(".", "").replace("-", "")
        return dados

    def mostra_pagamento(self, dados):
        print("----------------------------------------")
        print("Código:", dados["codigo"])
        print("Modalidade:", dados["modalidade"])
        print("Data:", dados["data"])
        print(f"Valor pago: R$ {dados['valor_pago']:.2f}")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def seleciona_atendimento(self):
        codigo = self.le_numero_tela("Código do atendimento: ")
        return codigo

    def seleciona_pagamento(self):
        codigo = self.le_numero_tela("Código do pagamento: ")
        return codigo

    def __le_data(self, mensagem):
        while True:
            try:
                return datetime.strptime(input(mensagem).strip(), "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.")
