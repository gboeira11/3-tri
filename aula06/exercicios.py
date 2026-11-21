def conta_frequencias(lista):
    frequencias = {}
    for item in lista:
        if item in frequencias:
            frequencias[item] += 1
        else:
            frequencias[item] = 1
    return frequencias


def hash_soma(palavra, tamanho):
    return sum(ord(c) for c in palavra) % tamanho


def gavetas_com_colisao(palavras, tamanho):
    if tamanho <= 0:
        return None

    hash_table = [0] * tamanho

    for palavra in palavras:
        index = hash_soma(palavra, tamanho)
        hash_table[index] += 1

    colisao_count = sum(1 for count in hash_table if count > 1)

    return colisao_count


def mais_frequente(lista):
    frequencias = {}
    max = 0
    mais = None

    for item in lista:
        if item in frequencias:
            frequencias[item] += 1
        else:
            frequencias[item] = 1

        if frequencias[item] > max:
            max = frequencias[item]
            mais = item

    return mais

