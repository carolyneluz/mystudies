class Menus:
    def __init__(self): ()

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
    def MenuOperacoes(sistema, itemDesejado):
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
            "(3) Editar\n"
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
                    sistema.AtualizarRegistros() # Ao fim de uma nova exclusão, salva a inclusão no arquivo .json
                elif entradaDesejada == 3:
                    sistema.EditarItem(itemDesejado)
                    sistema.AtualizarRegistros() # Ao fim de uma nova exclusão, salva a inclusão no arquivo .json
                elif entradaDesejada == 4:
                    sistema.ExcluirItem(itemDesejado)
                    sistema.AtualizarRegistros() # Ao fim de uma nova exclusão, salva a inclusão no arquivo .json
                    continue
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida (digite um número de 1 a 5).\n")
            except ValueError:
                print("Entrada inválida. Por favor, escolha uma opção válida (digite um número de 1 a 5).\n")