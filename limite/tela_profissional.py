
class TelaProfissional:
    
    def mostra_tela_opcoes(self) -> int:
        print("\n------- PROFISSIONAIS -------")
        print("1 - Incluir profissional")
        print("2 - Alterar profissional")
        print("3 - Excluir profissional")
        print("4 - Listar profissionais")
        print("0 - Retornar")
        return self.le_numero_tela("Escolha a opção: ", [0, 1, 2, 3, 4])

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

    def pega_dados_profissional(self) -> dict:
        print("\n------- DADOS DO PROFISSIONAL -------")
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ").replace(".", "").replace("-", "")
        especialidade = input("Especialidade: ")
        registro_profissional = input("Registro profissional: ")
        return {
            "nome": nome,
            "celular": celular,
            "cpf": cpf,
            "especialidade": especialidade,
            "registro_profissional": registro_profissional,
        }

    def mostra_profissional(self, dados: dict) -> None:
        print(f"Nome:                  {dados['nome']}")
        print(f"CPF:                   {dados['cpf']}")
        print(f"Celular:               {dados['celular']}")
        print(f"Especialidade:         {dados['especialidade']}")
        print(f"Registro profissional: {dados['registro_profissional']}")
        print("-" * 40)

    def mostra_mensagem(self, mensagem: str) -> None:
        print(f"\n{mensagem}")

    def seleciona_profissional(self) -> str:
        return input("CPF do profissional: ").replace(".", "").replace("-", "")