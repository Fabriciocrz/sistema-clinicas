from datetime import time


class TelaClinica:

    def mostra_tela_opcoes(self) -> int:
        print("\n-------- CLÍNICAS --------")
        print("1 - Incluir clínica")
        print("2 - Alterar clínica")
        print("3 - Excluir clínica")
        print("4 - Listar clínicas")
        print("5 - Vincular profissional")
        print("6 - Desvincular profissional")
        print("0 - Retornar")
        return self.le_numero_tela("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6])

    def pega_dados_clinica(self) -> dict:
        print("\n-------- DADOS DA CLÍNICA --------")
        nome = input("Nome: ")
        cidade = input("Cidade: ")
        descricao = input("Descrição: ")
        horario_abertura = self.__le_horario("Horário de abertura (HH:MM): ")
        horario_fechamento = self.__le_horario("Horário de fechamento (HH:MM): ")
        codigo = self.le_numero_tela("Código: ")
        return {
            "nome": nome,
            "cidade": cidade,
            "descricao": descricao,
            "horario_abertura": horario_abertura,
            "horario_fechamento": horario_fechamento,
            "codigo": codigo,
        }

    def mostra_clinica(self, dados: dict) -> None:
        print(f"\nCódigo: {dados['codigo']}")
        print(f"Nome: {dados['nome']}")
        print(f"Cidade: {dados['cidade']}")
        print(f"Descrição: {dados['descricao']}")
        print(f"Funcionamento: {dados['horario_abertura'].strftime('%H:%M')} às "
              f"{dados['horario_fechamento'].strftime('%H:%M')}")
        if "profissionais" in dados:
            nomes = [f"{p['nome']} (CPF {p['cpf']})" for p in dados["profissionais"]]
            print(f"Profissionais: {', '.join(nomes) or '-'}")

    def mostra_mensagem(self, mensagem: str) -> None:
        print(f"\n{mensagem}")

    def seleciona_clinica(self) -> int:
        return self.le_numero_tela("Código da clínica: ")

    def seleciona_profissional(self) -> str:
        return input("CPF do profissional: ").replace(".", "").replace("-", "")

    def le_numero_tela(self, mensagem: str, numeros_validos: list = None) -> int:
        while True:
            try:
                valor = int(input(mensagem))
                if numeros_validos and valor not in numeros_validos:
                    raise ValueError
                return valor
            except ValueError:
                print("Valor inválido.")
                if numeros_validos:
                    print("Opções disponíveis:", numeros_validos)

    # ---------- conversão de texto para horário (papel da tela) ----------

    def __le_horario(self, mensagem: str) -> time:
        while True:
            try:
                return time.fromisoformat(input(mensagem).strip())
            except ValueError:
                print("Horário inválido. Utilize o formato HH:MM.")