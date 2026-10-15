
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
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ").replace(".", "").replace("-", "")
        data_nascimento = self.__le_data("Data de nascimento (dd/mm/aaaa): ")
        tem_responsavel = input("Tem responsável? (s/n): ").strip().lower() == "s"
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
        return input("CPF do paciente: ").replace(".", "").replace("-", "")

    # ---------- conversão de texto para data (papel da tela) ----------

    def __le_data(self, mensagem: str) -> date:
        while True:
            try:
                return datetime.strptime(input(mensagem).strip(), "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.")
