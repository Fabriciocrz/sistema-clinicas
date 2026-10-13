
from datetime import date, datetime


class TelaPaciente:
    """Interface de console para as operações com pacientes."""

    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_tela_opcoes(self) -> int:
        print("\n-------- PACIENTES --------")
        print("1 - Incluir paciente")
        print("2 - Alterar paciente")
        print("3 - Excluir paciente")
        print("4 - Listar pacientes")
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

    def pega_dados_paciente(self) -> dict:
        print("\n-------- DADOS DO PACIENTE --------")
        nome = self.__le_texto("Nome: ")
        celular = self.__le_texto("Celular: ")
        cpf = self.__le_cpf("CPF: ")
        data_nascimento = self.__le_data("Data de nascimento (dd/mm/aaaa): ")
        tem_responsavel = self.__le_booleano("Tem responsável? (s/n): ")
        return {
            "nome": nome,
            "celular": celular,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "tem_responsavel": tem_responsavel,
        }

    def mostra_paciente(self, dados: dict) -> None:
        print("\nNome:", dados["nome"])
        print("Celular:", dados["celular"])
        print("CPF:", dados["cpf"])
        print("Data de nascimento:", dados["data_nascimento"].strftime("%d/%m/%Y"))
        print("Tem responsável:", "Sim" if dados["tem_responsavel"] else "Não")

    def mostra_mensagem(self, mensagem: str) -> None:
        print(f"\n{mensagem}")

    def seleciona_paciente(self) -> str:
        return self.__le_cpf("CPF do paciente: ")

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

    @staticmethod
    def __le_data(mensagem: str) -> date:
        while True:
            try:
                data = datetime.strptime(input(mensagem).strip(), "%d/%m/%Y").date()
                if data > date.today():
                    print("A data não pode estar no futuro.")
                    continue
                return data
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.")

    @staticmethod
    def __le_booleano(mensagem: str) -> bool:
        while True:
            resposta = input(mensagem).strip().lower()
            if resposta in ("s", "sim"):
                return True
            if resposta in ("n", "nao", "não"):
                return False
            print("Responda com 's' ou 'n'.")
