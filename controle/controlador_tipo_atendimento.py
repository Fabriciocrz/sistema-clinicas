from entidade.tipo_atendimento import TipoAtendimento
from limite.tela_tipo_atendimento import TelaTipoAtendimento

class ControladorTipoAtendimento:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tipos_atendimento = []
        self.__tela_tipo_atendimento = TelaTipoAtendimento(self)

    def retornar(self):
        self.__controlador_sistema.abre_tela()   

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_tipo_atendimento, 2: self.alterar_tipo_atendimento, 3: self.excluir_tipo_atendimento,
                        4: self.listar_tipos_atendimento,  0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_tipo_atendimento.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def incluir_tipo_atendimento(self):
        dados = self.__tela_tipo_atendimento.pega_dados_tipo_atendimento()

        if self.pega_tipo_atendimento_por_codigo(dados["codigo"]) != None:
            self.__tela_tipo_atendimento.mostra_mensagem("Atenção: ja tem um tipo de atendimento com esse código") 
            return
        
        tipo_atendimento = TipoAtendimento(dados["codigo"], dados["nome"])
        self.__tipos_atendimento.append(tipo_atendimento)          
        self.__tela_tipo_atendimento.mostra_mensagem("Novo tipo de atendimento adicionado") 

    def alterar_tipo_atendimento(self):
        self.listar_tipos_atendimento()
        codigo = self.__tela_tipo_atendimento.seleciona_tipo_atendimento()
        tipo_atendimento = self.pega_tipo_atendimento_por_codigo(codigo)

        if tipo_atendimento == None:
            self.__tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento não encontrado")
            return

        novos_dados = self.__tela_tipo_atendimento.pega_dados_tipo_atendimento()

        outro_codigo = self.pega_tipo_atendimento_por_codigo(novos_dados["codigo"])
        if outro_codigo != None and outro_codigo != tipo_atendimento:
            self.__tela_tipo_atendimento.mostra_mensagem("Atenção: ja tem um tipo de atendimento com esse código")

        else:
            tipo_atendimento.codigo = novos_dados["codigo"]
            tipo_atendimento.nome = novos_dados["nome"]
            self.__tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento alterado")


    def excluir_tipo_atendimento(self):
        self.listar_tipos_atendimento()
        codigo = self.__tela_tipo_atendimento.seleciona_tipo_atendimento()
        tipo_atendimento = self.pega_tipo_atendimento_por_codigo(codigo)

        if tipo_atendimento == None:
            self.__tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento não encontrado")
            return
        else:
            self.__tipos_atendimento.remove(tipo_atendimento)
            self.__tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento removido")

    def listar_tipos_atendimento(self):

        if len(self.__tipos_atendimento) == 0:
            self.__tela_tipo_atendimento.mostra_mensagem("Nenhum tipo de atendimento registrado")
            return

        else:
            for tipo_atendimento in self.__tipos_atendimento:
                self.__tela_tipo_atendimento.mostra_tipo_atendimento({"codigo": tipo_atendimento.codigo, "nome": tipo_atendimento.nome})

    def pega_tipo_atendimento_por_codigo(self, codigo: int) -> TipoAtendimento:
        for tipo_atendimento in self.__tipos_atendimento:
            if tipo_atendimento.codigo == codigo:
                return tipo_atendimento
        return None