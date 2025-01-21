# DESAFIO
# Implemente um sistema de filtragem de dados que permita ao usuário especificar múltiplos critérios de
# filtragem usando funções lambda e `filter()`. 
from time import sleep
import os

lista_dados = []
nova_lista = []

while True:
    print("#Inserção de Dados#")
    print("1. Inteiro.")
    print("2. String.")
    try:
        op = int(input("Digite o tipo de dado: "))
    except ValueError:
        print("Digite um número do tipo INTEIRO.")
    sleep(2)
    os.system('cls')
    if 1 <= op <= 2:
        for i in range(4):
            try:
                num = input(f"Digite o seu {i+1}º elemento da lista: ")
                if op == 1:
                    lista_dados.append(int(num))
                if op == 2:
                    lista_dados.append(num)
            except ValueError:
                print("Coloque apenas valores do tipo escolhido.")
                exit()
        sleep(2)
        os.system('cls')        
        print("#Sistema de Filtragem#")
        match op:
            case 1:
                print("1. Filtrar por multiplo.")
                print("2. Filtrar por divisor.")
                print("3. Filtrar par.")
                print("4. Filtrar impar.")
                print("5. Maior que x número.")
                print("6. Maior que x número.")
                try:
                    filtro = int(input("Digite a opção: "))
                except ValueError:
                    print("Digite um número do tipo INTEIRO.")
                match filtro:
                    case 1:
                        try:
                            multiplo = int(input("Digite o valor do multiplo: "))
                            if multiplo < 0:
                                raise ValueError
                        except ValueError:
                            print("Digite um valor válido! (Inteiro positivo.)")
                        nova_lista = list(filter(lambda x: x % multiplo == 0, lista_dados))
                    case 2:
                        try:
                            divisor = int(input("Digite o valor do divisor: "))
                            if divisor < 0:
                                raise ValueError
                        except ValueError:
                            print("Digite um valor válido! (Inteiro positivo.)")
                        nova_lista = list(filter(lambda x: x % divisor == 0, lista_dados))
                    case 3:
                        nova_lista = list(filter(lambda x: x % 2 == 0, lista_dados))
                    case 4:
                        nova_lista = list(filter(lambda x: x % 2 != 0, lista_dados))
                    case 5:
                        try:
                            maior = int(input("Digite o x: "))
                        except ValueError:
                            print("Digite um valor válido! (Inteiro)")
                        nova_lista = list(filter(lambda x: x > maior, lista_dados))
                    case 6:
                        try:
                            menor = int(input("Digite o x: "))
                        except ValueError:
                            print("Digite um valor válido! (Inteiro)")
                        nova_lista = list(filter(lambda x: x < menor, lista_dados))
                    case _:
                        print("Digite uma opção válida.")
                        sleep(2)
            case 2:
                print("1. Filtrar por tamanho.")
                print("2. Filtrar pela primeiro letra.")
                print("3. Filtrar por palavra.")
                try:
                    filtro = int(input("Digite o tipo de dado: "))
                except ValueError:
                    print("Digite um número do tipo INTEIRO.")
                    exit()
                match filtro:
                    case 1:
                        try:
                            tamanho = int(input("Digite o tamanho: "))
                            if tamanho < 1:
                                raise ValueError
                        except ValueError:
                            print("Digite um valor inteiro positivo.")
                            exit()
                        nova_lista = list(filter(lambda x: len(str(x)) == tamanho, lista_dados))
                    case 2:
                        primeira_letra = input("Digite a letra: ").lower()
                        if len(primeira_letra) == 1:
                            if primeira_letra.isalpha():
                                nova_lista = filter(lambda x: x[0].lower() == primeira_letra)
                            else: 
                                print("A letra que você digitou é um caracter inválido.")
                        else:
                            print("Tamanho inválido!")
                    case 3:
                        palavra = input("Digite a letra: ").lower()
                        if primeira_letra.isalpha():
                            nova_lista = filter(lambda x: x.lower() == palavra)
                        else: 
                            print("A palavra que você digitou contém caracteres inválidos.")
        print(nova_lista)
        input()
        lista_dados.clear()
        nova_lista.clear()
        os.system('cls')
    else:
        print("Opção inválida!")
        sleep(2)
        os.system('cls')
   
     