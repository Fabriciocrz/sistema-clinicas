class TelaTipoAtendimento:

    def le_numero_tela(self, mensagem= " ", numeros_validos = None):
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
        print("-------- Tipo de Atendimento ---------")
        print("Escolha sua opcao")
        print("1 - Incluir Tipo de atendimento")
        print("2 - Alterar Tipo de atendimento")
        print("3 - Excluir Tipo de atendimento")
        print("4 - Listar Tipos de atendimento")
        print("0 - Retornar")
        opcao = self.le_numero_tela("Escolha a opcao:", [0,1,2,3,4])
        return opcao

    def pega_dados_tipo_atendimento(self):
        print ("-------- Dados do Tipo de Atendimento ---------")
        codigo = self.le_numero_tela("Código: ")
        nome = input("Nome: ")
        return {"codigo": codigo, "nome": nome}

    def mostra_tipo_atendimento(self, dados):
        print("Código:", dados["codigo"], "- Nome:", dados["nome"])

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def seleciona_tipo_atendimento(self):
        codigo = self.le_numero_tela("Código do tipo de atendimento: ")
        return codigo

