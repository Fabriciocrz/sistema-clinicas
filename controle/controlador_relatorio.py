from limite.tela_relatorio import TelaRelatorio


class ControladorRelatorio:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorio()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.clinicas_com_mais_atendimentos, 2: self.atendimentos_mais_caros_e_baratos,
                        3: self.procedimentos_mais_realizados, 4: self.procedimentos_mais_caros_e_baratos,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_relatorio.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def clinicas_com_mais_atendimentos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos

        if len(atendimentos) == 0:
            self.__tela_relatorio.mostra_mensagem("Nenhum atendimento registrado")
            return

        contagem = {}
        for atendimento in atendimentos:
            nome_clinica = atendimento.clinica.nome
            if nome_clinica in contagem:
                contagem[nome_clinica] += 1
            else:
                contagem[nome_clinica] = 1

        maior_quantidade = 0
        for nome_clinica in contagem:
            if contagem[nome_clinica] > maior_quantidade:
                maior_quantidade = contagem[nome_clinica]

        linhas = []
        for nome_clinica in contagem:
            if contagem[nome_clinica] == maior_quantidade:
                linhas.append(f"Com mais atendimentos: {nome_clinica} ({maior_quantidade})")
        self.__tela_relatorio.mostra_relatorio("Clínicas com maior número de atendimentos", linhas)

    def atendimentos_mais_caros_e_baratos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos

        if len(atendimentos) == 0:
            self.__tela_relatorio.mostra_mensagem("Nenhum atendimento registrado")
            return

        mais_caro = atendimentos[0]
        mais_barato = atendimentos[0]

        for atendimento in atendimentos:
            if atendimento.valor_total() > mais_caro.valor_total():
                mais_caro = atendimento
            if atendimento.valor_total() < mais_barato.valor_total():
                mais_barato = atendimento

        linhas = []
        linhas.append(f"Mais caro: código {mais_caro.codigo} (R$ {mais_caro.valor_total():.2f})")
        linhas.append(f"Mais barato: código {mais_barato.codigo} (R$ {mais_barato.valor_total():.2f})")
        self.__tela_relatorio.mostra_relatorio("Atendimentos mais caros e mais baratos", linhas)

    def procedimentos_mais_realizados(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos

        contagem = {}
        for atendimento in atendimentos:
            for procedimento in atendimento.procedimentos:
                descricao = procedimento.descricao
                if descricao in contagem:
                    contagem[descricao] += 1
                else:
                    contagem[descricao] = 1

        if len(contagem) == 0:
            self.__tela_relatorio.mostra_mensagem("Nenhum procedimento registrado")
            return

        maior_quantidade = 0
        for descricao in contagem:
            if contagem[descricao] > maior_quantidade:
                maior_quantidade = contagem[descricao]

        linhas = []
        for descricao in contagem:
            if contagem[descricao] == maior_quantidade:
                linhas.append(f"Mais realizado: {descricao} ({maior_quantidade} vez(es))")
        self.__tela_relatorio.mostra_relatorio("Procedimentos mais realizados", linhas)

    def procedimentos_mais_caros_e_baratos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos

        procedimentos = []
        for atendimento in atendimentos:
            for procedimento in atendimento.procedimentos:
                procedimentos.append(procedimento)

        if len(procedimentos) == 0:
            self.__tela_relatorio.mostra_mensagem("Nenhum procedimento registrado")
            return

        mais_caro = procedimentos[0]
        mais_barato = procedimentos[0]
        for procedimento in procedimentos:
            if procedimento.custo > mais_caro.custo:
                mais_caro = procedimento
            if procedimento.custo < mais_barato.custo:
                mais_barato = procedimento

        linhas = []
        linhas.append(f"Mais caro: {mais_caro.descricao} (R$ {mais_caro.custo:.2f})")
        linhas.append(f"Mais barato: {mais_barato.descricao} (R$ {mais_barato.custo:.2f})")
        self.__tela_relatorio.mostra_relatorio("Procedimentos mais caros e mais baratos", linhas)