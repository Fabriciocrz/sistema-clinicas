from entidade.paciente import Paciente
from limite.tela_paciente import TelaPaciente
   

class ControladorPaciente:
    """Controla as operações de cadastro de pacientes."""

    def __init__(self, controlador_sistema):
        self.__pacientes: list[Paciente] = []
        self.__tela_paciente = TelaPaciente(self)
        self.__controlador_sistema = controlador_sistema

    def retornar(self) -> None:
        # Não chama controlador_sistema.abre_tela(): basta encerrar o laço de
        # abre_tela() para o controle voltar ao menu principal que nos chamou.
        pass

    def abre_tela(self) -> None:
        opcoes = {
            1: self.incluir_paciente,
            2: self.alterar_paciente,
            3: self.excluir_paciente,
            4: self.listar_pacientes,
        }
        while True:
            opcao = self.__tela_paciente.mostra_tela_opcoes()
            if opcao == 0:
                self.retornar()
                return
            opcoes[opcao]()

    def incluir_paciente(self) -> None:
        dados = self.__tela_paciente.pega_dados_paciente()

        if self.pega_paciente_por_cpf(dados["cpf"]) is not None:
            self.__tela_paciente.mostra_mensagem("ATENÇÃO: já existe um paciente com este CPF.")
            return

        paciente = Paciente(
            nome=dados["nome"],
            celular=dados["celular"],
            cpf=dados["cpf"],
            data_nascimento=dados["data_nascimento"],
            tem_responsavel=dados["tem_responsavel"],
        )
        self.__pacientes.append(paciente)
        self.__tela_paciente.mostra_mensagem("Paciente incluído com sucesso.")

    def alterar_paciente(self) -> None:
        paciente = self.__seleciona_paciente()
        if paciente is None:
            return

        novos_dados = self.__tela_paciente.pega_dados_paciente()

        # Se o CPF foi alterado, garante que não pertence a outro paciente.
        outro = self.pega_paciente_por_cpf(novos_dados["cpf"])
        if outro is not None and outro is not paciente:
            self.__tela_paciente.mostra_mensagem("ATENÇÃO: já existe um paciente com este CPF.")
            return

        paciente.nome = novos_dados["nome"]
        paciente.celular = novos_dados["celular"]
        paciente.cpf = novos_dados["cpf"]
        paciente.data_nascimento = novos_dados["data_nascimento"]
        paciente.tem_responsavel = novos_dados["tem_responsavel"]
        self.__tela_paciente.mostra_mensagem("Paciente alterado com sucesso.")

    def excluir_paciente(self) -> None:
        paciente = self.__seleciona_paciente()
        if paciente is None:
            return

        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if any(atendimento.paciente is paciente for atendimento in atendimentos):
            self.__tela_paciente.mostra_mensagem(
                "ATENÇÃO: não é possível excluir um paciente que possui atendimentos.")
            return

        self.__pacientes.remove(paciente)
        self.__tela_paciente.mostra_mensagem("Paciente excluído com sucesso.")

    def listar_pacientes(self) -> None:
        if not self.__pacientes:
            self.__tela_paciente.mostra_mensagem("Nenhum paciente cadastrado.")
            return

        for paciente in self.__pacientes:
            self.__tela_paciente.mostra_paciente({
                "nome": paciente.nome,
                "celular": paciente.celular,
                "cpf": paciente.cpf,
                "data_nascimento": paciente.data_nascimento,
                "tem_responsavel": paciente.tem_responsavel,
            })

    def pega_paciente_por_cpf(self, cpf: str) -> Paciente | None:
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None

    # ---------------------------------------------------- método auxiliar
    def __seleciona_paciente(self) -> Paciente | None:
        """Lista os pacientes, pede o CPF e devolve o paciente (ou None)."""
        if not self.__pacientes:
            self.__tela_paciente.mostra_mensagem("Nenhum paciente cadastrado.")
            return None
        self.listar_pacientes()
        paciente = self.pega_paciente_por_cpf(self.__tela_paciente.seleciona_paciente())
        if paciente is None:
            self.__tela_paciente.mostra_mensagem("ATENÇÃO: paciente não encontrado.")
        return paciente
