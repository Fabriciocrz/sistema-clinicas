class TelaSistema:

    def __init__(self, controlador):
        self.__controlador = controlador

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
        print("-------- Sistema inicial ---------")
        print("Escolha sua opcao")
        print("1 - Menu - Paciente")
        print("2 - Menu - Profissional")
        print("3 - Menu - Clinica")
        print("4 - Menu - Tipo de Atendimento")
        print("5 - Menu - Atendimento")
        print("6 - Menu - Pagamentos")
        print("7 - Menu - Relatórios")
        print("0 - Finalizar sistema")
        opcao = self.le_numero_tela("Escolha a opcao:", [0,1,2,3,4,5,6,7])
        return opcao
