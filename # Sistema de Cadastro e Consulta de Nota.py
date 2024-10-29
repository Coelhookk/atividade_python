import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect("sistema_notas.db")
cursor = conexao.cursor()

# Criar tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS notas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER,
    nota REAL,
    FOREIGN KEY (aluno_id) REFERENCES alunos (id)
)
""")
conexao.commit()

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    try:
        cursor.execute("INSERT INTO alunos (nome) VALUES (?)", (nome,))
        conexao.commit()
        print("Aluno cadastrado com sucesso.")
    except sqlite3.IntegrityError:
        print("Aluno já cadastrado!")

def adicionar_nota():
    nome = input("Digite o nome do aluno: ")
    cursor.execute("SELECT id FROM alunos WHERE nome = ?", (nome,))
    aluno = cursor.fetchone()
    if aluno:
        try:
            nota = float(input("Digite a nota do aluno: "))
            cursor.execute("INSERT INTO notas (aluno_id, nota) VALUES (?, ?)", (aluno[0], nota))
            conexao.commit()
            print("Nota adicionada com sucesso.")
        except ValueError:
            print("Digite uma nota válida.")
    else:
        print("Aluno não encontrado.")

def consultar_notas():
    nome = input("Digite o nome do aluno: ")
    cursor.execute("SELECT id FROM alunos WHERE nome = ?", (nome,))
    aluno = cursor.fetchone()
    if aluno:
        cursor.execute("SELECT nota FROM notas WHERE aluno_id = ?", (aluno[0],))
        notas = cursor.fetchall()
        if notas:
            notas = [nota[0] for nota in notas]
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

# Fechar a conexão ao encerrar o programa
conexao.close()
