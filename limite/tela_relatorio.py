class TelaRelatorio:

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
        print("-------- Relatórios ---------")
        print("Escolha sua opcao")
        print("1 - Clínicas com maior número de atendimentos")
        print("2 - Atendimentos mais caros e mais baratos")
        print("3 - Procedimentos mais realizados")
        print("4 - Procedimentos mais caros e mais baratos")
        print("0 - Retornar")
        opcao = self.le_numero_tela("Escolha a opcao:", [0, 1, 2, 3, 4])
        return opcao


    def mostra_relatorio(self, titulo, linhas):
        print("========", titulo, "========")
        for linha in linhas:
            print(linha)
        print("==========================================")


    def mostra_mensagem(self, mensagem):
        print(mensagem)