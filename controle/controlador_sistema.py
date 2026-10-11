from limite.tela_sistema import TelaSistema
#from controle.controlador_paciente import ControladorPaciente
#from controle.controlador_profissional import ControladorProfissional
#from controle.controlador_clinica import ControladorClinica
#from controle.controlador_tipo_atendimento import ControladorTipoAtendimento
#from controle.controlador_atendimento import ControladorAtendimento
#from controle.controlador_pagamento import ControladorPagamento
#from controle.controlador_relatorio import ControladorRelatorio

class ControladorSistema:
   
    def __init__(self):
        #self.__controlador_paciente = ControladorPaciente(self)
        #self.__controlador_profissional = ControladorProfissional(self)
        #self.__controlador_clinica = ControladorClinica(self)
        #self.__controlador_tipo_atendimento = ControladorTipoAtendimento(self)
        #self.__controlador_atendimento = ControladorAtendimento(self)
        #self.__controlador_pagamento = ControladorPagamento(self)
        #self.__controlador_relatorio = ControladorRelatorio(self)
        self.__tela_sistema = TelaSistema(self)

    @property
    def controlador_paciente(self):
        return self.__controlador_paciente

    @property
    def controlador_profissional(self):
        return self.__controlador_profissional

    @property
    def controlador_clinica(self):
        return self.__controlador_clinica

    @property
    def controlador_tipo_atendimento(self):
        return self.__controlador_tipo_atendimento

    @property
    def controlador_atendimento(self):
        return self.__controlador_atendimento

    @property
    def controlador_pagamento(self):
        return self.__controlador_pagamento

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_pacientes, 2: self.cadastra_profissionais, 3: self.cadastra_clinicas,
                        4: self.cadastra_tipos_atendimento, 5: self.cadastra_atendimentos, 6: self.cadastra_pagamentos,
                        7: self.abre_relatorios, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_pacientes(self):
        pass

    def cadastra_profissionais(self):
        pass

    def cadastra_clinicas(self):
        pass

    def cadastra_tipos_atendimento(self):
        pass

    def cadastra_atendimentos(self):
        pass

    def cadastra_pagamentos(self):
        pass

    def abre_relatorios(self):
        pass

    def encerra_sistema(self):
        exit(0)
    