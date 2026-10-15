from datetime import date, datetime
import math


class TelaPagamento:
    """Interface de console para as operações com pagamentos."""

    # Número do menu -> (chave neutra, nome exibido). A tela traduz a opção
    # do menu para a chave; o controlador só conhece as chaves.
    __MODALIDADES = {
        1: ("dinheiro", "Dinheiro"),
        2: ("cartao", "Cartão"),
        3: ("pix", "Pix"),
    }

    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_tela_opcoes(self) -> int:
        print("\n-------- PAGAMENTOS --------")
        print("1 - Incluir pagamento")
        print("2 - Alterar pagamento")
        print("3 - Excluir pagamento")
        print("4 - Listar pagamentos de um atendimento")
        print("0 - Retornar")
        return self.le_numero_tela("Escolha a opção: ", [0, 1, 2, 3, 4])

    def le_numero_tela(self, mensagem: str, numeros_validos: list | None = None) -> int:
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

    def pega_dados_pagamento(self) -> dict:
        print("\n-------- DADOS DO PAGAMENTO --------")
        modalidade = self.seleciona_modalidade()
        dados = {
            "modalidade": modalidade,
            "codigo": self.le_numero_tela("Código do pagamento: "),
            "data": self.__le_data("Data do pagamento (dd/mm/aaaa): "),
            "valor_pago": self.__le_valor("Valor pago: R$ "),
        }
        # Campos específicos de cada modalidade
        if modalidade == "cartao":
            dados["numero_cartao"] = input("Número do cartão: ")
            dados["bandeira"] = input("Bandeira: ")
        elif modalidade == "pix":
            dados["cpf_pagador"] = input("CPF do pagador: ").replace(".", "").replace("-", "")
        return dados

    def mostra_pagamento(self, dados: dict) -> None:
        print(f"\nCódigo: {dados['codigo']}")
        print(f"Modalidade: {dados['modalidade']}")
        print(f"Data: {dados['data'].strftime('%d/%m/%Y')}")
        print(f"Valor pago: R$ {dados['valor_pago']:.2f}")
        if "numero_cartao" in dados:
            # Por segurança, exibe só os 4 últimos dígitos do cartão.
            print(f"Cartão: **** **** **** {dados['numero_cartao'][-4:]} ({dados['bandeira']})")
        if "cpf_pagador" in dados:
            print(f"CPF do pagador: {dados['cpf_pagador']}")

    def mostra_resumo(self, dados: dict) -> None:
        """Situação financeira de um atendimento. Recebe números puros:
        formatar dinheiro é papel da tela, não do controlador."""
        print(f"\nAtendimento {dados['codigo_atendimento']} - Paciente: {dados['paciente']}")
        print(f"Total: R$ {dados['valor_total']:.2f} | "
              f"Pago: R$ {dados['total_pago']:.2f} | "
              f"Restante: R$ {dados['valor_restante']:.2f}")
        
    def mostra_mensagem(self, mensagem: str) -> None:
        print(f"\n{mensagem}")

    def seleciona_pagamento(self) -> int:
        return self.le_numero_tela("Código do pagamento: ")

    def seleciona_modalidade(self) -> str:
        print("Modalidades: " + " | ".join(
            f"{numero} - {nome}" for numero, (_, nome) in self.__MODALIDADES.items()))
        numero = self.le_numero_tela("Escolha a modalidade: ", list(self.__MODALIDADES))
        return self.__MODALIDADES[numero][0]

    def seleciona_atendimento(self) -> int:
        return self.le_numero_tela("Código do atendimento: ")

    # ---------- conversão de texto para data e valor (papel da tela) ----------

    def __le_data(self, mensagem: str) -> date:
        while True:
            try:
                return datetime.strptime(input(mensagem).strip(), "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.")

    def __le_valor(self, mensagem: str) -> float:
        """Aceita 150, 150.5, 150,50 e 1.500,50; recusa zero, negativos,
        'inf'/'nan' e mais de duas casas decimais."""
        while True:
            texto = input(mensagem).strip().replace("R$", "").replace(" ", "")
            if "," in texto:
                texto = texto.replace(".", "").replace(",", ".")
            try:
                valor = float(texto)
            except ValueError:
                valor = None
            if (valor is not None and math.isfinite(valor) and valor > 0
                    and round(valor, 2) == valor):
                return valor
            print("Valor inválido. Digite um valor maior que zero, com até 2 casas decimais.")

