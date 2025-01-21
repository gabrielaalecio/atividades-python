# 1. Crie uma função lambda que retorne o quadrado de um número.

quadrado = lambda x: x**2
print(quadrado(5))

# 2. Use `map()` com uma função lambda para converter uma lista de temperaturas de Celsius para
#Fahrenheit.

celcius_lista = [54, 23, 43, -2]
fahr_lista =  list(map(lambda x: (x * 9/5) + 32, celcius_lista))
print(fahr_lista)

# 3. Utilize `filter()` com uma função lambda para obter todos os números pares de uma lista.
lista = [2, 4, 5, 10, 0, 3]
pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares)

# 4. Implemente uma função que ordene uma lista de strings pelo seu comprimento usando `sorted()` e
# uma função lambda.
lista_string = ['omg', 'cara', 'dignissimo', 'emi', 'Emilly']
nova_lista = sorted(lista_string, key=lambda x: len(x))
print(nova_lista)

# 5. Crie uma função que aplique um desconto a uma lista de preços usando `map()` e uma função lambda
lista_precos = [10, 15.4, 12.4, 5, 1, 2.5]
novo_preco = list(map(lambda x: x - x * 0.50, lista_precos))
print(novo_preco)

# 6. Use `filter()` e `map()` em conjunto para criar uma lista de quadrados de números ímpares de 1 a 20.
lista_seis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
nova = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, lista_seis)))
print(nova)

# DESAFIO
# Implemente um sistema de filtragem de dados que permita ao usuário especificar múltiplos critérios de
# filtragem usando funções lambda e `filter()`. 

