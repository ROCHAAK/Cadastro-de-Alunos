from aluno import *
from entrada import *
from navegabilidade import *
import json

#variáveis de controle dos dados na memória
id = 1
""" número do id de autoincremento
"""
alunos = []
""" lista de dicionários que armazena as abstrações de alunos
"""

while True:
    imprimir_cabecalho()
    exibir_menu()
    opc = ler_inteiro("Opção: ")

    #navegabilidade
    if (opc == 1):
        #função lê os dados de aluno e retorna um dicionário
        #dicionário é adicionado na lista de alunos
        while True:
            aluno = ler_dados_alunos() 
            alunos.append(aluno)  
            id += 1
            continuar = input("Deseja adicionar outro aluno? (s/n): ")
    
            if continuar.lower() == 's':
                pass  
            else:
                break 
    elif (opc == 2):
        #função imprime todos os alunos em tela
        imprimir_dados_alunos(alunos)
        pass
    elif (opc == 3):
        #busca um aluno por id e apresenta seus dados se existir
        id_busca = input("Digite o ID do aluno que deseja buscar: ")
        aluno_buscado = buscar_aluno(id_busca, alunos)

        if aluno_buscado:
            print(f"Aluno encontrado: Nome: {aluno_buscado['nome']}, Idade: {aluno_buscado['idade']}, Peso: {aluno_buscado['peso']}, Altura: {aluno_buscado['altura']}")
        else:
            print("Aluno não encontrado.")
        pass
    elif (opc == 4):
        #exibe uma lista com todos os alunos filtrados por imc
        imc_min = float(input("Mínimo de IMC: "))
        imc_max = float(input("Máximo de IMC: "))
        
        alunos_filtrados = filtro_alunos_por_imc(alunos, imc_min, imc_max)
        
        if alunos_filtrados:
            print("\nAlunos encontrados com IMC na faixa especificada:")
            for aluno in alunos_filtrados:
                print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Peso: {aluno['peso']}, Altura: {aluno['altura']}, IMC: {calcular_imc_aluno(aluno['peso'], aluno['altura']):.2f}")
        else:
            print("Nenhum aluno encontrado com o IMC na faixa especificada.")
        pass
    elif (opc == 5):
        #salva os dados e pergunta se deseja sair do programa
        salvar_dados_alunos(alunos)
        sair = input("Deseja sair do programa? (s/n): ")
        if sair.lower() == 's':
            break
        break
    else:
        print("Opção inválida!")

    limpar_tela()
