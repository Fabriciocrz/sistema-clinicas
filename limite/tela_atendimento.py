from datetime import date, datetime, time


class TelaAtendimento:

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
        print("-------- Atendimentos ---------")
        print("Escolha sua opcao")
        print("1 - Incluir atendimento")
        print("2 - Alterar atendimento")
        print("3 - Excluir atendimento")
        print("4 - Listar atendimentos")
        print("5 - Incluir procedimento em um atendimento")
        print("6 - Alterar procedimento de um atendimento")
        print("7 - Excluir procedimento de um atendimento")
        print("8 - Listar procedimentos de um atendimento")
        print("0 - Retornar")
        opcao = self.le_numero_tela("Escolha a opcao:", [0,1,2,3,4,5,6,7,8])
        return opcao


    def pega_dados_atendimento(self):
        codigo = self.le_numero_tela("Código do atendimento: ")
        cpf_paciente = input("CPF do paciente: ").replace(".", "").replace("-", "")
        cpf_profissional = input("CPF do profissional: ").replace(".", "").replace("-", "")
        codigo_clinica = self.le_numero_tela("Código da clínica: ")
        codigo_tipo = self.le_numero_tela("Código do tipo de atendimento: ")
        data = self.__le_data("Data (dd/mm/aaaa): ")
        horario_inicio = self.__le_horario("Horário de início (HH:MM): ")
        horario_fim = self.__le_horario("Horário de fim (HH:MM): ")
        valor_base = self.__le_valor("Valor base (R$): ")
        numero_parcelas = self.le_numero_tela("Número de parcelas (1 até 12): ", list(range(1,13)))
        return {"codigo": codigo,
                "cpf_paciente": cpf_paciente,
                "cpf_profissional": cpf_profissional,
                "codigo_clinica": codigo_clinica,
                "codigo_tipo": codigo_tipo,
                "data": data,
                "horario_inicio": horario_inicio,
                "horario_fim": horario_fim,
                "valor_base": valor_base,
                "numero_parcelas": numero_parcelas}


    def mostra_atendimento(self,dados):
        print("----------------------------------------")
        print("Código:", dados["codigo"])
        print("Data:", dados["data"], "das", dados["horario_inicio"], "às", dados["horario_fim"])
        print("Clínica:", dados["clinica"])
        print("Paciente:", dados["paciente"])
        print("Profissional:", dados["profissional"])
        print("Tipo:", dados["tipo_atendimento"])
        print("Valor total: R$", dados["valor_total"])
        print("Pago: R$", dados["total_pago"], "- Restante: R$", dados["valor_restante"])
        print("Parcelas:", dados["parcelas_pagas"], "de", dados["numero_parcelas"])
 

    def mostra_mensagem(self, mensagem):
        print(mensagem)


    def seleciona_atendimento(self):
        codigo = self.le_numero_tela("Código do atendimento: ")
        return codigo


    def pega_dados_procedimento(self):
        print("-------- Dados do Procedimento ---------")
        codigo = self.le_numero_tela("Código do procedimento: ")
        descricao = input("Descrição: ")
        custo = self.__le_valor("Custo (R$): ")
        cpf_profissional = input("CPF do profissional responsável: ").replace(".", "").replace("-", "")
        return {"codigo": codigo,
                "descricao": descricao,
                "custo": custo,
                "cpf_profissional": cpf_profissional}

 
    def mostra_procedimento(self, dados):
        print("----------------------------------------")
        print ("Código:", dados["codigo"])
        print ("Descrição", dados["descricao"])
        print("Custo: R$", dados["custo"])
        print("Profissional:", dados["profissional"])

 
    def seleciona_procedimento(self):
        codigo = self.le_numero_tela("Código do procedimento: ")
        return codigo


    def __le_data(self, mensagem):
        while True:
            try:
                return datetime.strptime(input(mensagem).strip(), "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.")

 
    def __le_horario(self, mensagem):
        while True:
            try:
                return time.fromisoformat(input(mensagem).strip())
            except ValueError:
                print("Horário inválido. Use o formato HH:MM.")

 
    def __le_valor(self, mensagem):
        while True:
            try:
                return float(input(mensagem).strip().replace(",", "."))
            except ValueError:
                print("Valor inválido. Digite um número, ex.: 150,00")