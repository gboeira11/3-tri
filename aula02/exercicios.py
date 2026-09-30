"""Aula 02 - Listas em Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def remove_negativos(lista):
    """Devolve uma lista nova so com os numeros que nao sao negativos."""
for numero in lista:
        if numero >= 0:
            resultado.append(numero)
            
    return resultado

def inverte(lista):
    """Devolve uma lista nova na ordem contraria.
    Sem usar reverse() e sem usar [::-1]."""
def inverte(lista):
    lista_invertida = []
    i = len(lista) - 1
    while i >= 0:
        lista_invertida.append(lista[i])
        i += 1
        i -= 1
    return lista_invertida

def busca_binaria(lista, alvo):
    """Recebe uma lista JA ORDENADA. Devolve a posicao do alvo, ou -1."""
inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        
        if lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

def intercala(lista_a, lista_b):
    """Devolve uma lista nova alternando os elementos das duas.
    As duas listas tem o mesmo tamanho."""
for item_a, item_b in zip(lista_a, lista_b):
        resultado.append(item_a)
        resultado.append(item_b)
        
    return resultado

def remove_repetidos(lista):
    """(Desafio) Devolve uma lista nova sem repetidos,
    mantendo a ordem da primeira aparicao."""
for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado