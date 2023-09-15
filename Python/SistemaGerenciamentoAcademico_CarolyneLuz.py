# Carolyne Soares Miranda da Luz
# Análise e Desenvolvimento de Sistemas

import json

# Foi criada a classe abaixo para representar as listas de cada elemento, bem como gerenciar o armazenamento destes e do arquivo externo
class SistemaGerenciamentoAcademico:
    def __init__(self):
        # Inicializa listas vazias para cada tipo de cadastro
        self.estudantes = []
        self.disciplinas = []
        self.professores = []
        self.turmas = []
        self.matriculas = []
        
        # Nome do arquivo JSON
        arquivo_json = 'data.json'

        # Bloco de código para tentar abrir o arquivo caso ele já exista. Na exceção, caso não exista, cria um em branco com o mesmo nome, data.json
        try:
            with open(arquivo_json, 'r') as file:
                dados = json.load(file)

                if 'estudantes' in dados:
                    self.estudantes = dados['estudantes']
                if 'disciplinas' in dados:
                    self.disciplinas = dados['disciplinas']
                if 'professores' in dados:
                    self.professores = dados['professores']
                if 'turmas' in dados:
                    self.turmas = dados['turmas']
                if 'matriculas' in dados:
                    self.matriculas = dados['matriculas']
        except FileNotFoundError:
            # O arquivo JSON não existe, então as listas permanecem vazias
            self.CriarArquivoVazio(arquivo_json)

    def CriarArquivoVazio(self, arquivo_json):
        # Cria um novo arquivo JSON com listas vazias
        dados = {
            "estudantes": [],
            "disciplinas": [],
            "professores": [],
            "turmas": [],
            "matriculas": []
        }

        with open(arquivo_json, 'w') as file:
            json.dump(dados, file)
    
    # Método para imprimir uma lista de um determinado elemento
    def ImprimirLista(self, index):
        print("\n===== LISTAGEM =====\n")
        index_to_list = {
            1: ("estudantes", self.estudantes),
            2: ("disciplinas", self.disciplinas),
            3: ("professores", self.professores),
            4: ("turmas", self.turmas),
            5: ("matriculas", self.matriculas)
        }
        
        if index in index_to_list:
            nome_lista, lista = index_to_list[index]
            if lista:
                print(f"Lista de {nome_lista}:")
                for item in lista:
                    print(item)
            else:
                print(f"A lista de {nome_lista} está vazia.")
        else:
            print("Índice inválido.")
    
    # Método para cadastrar um item na lista
    def CadastrarItem(self, index):
        print("\n===== INCLUSÃO =====\n")
        index_to_list = {
            1: self.estudantes,
            2: self.disciplinas,
            3: self.professores,
            4: self.turmas,
            5: self.matriculas
        }
        if index == 1:
            item = input("Digite o nome do estudante e pressione ENTER para continuar: ")
        else:
            return # Para implementar depois para os outros casos, como professor, matrícula, etc.
        try:
            index_to_list[index].append(item)
            index_to_list[index].sort()
            
        except IndexError:
            print("Ocorreu um erro ao incluir novos dados na lista")

    # Método para atualizar o arquivo JSON com os dados das listas locais 
    def AtualizarRegistros(self):
        
        arquivo_json = 'data.json'
        dados = {
            "estudantes": self.estudantes,
            "disciplinas": self.disciplinas,
            "professores": self.professores,
            "turmas": self.turmas,
            "matriculas": self.matriculas
        }

        with open(arquivo_json, 'w') as file:
            json.dump(dados, file)

        print(f"Dados atualizados no arquivo {arquivo_json}.")

# Método para exibição e uso do menu principal
def MenuPrincipal():
    print("\n----- MENU PRINCIPAL -----\n\n"
      "(1) Gerenciar estudantes\n"
      "(2) Gerenciar professores\n"
      "(3) Gerenciar disciplinas\n"
      "(4) Gerenciar turmas\n"
      "(5) Gerenciar matriculas\n"
      "(9) Sair\n")
    
    # Enquanto não for escolhida a opção 9, persiste no menu principal 
    while True:
        entradaDesejada = input("Informe a ação desejada: ")

        try:
            entradaDesejada = int(entradaDesejada)
            if entradaDesejada in [1, 2, 3, 4, 5]:
                return entradaDesejada
            elif entradaDesejada == 9:
                exit()
            else: # Caso o usuário digite um número que não está incluso nas opções
                print("Opção inválida. Por favor, escolha uma opção válida (digite um número de 1 a 5 ou digite 9 para sair).\n")
        except ValueError: # Caso o usuário digite um valor não numérico
            print("Entrada inválida. Por favor, escolha uma opção válida (digite um número de 1 a 5 ou digite 9 para sair).\n")

# Método para exibição e uso do menu de operações
def  MenuOperacoes(sistema, itemDesejado):
    entrada_mapping = { # Relação do tipo de item com um número, para facilitar operações internas
        1: "ESTUDANTES",
        2: "PROFESSORES",
        3: "DISCIPLINAS",
        4: "TURMAS",
        5: "MATRÍCULAS"
    }
    
    entradaSelecionada = entrada_mapping.get(itemDesejado, "Opção inválida")
    while True:
        print(f"\n**** [{entradaSelecionada}] MENU DE OPERAÇÕES ****\n\n"
        "(1) Incluir\n"
        "(2) Listar\n"
        "(3) Atualizar\n"
        "(4) Excluir\n"
        "(5) Voltar ao menu principal\n")
        entradaDesejada = input("Informe a ação desejada: ")

        try:
            entradaDesejada = int(entradaDesejada)
            if entradaDesejada == 5:
                return
            elif entradaDesejada == 1: 
                sistema.CadastrarItem(itemDesejado)
                sistema.AtualizarRegistros() # Ao fim de uma nova inclusão, salva a inclusão no arquivo .json
            elif entradaDesejada == 2:
                sistema.ImprimirLista(itemDesejado)
            elif entradaDesejada in [3, 4]: # Alterar depois para incluir as outras funcionalidades que serão implementadas no futuro
                print ("\n FUNCIONALIDADE EM DESENVOLVIMENTO")
                continue
            else:
                print("Opção inválida. Por favor, escolha uma opção válida (digite um número de 1 a 5).\n")
        except ValueError:
            print("Entrada inválida. Por favor, escolha uma opção válida (digite um número de 1 a 5).\n")
    return true


# Exemplo de uso
sistema = SistemaGerenciamentoAcademico()

while True:
    itemEscolhido = MenuPrincipal()
    if itemEscolhido in [2, 3, 4, 5]:
        print ("\n FUNCIONALIDADE EM DESENVOLVIMENTO") # Caso selecione itens que ainda não foram desenvolvidos
    else:
        MenuOperacoes(sistema, itemEscolhido)

