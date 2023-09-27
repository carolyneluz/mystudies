import json

# Foi criada a classe abaixo para representar as listas de cada elemento, bem como gerenciar o armazenamento destes e do arquivo externo
class SistemaGerenciamentoAcademico:
    def __init__(self):
        # Inicializa listas vazias para cada tipo de cadastro
        self.estudantes = []
        self.professores = []
        self.disciplinas = []
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
                if 'professores' in dados:
                    self.professores = dados['professores']
                if 'disciplinas' in dados:
                    self.disciplinas = dados['disciplinas']
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
            "professores": [],
            "disciplinas": [],
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
            2: ("professores", self.professores),
            3: ("disciplinas", self.disciplinas),
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
            2: self.professores,
            3: self.disciplinas,
            4: self.turmas,
            5: self.matriculas
        }
        
        # Mapeia o tipo de item com base no valor de index
        tipo_item = {
            1: "estudante",
            2: "professor",
            3: "disciplina",
            4: "turma",
            5: "matrícula"
        }.get(index, "item")

        if tipo_item in ["estudante", "professor"]:
            try:
                # Coleta as informações para o novo estudante ou professor
                codigo = int(input(f"Digite o código do {tipo_item} e pressione ENTER para continuar: "))
                nome = input(f"Digite o nome do {tipo_item} e pressione ENTER para continuar: ")
                cpf = input(f"Digite o CPF do {tipo_item} e pressione ENTER para continuar: ")

                # Cria um dicionário para o novo estudante ou professor
                item = {
                    "codigo": codigo,
                    "nome": nome,
                    "CPF": cpf
                }

                # Adiciona o item à lista apropriada
                index_to_list[index].append(item)
                index_to_list[index].sort(key=lambda x: x['codigo']) # Após incluir um item, sempre ordenamos de acordo com o código, em ordem crescente
            
            except IndexError:
                print("Ocorreu um erro ao incluir novos dados na lista")

        elif tipo_item == "disciplina":
            try:
                # Coleta as informações para o novo estudante ou professor
                codigo = int(input(f"Digite o código da {tipo_item} e pressione ENTER para continuar: "))
                nome = input(f"Digite o nome da {tipo_item} e pressione ENTER para continuar: ")

                item = {
                    "codigo": codigo,
                    "nome": nome,
                }

                # Adiciona o item à lista apropriada
                index_to_list[index].append(item)
                index_to_list[index].sort(key=lambda x: x['codigo'])

            except IndexError:
                print("Ocorreu um erro ao incluir novos dados na lista")

        elif tipo_item == "turma":
            try:
                codigo = int(input(f"Digite o código da {tipo_item} e pressione ENTER para continuar: "))
                codigo_professor = int(input(f"Digite o código do professor e pressione ENTER para continuar: "))
                codigo_disciplina = int(input(f"Digite o código da disciplina e pressione ENTER para continuar: "))

                item = {
                    "codigo": codigo,
                    "codigo_professor": codigo_professor,
                    "codigo_disciplina": codigo_disciplina,
                }

                # Adiciona o item à lista apropriada
                index_to_list[index].append(item)
                index_to_list[index].sort(key=lambda x: x['codigo'])

            except IndexError:
                print("Ocorreu um erro ao incluir novos dados na lista")
        
        elif tipo_item == "matrícula":
            try:
                codigo_turma = int(input(f"Digite o código da turma e pressione ENTER para continuar: "))
                codigo_estudante = int(input(f"Digite o código do estudante e pressione ENTER para continuar: "))

                item = {
                    "codigo_turma": codigo_turma,
                    "codigo_estudante": codigo_estudante,
                }

                # Adiciona o item à lista apropriada
                index_to_list[index].append(item)
                index_to_list[index].sort(key=lambda x: x['codigo_turma'])

            except IndexError:
                print("Ocorreu um erro ao incluir novos dados na lista")
        else:
            return # Para implementar depois para os outros casos, que poderiam vir a existir
      
    def ExcluirItem(self, index):
        print("\n===== EXCLUSÃO =====\n")  
        # Mapeia o tipo de item com base no valor de index
        tipo_item = {
            1: "estudante",
            2: "professor",
            3: "disciplina",
            4: "turma",
            5: "matrícula"
        }.get(index, "item")

        if tipo_item == "estudante":
            try:
                codigo = int(input(f"Digite o código do {tipo_item} que deseja excluir: "))
                for estudante in self.estudantes:
                    if estudante["codigo"] == codigo:
                        self.estudantes.remove(estudante)
                        print(f"{tipo_item} com código {codigo} foi excluído com sucesso.")
                        return
                print(f"Estudante com código {codigo} não encontrado.")
            except ValueError:
                print("Entrada inválida. O código do estudante deve ser um número inteiro.")
        
        if tipo_item == "professor":
            try:
                codigo = int(input(f"Digite o código do {tipo_item} que deseja excluir: "))
                for professor in self.professores:
                    if professor["codigo"] == codigo:
                        self.professores.remove(professor)
                        print(f"{tipo_item} com código {codigo} foi excluído com sucesso.")
                        return
                print(f"Professor com código {codigo} não encontrado.")
            except ValueError:
                print("Entrada inválida. O código do professor deve ser um número inteiro.")
        
        elif tipo_item == "disciplina":
            try:
                codigo = int(input(f"Digite o código da {tipo_item} que deseja excluir: "))
                for disciplina in self.disciplinas:
                    if disciplina["codigo"] == codigo:
                        self.disciplinas.remove(disciplina)
                        print(f"Disciplina com código {codigo} foi excluída com sucesso.")
                        return
                print(f"Disciplina com código {codigo} não encontrada.")
            except ValueError:
                print("Entrada inválida. O código da disciplina deve ser um número inteiro.")
        
        elif tipo_item == "turma":
            try:
                codigo = int(input(f"Digite o código da {tipo_item} que deseja excluir: "))
                for turma in self.turmas:
                    if turma["codigo"] == codigo:
                        self.turmas.remove(turma)
                        print(f"Turma com código {codigo} foi excluída com sucesso.")
                        return
                print(f"Turma com código {codigo} não encontrada.")
            except ValueError:
                print("Entrada inválida. O código da turma deve ser um número inteiro.")

        elif tipo_item == "matrícula":
            try:
                codigo_turma = int(input("Digite o código da turma da matrícula que deseja excluir: "))
                codigo_estudante = int(input("Digite o código do estudante da matrícula que deseja excluir: "))

                for matricula in self.matriculas:
                    if (
                        matricula["codigo_turma"] == codigo_turma
                        and matricula["codigo_estudante"] == codigo_estudante
                    ):
                        self.matriculas.remove(matricula)
                        print(f"Matrícula na turma {codigo_turma} para o estudante {codigo_estudante} foi excluída com sucesso.")
                        return
                print(f"Matrícula na turma {codigo_turma} para o estudante {codigo_estudante} não encontrada.")
            except ValueError:
                print("Entrada inválida. O código da turma deve ser um número inteiro.")
            
    def EditarItem(self, index):
        print("\n===== EDIÇÃO =====\n")
        index_to_list = {
            1: self.estudantes,
            2: self.professores,
            3: self.disciplinas,
            4: self.turmas,
            5: self.matriculas
        }
        
        # Mapeia o tipo de item com base no valor de index
        tipo_item = {
            1: "estudante",
            2: "professor",
            3: "disciplina",
            4: "turma",
            5: "matrícula"
        }.get(index, "item")

        if tipo_item == "estudante":
            try:
                codigo = int(input(f"Digite o código do {tipo_item} que deseja editar: "))
                encontrou = False
                for estudante in self.estudantes:
                    if estudante["codigo"] == codigo:
                        self.estudantes.remove(estudante)
                        encontrou = True
                if encontrou == False:
                    print("Não foi encontrado um estudante com esse código")
                    return
                    
                codigo = int(input(f"Digite o novo código do {tipo_item} e pressione ENTER para continuar: "))
                nome = input(f"Digite o novo nome do {tipo_item} e pressione ENTER para continuar: ")
                cpf = input(f"Digite o novo CPF do {tipo_item} e pressione ENTER para continuar: ")

                item = {
                    "codigo": codigo,
                    "nome": nome,
                    "CPF": cpf
                }

                # Adiciona o item à lista apropriada
                index_to_list[index].append(item)
                index_to_list[index].sort(key=lambda x: x['codigo']) # Após incluir um item, sempre ordenamos de acordo com o código, em ordem crescente
            
            except IndexError:
                print("Ocorreu um erro ao atualizar novos dados na lista")

        elif tipo_item == "professor":
            try:
                codigo = int(input(f"Digite o código do {tipo_item} que deseja editar: "))
                encontrou = False
                for professor in self.professores:
                    if professor["codigo"] == codigo:
                        self.professores.remove(professor)
                        encontrou = True
                if encontrou == False:
                    print("Não foi encontrado um professor com esse código")
                    return

                codigo = int(input(f"Digite o novo código do {tipo_item} e pressione ENTER para continuar: "))
                nome = input(f"Digite o novo nome do {tipo_item} e pressione ENTER para continuar: ")
                cpf = input(f"Digite o novo CPF do {tipo_item} e pressione ENTER para continuar: ")

                item = {
                    "codigo": codigo,
                    "nome": nome,
                    "CPF": cpf
                }

                # Adiciona o item à lista apropriada
                index_to_list[index].append(item)
                index_to_list[index].sort(key=lambda x: x['codigo']) # Após incluir um item, sempre ordenamos de acordo com o código, em ordem crescente
            
            except IndexError:
                print("Ocorreu um erro ao atualizar novos dados na lista")
        
        elif tipo_item == "disciplina":
            try:
                codigo = int(input(f"Digite o código da {tipo_item} que deseja editar: "))
                encontrou = False
                for disciplina in self.disciplinas:
                    if disciplina["codigo"] == codigo:
                        self.disciplinas.remove(disciplina)
                        encontrou = True
                if encontrou == False:
                    print("Não foi encontrada uma disciplina com esse código")
                    return
                codigo = int(input(f"Digite o novo código da {tipo_item} e pressione ENTER para continuar: "))
                nome = input(f"Digite o novo nome da {tipo_item} e pressione ENTER para continuar: ")

                item = {
                    "codigo": codigo,
                    "nome": nome,
                }

                # Adiciona o item à lista apropriada
                index_to_list[index].append(item)
                index_to_list[index].sort(key=lambda x: x['codigo'])

            except IndexError:
                print("Ocorreu um erro ao atualizar novos dados na lista")

        elif tipo_item == "turma":
            try:
                codigo = int(input(f"Digite o código da {tipo_item} que deseja editar: "))
                encontrou = False
                for turma in self.turmas:
                    if turma["codigo"] == codigo:
                        self.turmas.remove(turma)
                        encontrou = True
                if encontrou == False:
                    print("Não foi encontrada uma turma com esse código")
                    return
                codigo = int(input(f"Digite o novo código da {tipo_item} e pressione ENTER para continuar: "))
                codigo_professor = int(input(f"Digite o novo código do professor e pressione ENTER para continuar: "))
                codigo_disciplina = int(input(f"Digite o novo código da disciplina e pressione ENTER para continuar: "))

                item = {
                    "codigo": codigo,
                    "codigo_professor": codigo_professor,
                    "codigo_disciplina": codigo_disciplina,
                }

                index_to_list[index].append(item)
                index_to_list[index].sort(key=lambda x: x['codigo'])

            except IndexError:
                print("Ocorreu um erro ao atualizar novos dados na lista")
        
        elif tipo_item == "matrícula":
            try:
                codigo_turma = int(input(f"Digite o código da turma da matrícula que deseja editar e pressione ENTER para continuar: "))
                codigo_estudante = int(input(f"Digite o código do estudante da matrícula que deseja editar e pressione ENTER para continuar: "))
                encontrou = False
                for matricula in self.matriculas:
                    if (
                        matricula["codigo_turma"] == codigo_turma
                        and matricula["codigo_estudante"] == codigo_estudante
                    ):
                        self.matriculas.remove(matricula)
                        encontrou = True
                if encontrou == False:
                    print(f"Matrícula na turma {codigo_turma} para o estudante {codigo_estudante} não encontrada.")
                    return
                
                codigo_turma = int(input(f"Digite o novo código da turma e pressione ENTER para continuar: "))
                codigo_estudante = int(input(f"Digite o novo código do estudante e pressione ENTER para continuar: "))
                item = {
                    "codigo_turma": codigo_turma,
                    "codigo_estudante": codigo_estudante,
                }
                
                # Adiciona o item à lista apropriada
                index_to_list[index].append(item)
                index_to_list[index].sort(key=lambda x: x['codigo_turma'])

            except IndexError:
                print("Ocorreu um erro ao atualizar novos dados na lista")
        
        else:
            return # Para implementar depois para os outros casos, que poderiam vir a existir

    def AtualizarRegistros(self):
        
        arquivo_json = 'data.json'
        dados = {
            "estudantes": self.estudantes,
            "professores": self.professores,
            "disciplinas": self.disciplinas,
            "turmas": self.turmas,
            "matriculas": self.matriculas
        }

        with open(arquivo_json, 'w') as file:
            json.dump(dados, file)
