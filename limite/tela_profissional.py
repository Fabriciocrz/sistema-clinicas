
class TelaProfissional:
    """Interface de console para as operações com profissionais."""

    def __init__(self, controlador):
        self.__controlador = controlador

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
        nome = self.__le_texto("Nome: ")
        celular = self.__le_texto("Celular: ")
        cpf = self.__le_cpf("CPF: ")
        especialidade = self.__le_texto("Especialidade: ")
        registro_profissional = self.__le_texto("Registro profissional: ")
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
        return self.__le_cpf("CPF do profissional: ")

    # ---------- métodos auxiliares de leitura/validação ----------

    @staticmethod
    def __le_texto(mensagem: str) -> str:
        while True:
            valor = input(mensagem).strip()
            if valor:
                return valor
            print("O valor não pode ser vazio.")

    @staticmethod
    def __le_cpf(mensagem: str) -> str:
        while True:
            cpf = input(mensagem).strip().replace(".", "").replace("-", "")
            if cpf.isdigit() and len(cpf) == 11:
                return cpf
            print("CPF inválido. Digite os 11 dígitos.")