"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
    """Devolve a soma de todos os numeros da lista. Lista vazia devolve 0."""
    pass
    soma = 0
    for n in lista:
    soma = soma + n
    return soma


def conta_pares(lista):
    """Devolve quantos numeros da lista sao pares."""
    pass
    conta_pares = 0
    for n in lista:
    if n % 2 == 0:
        conta_pares += 1
        return conta_pares


def maior_valor(lista):
    """Devolve o maior numero da lista. A lista nao esta vazia."""
    pass
maior = lista[0]
for n in lista:
    if n > maior:
        maior = n
return maior

def existe(lista, alvo):
    """Devolve True se o alvo esta na lista, False se nao esta."""
    pass
for item in lista:
    if item == alvo:
        return True
    return False

def busca_linear(lista, alvo):
    """Devolve a posicao do alvo na lista, ou -1 se ele nao estiver."""
    pass
for i in range(len(lista)):
    if lista[i] == alvo:
        return i
    return -1

def segundo_maior(lista):
    """(Desafio) Devolve o segundo maior, percorrendo a lista uma unica vez."""
    pass
