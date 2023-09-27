# Carolyne Soares Miranda da Luz
# Análise e Desenvolvimento de Sistemas

import json
from SistemaGerenciamento import SistemaGerenciamentoAcademico
from Menus import Menus

# Exemplo de uso
sistema = SistemaGerenciamentoAcademico()

while True:
    itemEscolhido = Menus.MenuPrincipal()
    Menus.MenuOperacoes(sistema, itemEscolhido)
