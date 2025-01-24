from time import sleep
import os

tamanho_alunos = 0

def cadastro(nome, idade, curso):
    global tamanho_alunos
    tamanho_alunos = tamanho_alunos + 1
    if tamanho_alunos < 10:
        matricula = "20250" + str(tamanho_alunos)
    else:
        matricula = "2025" + str(tamanho_alunos)
    aluno = f'{nome};{idade};{curso};{matricula}\n'
    with open("alunos.txt", "a") as arquivo:
        arquivo.writelines(aluno)   

def listar():
    with open("alunos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        if not linhas:
            print("Não há alunos cadastrados!")
        else:
            for i in linhas:
                nome, idade, curso, matricula = i.strip().split(";")
                print(f"Nome: {nome}")
                print(f"Idade: {idade}")
                print(f"Curso: {curso}")
                print(f"Matricula: {matricula}")
                print(15*'=')
                
def buscar(cod):
    with open("alunos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        if not linhas:
            print("Não há alunos cadastrados!")
        else:
            for i in linhas:
                nome, idade, curso, matricula = i.strip().split(";")
                if matricula == cod:
                    print(f"Nome: {nome}")
                    print(f"Idade: {idade}")
                    print(f"Curso: {curso}")
                    print(f"Matricula: {matricula}")
                    print(15*'=')
                    return True
    return False
    
def editar(cod):
    linhas_atualizada = []
    achou = False
    with open("alunos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    for i in linhas:
        nome, idade, curso, matricula = i.strip().split(";")
        if matricula == cod:
            achou = True
            print("1. Editar o nome. ")
            print("2. Editar a idade. ")
            print("3. Editar o curso. ")
            op = int(input("Digite a opção desejada: "))
            match op:
                case 1:
                    nome_novo = input("Digite o nome: ")
                    if nome_novo.isalpha():
                        nome = nome_novo
                    else:
                        print("Digite apenas letras!")
                        exit()
                case 2:
                    try:
                        idade_nova = int(input("Digite o nome: "))
                        if idade_nova < 18:
                            print("Menores de idade não podem ser cadastrados!")
                        else:
                            idade = idade_nova
                    except ValueError:
                        print("Digite um valor válido! (inteiro)")
                        exit()
                case 3:
                    curso_novo = input("Digite o nome: ")
                    if curso_novo.isalpha():
                        curso = curso_novo
                    else:
                        print("Digite apenas letras!")
                        exit()
        linhas_atualizada.append(f'{nome};{idade};{curso};{matricula}\n')

    with open("alunos.txt", "w") as arquivo:
            arquivo.writelines(linhas_atualizada)
    
    return achou

def excluir(cod):
    linhas_atualizada = []
    achou = False
    with open("alunos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    for i in linhas:
        nome, idade, curso, matricula = i.strip().split(";")
        if matricula != cod:
            linhas_atualizada.append(i)
        else:
            achou = True

    with open("alunos.txt", "w") as arquivo:
            arquivo.writelines(linhas_atualizada)

    return achou


while True:
    print("1. Cadastrar aluno.")
    print("2. Listar Aluno.")
    print("3. Buscar Aluno.")
    print("4. Editar Aluno.")
    print("5. Excluir Aluno.")
    try:
        op = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Digite um valor válido!")
        sleep(2)
        exit()
    os.system("cls")
    match op:
        case 1:
            try:
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                if idade < 18 or idade > 99:
                    print("Idade inválida!")
                    break
                curso = input("Curso: ")
                cadastro(nome, idade, curso)
            except ValueError:
                print("Digite um valor válido!")
        case 2:
            print(15*'=')
            print("Lista de Alunos")
            print(15*'=')
            listar()
            input("Digite qualquer coisa para voltar para a tela inicial: ")
        case 3: #buscar aluno
            print(15*'=')
            print("Buscar Aluno")
            print(15*'=')
            cod = input("Digite o número de matrícula do aluno: ")
            print(15*'=')
            if cod.isdigit():
                if not buscar(cod):
                    print("Aluno não encontrado!")
                    print(15*'=')
                input("Digite qualquer coisa para voltar para a tela inicial: ")
            else:
                print("Digite uma mátricula válida!")
            print(15*'=')
            sleep(2)
        case 4: #editar aluno
            print(15*'=')
            print("Edição de Aluno")
            print(15*'=')
            ed = input("Digite o número de matrícula do aluno: ")
            if ed.isdigit():
                if editar(ed):
                    print("Aluno editado com sucesso!")
                else:
                    print("O aluno não foi encontrado!")
                input("Digite qualquer coisa para voltar para a tela inicial: ")
            else:
                print("Digite uma mátricula válida!")
            print(15*'=')
            sleep(2)
        case 5: #excluir aluno
            print(15*'=')
            print("Excluir Aluno")
            print(15*'=')
            ed = input("Digite o número de matrícula do aluno: ")
            if ed.isdigit():
                if excluir(ed):
                    print("Aluno excluido com sucesso!")
                else:
                    print("O aluno não foi encontrado!")
                input("Digite qualquer coisa para voltar para a tela inicial: ")
            else:
                print("Digite uma mátricula válida!")
            print(15*'=')
            sleep(2)
        case _:
            print("Saindo...")
            sleep(2)
            exit()
    os.system("cls")