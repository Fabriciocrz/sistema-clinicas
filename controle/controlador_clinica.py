from limite.tela_clinica import TelaClinica
from entidade.clinica import Clinica


class ControladorClinica:
    """Controla as operações de cadastro de clínicas e o vínculo com profissionais."""

    def __init__(self, controlador_sistema):
        self.__clinicas: list[Clinica] = []
        self.__tela_clinica = TelaClinica(self)
        self.__controlador_sistema = controlador_sistema

    @property
    def clinicas(self) -> list[Clinica]:
        # Usado por ControladorProfissional (exclusão) e ControladorRelatorio.
        return list(self.__clinicas)

    def retornar(self) -> None:
        # O controle volta ao menu principal quando abre_tela() termina.
        pass

    def abre_tela(self) -> None:
        opcoes = {
            1: self.incluir_clinica,
            2: self.alterar_clinica,
            3: self.excluir_clinica,
            4: self.listar_clinicas,
            5: self.vincular_profissional,
            6: self.desvincular_profissional,
        }
        while True:
            opcao = self.__tela_clinica.mostra_tela_opcoes()
            if opcao == 0:
                self.retornar()
                return
            opcoes[opcao]()

    def incluir_clinica(self) -> None:
        dados = self.__tela_clinica.pega_dados_clinica()

        if self.pega_clinica_por_codigo(dados["codigo"]) is not None:
            self.__tela_clinica.mostra_mensagem("ATENÇÃO: já existe clínica com esse código!")
            return

        # Qualquer par de horários é aceito: abrir às 18:00 e fechar às 08:00
        # significa que a clínica funciona durante a noite.
        try:
            clinica = Clinica(**dados)            # a entidade valida cada campo
        except ValueError as erro:
            self.__tela_clinica.mostra_mensagem(f"ATENÇÃO: {erro}")
            return
        self.__clinicas.append(clinica)
        self.__tela_clinica.mostra_mensagem("Clínica incluída com sucesso!")

    def alterar_clinica(self) -> None:
        clinica = self.__seleciona_clinica()
        if clinica is None:
            return

        novos_dados = self.__tela_clinica.pega_dados_clinica()

        outra = self.pega_clinica_por_codigo(novos_dados["codigo"])
        if outra is not None and outra is not clinica:
            self.__tela_clinica.mostra_mensagem(
                "ATENÇÃO: já existe outra clínica com esse código!")
            return

        # Uma clínica provisória valida os campos e, com a regra do Model
        # (esta_aberta), confere se os atendimentos já marcados continuam
        # dentro do novo horário. A clínica real só muda se tudo estiver certo.
        try:
            nova = Clinica(**novos_dados)
        except ValueError as erro:
            self.__tela_clinica.mostra_mensagem(f"ATENÇÃO: {erro}")
            return
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if any(atendimento.clinica is clinica
               and not nova.esta_aberta(atendimento.horario_inicio, atendimento.horario_fim)
               for atendimento in atendimentos):
            self.__tela_clinica.mostra_mensagem(
                "ATENÇÃO: há atendimentos fora do novo horário de funcionamento.")
            return

        clinica.nome = nova.nome
        clinica.cidade = nova.cidade
        clinica.descricao = nova.descricao
        clinica.horario_abertura = nova.horario_abertura
        clinica.horario_fechamento = nova.horario_fechamento
        clinica.codigo = nova.codigo
        self.__tela_clinica.mostra_mensagem("Clínica alterada com sucesso!")

    def excluir_clinica(self) -> None:
        clinica = self.__seleciona_clinica()
        if clinica is None:
            return

        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if any(atendimento.clinica is clinica for atendimento in atendimentos):
            self.__tela_clinica.mostra_mensagem(
                "ATENÇÃO: não é possível excluir uma clínica que possui atendimentos.")
            return

        self.__clinicas.remove(clinica)
        self.__tela_clinica.mostra_mensagem("Clínica excluída com sucesso!")

    def listar_clinicas(self) -> None:
        if not self.__clinicas:
            self.__tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
            return

        for clinica in self.__clinicas:
            # Os horários vão como objetos time: formatar é papel da tela.
            self.__tela_clinica.mostra_clinica({
                "codigo": clinica.codigo,
                "nome": clinica.nome,
                "cidade": clinica.cidade,
                "descricao": clinica.descricao,
                "horario_abertura": clinica.horario_abertura,
                "horario_fechamento": clinica.horario_fechamento,
                "profissionais": [{"nome": p.nome, "cpf": p.cpf} for p in clinica.profissionais],
            })

    def pega_clinica_por_codigo(self, codigo: int) -> Clinica | None:
        for clinica in self.__clinicas:
            if clinica.codigo == codigo:
                return clinica
        return None

    def vincular_profissional(self) -> None:
        clinica = self.__seleciona_clinica()
        if clinica is None:
            return

        controlador_profissional = self.__controlador_sistema.controlador_profissional
        controlador_profissional.listar_profissionais()
        profissional = controlador_profissional.pega_profissional_por_cpf(
            self.__tela_clinica.seleciona_profissional())
        if profissional is None:
            self.__tela_clinica.mostra_mensagem("ATENÇÃO: profissional não encontrado!")
            return

        try:
            clinica.incluir_profissional(profissional)
        except ValueError as erro:
            self.__tela_clinica.mostra_mensagem(f"ATENÇÃO: {erro}")
            return
        self.__tela_clinica.mostra_mensagem("Profissional vinculado com sucesso!")

    def desvincular_profissional(self) -> None:
        clinica = self.__seleciona_clinica()
        if clinica is None:
            return

        cpf = self.__tela_clinica.seleciona_profissional()
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        for profissional in clinica.profissionais:
            if profissional.cpf == cpf:
                if any(atendimento.clinica is clinica and atendimento.profissional is profissional
                       for atendimento in atendimentos):
                    self.__tela_clinica.mostra_mensagem(
                        "ATENÇÃO: o profissional possui atendimentos nesta clínica.")
                    return
                clinica.excluir_profissional(profissional)
                self.__tela_clinica.mostra_mensagem("Profissional desvinculado com sucesso!")
                return
        self.__tela_clinica.mostra_mensagem(
            "ATENÇÃO: profissional não vinculado a esta clínica!")

    # --------------------------------------------------- métodos auxiliares
    def __seleciona_clinica(self) -> Clinica | None:
        """Lista as clínicas, pede o código e devolve a clínica (ou None)."""
        if not self.__clinicas:
            self.__tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
            return None
        self.listar_clinicas()
        clinica = self.pega_clinica_por_codigo(self.__tela_clinica.seleciona_clinica())
        if clinica is None:
            self.__tela_clinica.mostra_mensagem("ATENÇÃO: clínica não encontrada!")
        return clinica
