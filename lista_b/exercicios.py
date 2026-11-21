"""Lista B - ordenacao, dois indices e janela, contagem por chave.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Nos exercicios de ordenacao, NAO use sorted() nem list.sort().
Onde o enunciado pede lista nova, preserve a lista recebida.
bubble_sort e selection_sort devolvem (lista_ordenada, comparacoes, trocas),
o mesmo contrato da aula05.
"""

# ---------- Bloco 1: ordenacao ----------

def passagem_bubble(lista):
    """Uma unica passagem completa da esquerda para a direita, trocando
    vizinhos fora de ordem. Devolve uma copia; nao altera a entrada."""
    lista = lista.copy()

    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux

    return lista

def bubble_sort(lista):
    """Bubble sort crescente, parando quando uma passagem nao faz troca.
    Devolve (lista_ordenada, comparacoes, trocas): conte toda comparacao
    entre vizinhos e somente as trocas que acontecerem."""
    lista = lista.copy()
    comparacoes = 0
    trocas = 0

    for j in range(len(lista) - 1):
        fez_troca = False
        for i in range(len(lista) - 1 - j):
            comparacoes += 1
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                trocas += 1
                fez_troca = True
        if not fez_troca:
            break

    return lista, comparacoes, trocas


def selection_sort(lista):
    """Selection sort crescente. Devolve (lista_ordenada, comparacoes,
    trocas): conte cada comparacao entre candidatos e as trocas reais
    (nao conte a troca de um value consigo mesmo)."""
    lista = lista.copy()
    comparacoes = 0
    trocas = 0

    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            comparacoes += 1
            if lista[j] < lista[min_idx]:
                min_idx = j
        if min_idx != i:
            aux = lista[i]
            lista[i] = lista[min_idx]
            lista[min_idx] = aux
            trocas += 1

    return lista, comparacoes, trocas


def insertion_sort(lista):
    """Insira cada proximo valor na posicao certa do trecho ja ordenado.
    Devolve uma copia; nao altera a entrada."""
    lista = lista.copy()
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista


def quicksort(lista):
    """(Desafio) Quicksort recursivo, separando menores, iguais e maiores
    que o pivo. Devolve uma copia."""
    if len(lista) <= 1:
        return lista.copy()

    pivo = lista[0]

    menores = []
    iguais = []
    maiores = []

    for numero in lista:
        if numero < pivo:
            menores.append(numero)
        elif numero == pivo:
            iguais.append(numero)
        else:
            maiores.append(numero)

    return quicksort(menores) + iguais + quicksort(maiores)

# ---------- Bloco 2: dois indices e janela ----------

def eh_palindromo(texto):
    """True se a sequencia for igual de tras para frente. Maiusculas e
    espacos contam."""
    esquerda = 0
    direita = len(texto) - 1

    while esquerda < direita:
        if texto[esquerda] != texto[direita]:
            return False
        esquerda += 1
        direita -= 1

    return True


def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. Dois indices distintos cuja soma e alvo, ou
    (-1, -1). Use dois indices, sem laco dentro de laco."""
    esquerda = 0
    direita = len(lista) - 1

    while esquerda < direita:
        soma = lista[esquerda] + lista[direita]
        if soma == alvo:
            return (esquerda, direita)
        elif soma < alvo:
            esquerda += 1
        else:
            direita -= 1

    return (-1, -1)


def remove_repetidos_ordenada(lista):
    """Lista JA ORDENADA. Copia com uma ocorrencia de cada valor."""
    if not lista:
        return []

    resultado = [lista[0]]
    for i in range(1, len(lista)):
        if lista[i] != lista[i - 1]:
            resultado.append(lista[i])

    return resultado


def soma_maxima_janela(lista, k):
    """Maior soma de um trecho consecutivo de tamanho k (1 <= k <= n).
    Atualize a janela sem somar tudo de novo."""
    if not lista or k <= 0 or k > len(lista):
        return None

    max_soma = sum(lista[:k])
    soma_atual = max_soma

    for i in range(1, len(lista) - k + 1):
        soma_atual = soma_atual - lista[i - 1] + lista[i + k - 1]
        max_soma = max(max_soma, soma_atual)

    return max_soma


def conta_janelas_acima(lista, k, limite):
    """(Desafio) Quantas janelas consecutivas de tamanho k tem soma
    ESTRITAMENTE maior que limite. Atualize a soma em tempo constante."""
    if not lista or k <= 0 or k > len(lista):
        return 0

    count = 0
    soma_atual = sum(lista[:k])

    if soma_atual > limite:
        count += 1

    for i in range(1, len(lista) - k + 1):
        soma_atual = soma_atual - lista[i - 1] + lista[i + k - 1]
        if soma_atual > limite:
            count += 1

    return count


# ---------- Bloco 3: contagem por chave ----------

def conta_frequencias(lista):
    """Dicionario com a frequencia de cada valor."""
    frequencias = {}
    for item in lista:
        if item in frequencias:
            frequencias[item] += 1
        else:
            frequencias[item] = 1
    return frequencias


def mais_frequente(lista):
    """Valor mais frequente; em empate, o que apareceu primeiro.
    Lista nao vazia."""
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


def primeiro_unico(lista):
    """Primeiro valor que aparece uma unica vez, ou None. Use dicionario."""
    frequencias = {}
    for item in lista:
        if item in frequencias:
            frequencias[item] += 1
        else:
            frequencias[item] = 1

    for item in lista:
        if frequencias[item] == 1:
            return item

    return None

