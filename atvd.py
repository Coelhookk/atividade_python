# Sistema de Cadastro e Consulta de Notas de Alunos

alunos = {}

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    if nome in alunos:
        print("Aluno já cadastrado!")
    else:
        alunos[nome] = []
        print("Aluno cadastrado com sucesso.")

def adicionar_nota():
    nome = input("Digite o nome do aluno: ")
    if nome in alunos:
        try:
            nota = float(input("Digite a nota do aluno: "))
            alunos[nome].append(nota)
            print("Nota adicionada com sucesso.")
        except ValueError:
            print("Digite uma nota válida.")
    else:
        print("Aluno não encontrado.")

def consultar_notas():
    nome = input("Digite o nome do aluno: ")
    if nome in alunos:
        notas = alunos[nome]
        if notas:
            media = sum(notas) / len(notas)
            print(f"Notas de {nome}: {notas}")
            print(f"Média de {nome}: {media:.2f}")
        else:
            print("Este aluno ainda não tem notas cadastradas.")
    else:
        print("Aluno não encontrado.")

def menu():
    while True:
        print("\nSistema de Cadastro e Consulta de Notas")
        print("1. Cadastrar Aluno")
        print("2. Adicionar Nota")
        print("3. Consultar Notas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            adicionar_nota()
        elif opcao == "3":
            consultar_notas()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu principal
menu()
