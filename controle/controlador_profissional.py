from entidade.profissional import Profissional
from limite.tela_profissional import TelaProfissional


class ControladorProfissional:
    """Controla as operações de cadastro de profissionais."""

    def __init__(self, controlador_sistema):
        self.__profissionais: list[Profissional] = []
        self.__tela_profissional = TelaProfissional(self)
        self.__controlador_sistema = controlador_sistema

    def retornar(self) -> None:
        # O controle volta ao menu principal quando abre_tela() termina.
        pass

    def abre_tela(self) -> None:
        opcoes = {
            1: self.incluir_profissional,
            2: self.alterar_profissional,
            3: self.excluir_profissional,
            4: self.listar_profissionais,
        }
        while True:
            opcao = self.__tela_profissional.mostra_tela_opcoes()
            if opcao == 0:
                self.retornar()
                return
            opcoes[opcao]()

    def incluir_profissional(self) -> None:
        dados = self.__tela_profissional.pega_dados_profissional()

        if self.pega_profissional_por_cpf(dados["cpf"]) is not None:
            self.__tela_profissional.mostra_mensagem(
                "ATENÇÃO: já existe um profissional com esse CPF.")
            return

        profissional = Profissional(
            nome=dados["nome"],
            celular=dados["celular"],
            cpf=dados["cpf"],
            especialidade=dados["especialidade"],
            registro_profissional=dados["registro_profissional"],
        )
        self.__profissionais.append(profissional)
        self.__tela_profissional.mostra_mensagem("Profissional incluído com sucesso.")

    def alterar_profissional(self) -> None:
        profissional = self.__seleciona_profissional()
        if profissional is None:
            return

        novos_dados = self.__tela_profissional.pega_dados_profissional()

        # Mesmo critério de ControladorPaciente: o CPF pode mudar,
        # desde que não pertença a outro profissional.
        outro = self.pega_profissional_por_cpf(novos_dados["cpf"])
        if outro is not None and outro is not profissional:
            self.__tela_profissional.mostra_mensagem(
                "ATENÇÃO: já existe um profissional com esse CPF.")
            return

        profissional.nome = novos_dados["nome"]
        profissional.celular = novos_dados["celular"]
        profissional.cpf = novos_dados["cpf"]
        profissional.especialidade = novos_dados["especialidade"]
        profissional.registro_profissional = novos_dados["registro_profissional"]
        self.__tela_profissional.mostra_mensagem("Profissional alterado com sucesso.")

    def excluir_profissional(self) -> None:
        profissional = self.__seleciona_profissional()
        if profissional is None:
            return

        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if any(atendimento.profissional is profissional for atendimento in atendimentos):
            self.__tela_profissional.mostra_mensagem(
                "ATENÇÃO: não é possível excluir um profissional que possui atendimentos.")
            return

        # Remove o vínculo com as clínicas para não deixar referências órfãs.
        for clinica in self.__controlador_sistema.controlador_clinica.clinicas:
            if profissional in clinica.profissionais:
                clinica.excluir_profissional(profissional)

        self.__profissionais.remove(profissional)
        self.__tela_profissional.mostra_mensagem("Profissional excluído com sucesso.")

    def listar_profissionais(self) -> None:
        if not self.__profissionais:
            self.__tela_profissional.mostra_mensagem("Nenhum profissional cadastrado.")
            return

        for profissional in self.__profissionais:
            self.__tela_profissional.mostra_profissional({
                "nome": profissional.nome,
                "cpf": profissional.cpf,
                "celular": profissional.celular,
                "especialidade": profissional.especialidade,
                "registro_profissional": profissional.registro_profissional,
            })

    def pega_profissional_por_cpf(self, cpf: str) -> Profissional | None:
        for profissional in self.__profissionais:
            if profissional.cpf == cpf:
                return profissional
        return None

    # ---------------------------------------------------- método auxiliar
    def __seleciona_profissional(self) -> Profissional | None:
        """Lista os profissionais, pede o CPF e devolve o profissional (ou None)."""
        if not self.__profissionais:
            self.__tela_profissional.mostra_mensagem("Nenhum profissional cadastrado.")
            return None
        self.listar_profissionais()
        profissional = self.pega_profissional_por_cpf(
            self.__tela_profissional.seleciona_profissional())
        if profissional is None:
            self.__tela_profissional.mostra_mensagem("ATENÇÃO: profissional não encontrado.")
        return profissional