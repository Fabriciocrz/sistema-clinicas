from entidade.atendimento import Atendimento
from limite.tela_atendimento import TelaAtendimento
from exceptions.paciente_menor_de_idade_exception import PacienteMenorDeIdadeException
from exceptions.fora_do_horario_de_funcionamento_exception import ForaDoHorarioDeFuncionamentoException


class ControladorAtendimento:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__atendimentos = []
        self.__tela_atendimento = TelaAtendimento()

    @property
    def atendimentos(self) -> list:
        return self.__atendimentos

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_atendimento, 2: self.alterar_atendimento,
                        3: self.excluir_atendimento, 4: self.listar_atendimentos,
                        5: self.incluir_procedimento, 6: self.alterar_procedimento,
                        7: self.excluir_procedimento, 8: self.listar_procedimentos,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_atendimento.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def incluir_atendimento(self):
        dados = self.__tela_atendimento.pega_dados_atendimento()

        if self.pega_atendimento_por_codigo(dados["codigo"]) != None:
            self.__tela_atendimento.mostra_mensagem("já existe um atendimento com esse código")
            return

        paciente = self.__controlador_sistema.controlador_paciente.pega_paciente_por_cpf(dados["cpf_paciente"])
        profissional = self.__controlador_sistema.controlador_profissional.pega_profissional_por_cpf(dados["cpf_profissional"])
        clinica = self.__controlador_sistema.controlador_clinica.pega_clinica_por_codigo(dados["codigo_clinica"])
        tipo_atendimento = self.__controlador_sistema.controlador_tipo_atendimento.pega_tipo_atendimento_por_codigo(dados["codigo_tipo"])

        if paciente == None:
            self.__tela_atendimento.mostra_mensagem("Paciente não encontrado")
            return
        if profissional == None:
            self.__tela_atendimento.mostra_mensagem("Profissional não encontrado")
            return
        if clinica == None:
            self.__tela_atendimento.mostra_mensagem("Clínica não encontrada")
            return
        if tipo_atendimento == None:
            self.__tela_atendimento.mostra_mensagem("Tipo de atendimento não encontrado")
            return
        if dados["horario_inicio"] >= dados["horario_fim"]:
            self.__tela_atendimento.mostra_mensagem("O horário de início tem que ser antes do horário de fim")
            return

        try:
            nascimento = paciente.data_nascimento
            data = dados["data"]
            idade = data.year - nascimento.year
            if (data.month, data.day) < (nascimento.month, nascimento.day):
                idade = idade - 1
            if idade < 18 and not paciente.tem_responsavel:
                raise PacienteMenorDeIdadeException()

            if dados["horario_inicio"] < clinica.horario_abertura or dados["horario_fim"] > clinica.horario_fechamento:
                raise ForaDoHorarioDeFuncionamentoException()

        except PacienteMenorDeIdadeException as erro:
            self.__tela_atendimento.mostra_mensagem(str(erro))
            return
        except ForaDoHorarioDeFuncionamentoException as erro:
            self.__tela_atendimento.mostra_mensagem(str(erro))
            return

        atendimento = Atendimento(dados["data"], dados["horario_inicio"], dados["horario_fim"],
                                  dados["valor_base"], dados["codigo"], dados["numero_parcelas"],
                                  clinica, tipo_atendimento, profissional, paciente)
        self.__atendimentos.append(atendimento)
        self.__tela_atendimento.mostra_mensagem("Atendimento incluído")

    def alterar_atendimento(self):
        self.listar_atendimentos()
        codigo = self.__tela_atendimento.seleciona_atendimento()
        atendimento = self.pega_atendimento_por_codigo(codigo)

        if atendimento == None:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado")
            return

        dados = self.__tela_atendimento.pega_dados_atendimento()

        atendimento_com_mesmo_codigo = self.pega_atendimento_por_codigo(dados["codigo"])
        if atendimento_com_mesmo_codigo != None and atendimento_com_mesmo_codigo != atendimento:
            self.__tela_atendimento.mostra_mensagem("Já existe um atendimento com esse código")
            return

        paciente = self.__controlador_sistema.controlador_paciente.pega_paciente_por_cpf(dados["cpf_paciente"])
        profissional = self.__controlador_sistema.controlador_profissional.pega_profissional_por_cpf(dados["cpf_profissional"])
        clinica = self.__controlador_sistema.controlador_clinica.pega_clinica_por_codigo(dados["codigo_clinica"])
        tipo_atendimento = self.__controlador_sistema.controlador_tipo_atendimento.pega_tipo_atendimento_por_codigo(dados["codigo_tipo"])

        if paciente == None:
            self.__tela_atendimento.mostra_mensagem("Paciente não encontrado")
            return
        if profissional == None:
            self.__tela_atendimento.mostra_mensagem("Profissional não encontrado")
            return
        if clinica == None:
            self.__tela_atendimento.mostra_mensagem("Clínica não encontrada")
            return
        if tipo_atendimento == None:
            self.__tela_atendimento.mostra_mensagem("Tipo de atendimento não encontrado")
            return
        if dados["horario_inicio"] >= dados["horario_fim"]:
            self.__tela_atendimento.mostra_mensagem("O horário de início tem que ser antes do horário de fim")
            return
        if dados["numero_parcelas"] < len(atendimento.pagamentos):
            self.__tela_atendimento.mostra_mensagem("Já foram pagas mais parcelas do que esse número")
            return

        try:
            nascimento = paciente.data_nascimento
            data = dados["data"]
            idade = data.year - nascimento.year
            if (data.month, data.day) < (nascimento.month, nascimento.day):
                idade = idade - 1
            if idade < 18 and not paciente.tem_responsavel:
                raise PacienteMenorDeIdadeException()

            if dados["horario_inicio"] < clinica.horario_abertura or dados["horario_fim"] > clinica.horario_fechamento:
                raise ForaDoHorarioDeFuncionamentoException()

        except PacienteMenorDeIdadeException as erro:
            self.__tela_atendimento.mostra_mensagem(str(erro))
            return
        except ForaDoHorarioDeFuncionamentoException as erro:
            self.__tela_atendimento.mostra_mensagem(str(erro))
            return

        atendimento.codigo = dados["codigo"]
        atendimento.paciente = paciente
        atendimento.profissional = profissional
        atendimento.clinica = clinica
        atendimento.tipo_atendimento = tipo_atendimento
        atendimento.data = dados["data"]
        atendimento.horario_inicio = dados["horario_inicio"]
        atendimento.horario_fim = dados["horario_fim"]
        atendimento.valor_base = dados["valor_base"]
        atendimento.numero_parcelas = dados["numero_parcelas"]
        self.__tela_atendimento.mostra_mensagem("Atendimento alterado")

    def excluir_atendimento(self):
        self.listar_atendimentos()
        codigo = self.__tela_atendimento.seleciona_atendimento()
        atendimento = self.pega_atendimento_por_codigo(codigo)

        if atendimento == None:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado")
            return

        self.__atendimentos.remove(atendimento)
        self.__tela_atendimento.mostra_mensagem("Atendimento removido")

    def listar_atendimentos(self):
        if len(self.__atendimentos) == 0:
            self.__tela_atendimento.mostra_mensagem("Nenhum atendimento registrado")
            return

        for atendimento in self.__atendimentos:
            self.__tela_atendimento.mostra_atendimento({
                "codigo": atendimento.codigo,
                "data": atendimento.data.strftime("%d/%m/%Y"),
                "horario_inicio": atendimento.horario_inicio.strftime("%H:%M"),
                "horario_fim": atendimento.horario_fim.strftime("%H:%M"),
                "clinica": atendimento.clinica.nome,
                "paciente": atendimento.paciente.nome,
                "profissional": atendimento.profissional.nome,
                "tipo_atendimento": atendimento.tipo_atendimento.nome,
                "valor_total": atendimento.valor_total(),
                "total_pago": atendimento.total_pago(),
                "valor_restante": atendimento.valor_restante(),
                "parcelas_pagas": len(atendimento.pagamentos),
                "numero_parcelas": atendimento.numero_parcelas})

    def pega_atendimento_por_codigo(self, codigo: int) -> Atendimento:
        for atendimento in self.__atendimentos:
            if atendimento.codigo == codigo:
                return atendimento
        return None

    def incluir_procedimento(self):
        self.listar_atendimentos()
        codigo_atendimento = self.__tela_atendimento.seleciona_atendimento()
        atendimento = self.pega_atendimento_por_codigo(codigo_atendimento)

        if atendimento == None:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado")
            return

        dados = self.__tela_atendimento.pega_dados_procedimento()

        for procedimento in atendimento.procedimentos:
            if procedimento.codigo == dados["codigo"]:
                self.__tela_atendimento.mostra_mensagem("Já existe um procedimento com esse código nesse atendimento")
                return

        profissional = self.__controlador_sistema.controlador_profissional.pega_profissional_por_cpf(dados["cpf_profissional"])
        if profissional == None:
            self.__tela_atendimento.mostra_mensagem("Profissional não encontrado")
            return

        atendimento.incluir_procedimento(dados["descricao"], dados["custo"], dados["codigo"], profissional)
        self.__tela_atendimento.mostra_mensagem("Procedimento adicionado")

    def alterar_procedimento(self):
        codigo_atendimento = self.__tela_atendimento.seleciona_atendimento()
        atendimento = self.pega_atendimento_por_codigo(codigo_atendimento)

        if atendimento == None:
            self.__tela_atendimento.mostra_mensagem("atendimento não encontrado")
            return

        for procedimento in atendimento.procedimentos:
            dados = {"codigo": procedimento.codigo,
                     "descricao": procedimento.descricao,
                     "custo": procedimento.custo,
                     "profissional": procedimento.profissional.nome}
            self.__tela_atendimento.mostra_procedimento(dados)

        codigo = self.__tela_atendimento.seleciona_procedimento()
        procedimento_escolhido = None
        for procedimento in atendimento.procedimentos:
            if procedimento.codigo == codigo:
                procedimento_escolhido = procedimento

        if procedimento_escolhido == None:
            self.__tela_atendimento.mostra_mensagem("Procedimento não encontrado")
            return

        dados = self.__tela_atendimento.pega_dados_procedimento()

        for procedimento in atendimento.procedimentos:
            if procedimento.codigo == dados["codigo"] and procedimento != procedimento_escolhido:
                self.__tela_atendimento.mostra_mensagem("já existe um procedimento com esse código nesse atendimento")
                return

        profissional = self.__controlador_sistema.controlador_profissional.pega_profissional_por_cpf(dados["cpf_profissional"])
        if profissional == None:
            self.__tela_atendimento.mostra_mensagem("Profissional não encontrado")
            return

        procedimento_escolhido.codigo = dados["codigo"]
        procedimento_escolhido.descricao = dados["descricao"]
        procedimento_escolhido.custo = dados["custo"]
        procedimento_escolhido.profissional = profissional
        self.__tela_atendimento.mostra_mensagem("Procedimento alterado")

    def excluir_procedimento(self):
        codigo_atendimento = self.__tela_atendimento.seleciona_atendimento()
        atendimento = self.pega_atendimento_por_codigo(codigo_atendimento)

        if atendimento == None:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado")
            return

        for procedimento in atendimento.procedimentos:
            dados = {"codigo": procedimento.codigo,
                     "descricao": procedimento.descricao,
                     "custo": procedimento.custo,
                     "profissional": procedimento.profissional.nome}
            self.__tela_atendimento.mostra_procedimento(dados)

        codigo = self.__tela_atendimento.seleciona_procedimento()
        for procedimento in atendimento.procedimentos:
            if procedimento.codigo == codigo:
                atendimento.excluir_procedimento(codigo)
                self.__tela_atendimento.mostra_mensagem("Procedimento excluído")
                return
            
        self.__tela_atendimento.mostra_mensagem("procedimento não encontrado")

    def listar_procedimentos(self):
        codigo_atendimento = self.__tela_atendimento.seleciona_atendimento()
        atendimento = self.pega_atendimento_por_codigo(codigo_atendimento)

        if atendimento == None:
            self.__tela_atendimento.mostra_mensagem("Atendimento não encontrado")
            return

        if len(atendimento.procedimentos) == 0:
            self.__tela_atendimento.mostra_mensagem("Nenhum procedimento registrado nesse atendimento")
            return

        for procedimento in atendimento.procedimentos:
            dados = {"codigo": procedimento.codigo,
                     "descricao": procedimento.descricao,
                     "custo": procedimento.custo,
                     "profissional": procedimento.profissional.nome}
            self.__tela_atendimento.mostra_procedimento(dados)