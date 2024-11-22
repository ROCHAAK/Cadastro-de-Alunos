from entrada import *
import json

def ler_dados_alunos():
    """
    Lê os dadosdos alunos: nome,dade, peso e altura.

    Retorno:
     - Um dicionario contendo os dados: nome, idade, peso e altura.
    """
    id = 1
    aluno = {}
    aluno['id'] = id
    aluno['nome'] = ler_string("Digite o seu nome: ")
    aluno['idade'] = ler_inteiro("Digite a sua idade: ", pos=True)
    aluno['peso'] = ler_real("Digite o seu peso: ", pos=True)
    aluno['altura'] = ler_real("Digite a sua altura: ", pos=True)
    
    return aluno

def imprimir_dados_alunos(alunos):
    """
    Imprime as informações de todos os alunos na lista.

    Parâmetros:
    - alunos: lista de dicionários contendo os dados dos alunos.
    """
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    for i, aluno in enumerate(alunos, 1):
        print(f"{i}. Nome: {aluno['nome']}, Idade: {aluno['idade']}, Peso: {aluno['peso']}, Altura: {aluno['altura']}")

def buscar_aluno(id, alunos):
    """
    Busca um aluno através do ID e traz as informações deste aluno.

    Parâmetros:
    - id: ID do aluno a ser buscado
    - alunos: lista de dicionários contendo os dados dos alunos.

    Retorno:
    - Dicionário com as informações do aluno se encontrado, ou None se não encontrado.
    """
    for aluno in alunos:
        if aluno['id'] == int(id):
            return aluno 
    return None

def calcular_imc_aluno(peso, altura):
    """
    Calcula o IMC de um aluno a partir de seu peso e altura.

    Parâmetros:
    - peso: peso do aluno.
    - altura: altura do aluno.

    Retorno:
    - O IMC do aluno.
    """
    imc = peso / (altura ** 2)
    return imc

def filtro_alunos_por_imc(alunos, imc_min, imc_max):
    """
    Exibe uma lista com todos os alunos filtrados por imc

    Parâmetros:
    - alunos: lista de dicionários contendo os dados dos alunos.
    - imc_min: IMC mínimo para filtrar.
    - imc_max: IMC máximo para filtrar.

    Retorno:
    - Lista de alunos que tem IMC dentro da faixa.
    """
    alunos_filtrados = []
    for aluno in alunos:
        imc = calcular_imc_aluno(aluno['peso'], aluno['altura'])
        if imc_min <= imc <= imc_max:
            alunos_filtrados.append(aluno)
    return alunos_filtrados

def salvar_dados_alunos(alunos, arquivo='alunos.json'):
    """
    Salva a lista de alunos em um arquivo JSON.

    Parâmetros:
    - alunos: lista de dicionários contendo os dados dos alunos.
    - arquivo: nome do arquivo onde os dados serão salvos.
    """
    with open(arquivo, 'w') as f:
        json.dump(alunos, f, indent=4)
    print("Dados salvos com sucesso!")

def carregar_dados(arquivo='alunos.json'):
    """
    Carrega a lista de alunos de um arquivo JSON.

    Parâmetros:
    - arquivo: nome do arquivo de onde os dados serão carregados.

    Retorno:
    - Lista de alunos carregada do arquivo.
    """
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []