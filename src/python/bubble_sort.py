""" Implementação do algoritmo bubble sort com recursão """


def bubble_sort(data, size):
    """
    Implementação de um algoritmo de ubble sort com recursão.

    Argumentos:
    data: lista. Lista que será ordenada
    size: int. Tamanho da lista

    Retorna a lista "data" ordenada.
    """
    swap = False
    for i in range(0, size - 1):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
            swap = True
    if swap:
        bubble_sort(data, size - 1)


if __name__ == '__main__':
    lista_nao_odenada = [2, 9, 8, 0, 1, 3, 5, 4, 6, 7]
    print(lista_nao_odenada)
    bubble_sort(lista_nao_odenada, len(lista_nao_odenada))
    print(lista_nao_odenada)
