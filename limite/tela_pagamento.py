from datetime import date, datetime
import math


class TelaPagamento:
    """Interface de console para as operações com pagamentos."""

    # Número do menu -> (chave neutra, nome exibido). A tela traduz a opção
    # do menu para a chave; o controlador só conhece as chaves.
    MODALIDADES = {
        1: ("dinheiro", "Dinheiro"),
        2: ("cartao", "Cartão"),
        3: ("pix", "Pix"),
    }

    # Número do menu -> nome da bandeira.
    BANDEIRAS = {
        1: "Visa",
        2: "Mastercard",
        3: "Elo",
        4: "American Express",
        5: "Outras",
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
            "codigo": self.__le_codigo("Código do pagamento: "),
            "data": self.__le_data("Data do pagamento (dd/mm/aaaa): "),
            "valor_pago": self.__le_valor("Valor pago: R$ "),
        }
        # Campos específicos de cada modalidade
        if modalidade == "cartao":
            dados["numero_cartao"] = self.__le_numero_cartao("Número do cartão: ")
            dados["bandeira"] = self.__le_bandeira()
        elif modalidade == "pix":
            dados["cpf_pagador"] = self.__le_cpf("CPF do pagador: ")
        return dados

    def mostra_pagamento(self, dados: dict) -> None:
        print(f"\nCódigo: {dados['codigo']}")
        print(f"Modalidade: {dados['modalidade']}")
        print(f"Data: {dados['data'].strftime('%d/%m/%Y')}")
        print(f"Valor pago: {self.__formata_moeda(dados['valor_pago'])}")
        if "numero_cartao" in dados:
            # Por segurança, exibe só os 4 últimos dígitos do cartão.
            print(f"Cartão: **** **** **** {dados['numero_cartao'][-4:]} ({dados['bandeira']})")
        if "cpf_pagador" in dados:
            print(f"CPF do pagador: {self.__formata_cpf(dados['cpf_pagador'])}")

    def mostra_resumo(self, dados: dict) -> None:
        """Situação financeira de um atendimento. Recebe números puros:
        formatar dinheiro é papel da tela, não do controlador."""
        print(f"\nAtendimento {dados['codigo_atendimento']} - Paciente: {dados['paciente']}")
        print(f"Total: {self.__formata_moeda(dados['valor_total'])} | "
              f"Pago: {self.__formata_moeda(dados['total_pago'])} | "
              f"Restante: {self.__formata_moeda(dados['valor_restante'])}")
        
    def mostra_mensagem(self, mensagem: str) -> None:
        print(f"\n{mensagem}")

    def seleciona_pagamento(self) -> int:
        return self.__le_codigo("Código do pagamento: ")

    def seleciona_modalidade(self) -> str:
        print("Modalidades: " + " | ".join(
            f"{numero} - {nome}" for numero, (_, nome) in self.MODALIDADES.items()))
        numero = self.le_numero_tela("Escolha a modalidade: ", list(self.MODALIDADES))
        return self.MODALIDADES[numero][0]

    def seleciona_atendimento(self) -> int:
        return self.__le_codigo("Código do atendimento: ")

    # ---------- métodos auxiliares de leitura/validação ----------

    def __le_codigo(self, mensagem: str) -> int:
        while True:
            codigo = self.le_numero_tela(mensagem)
            if codigo > 0:
                return codigo
            print("O código deve ser um número positivo.")

    def __le_bandeira(self) -> str:
        print("Bandeiras: " + " | ".join(f"{numero} - {nome}" for numero, nome in self.BANDEIRAS.items()))
        numero = self.le_numero_tela("Escolha a bandeira: ", list(self.BANDEIRAS))
        return self.BANDEIRAS[numero]

    @staticmethod
    def __le_data(mensagem: str) -> date:
        while True:
            try:
                return datetime.strptime(input(mensagem).strip(), "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.")

    @staticmethod
    def __le_valor(mensagem: str) -> float:
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

    @staticmethod
    def __le_cpf(mensagem: str) -> str:
        while True:
            cpf = input(mensagem).strip().replace(".", "").replace("-", "")
            if cpf.isdigit() and len(cpf) == 11:
                return cpf
            print("CPF inválido. Digite os 11 dígitos.")

    @staticmethod
    def __le_numero_cartao(mensagem: str) -> str:
        while True:
            numero = input(mensagem).strip().replace(" ", "").replace("-", "")
            if numero.isdigit() and 13 <= len(numero) <= 19:
                return numero
            print("Número de cartão inválido. Digite de 13 a 19 dígitos.")

    # ---------- métodos auxiliares de formatação ----------

    @staticmethod
    def __formata_moeda(valor: float) -> str:
        # 1234.5 -> "R$ 1.234,50"
        texto = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return f"R$ {texto}"

    @staticmethod
    def __formata_cpf(cpf: str) -> str:
        # "12345678900" -> "123.456.789-00"
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
