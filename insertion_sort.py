def insertion_sort(lista):
    lista = lista.copy()

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista


if __name__ == "__main__":
    exemplo = [5, 3, 1, 4, 2]
    print("Lista original:", exemplo)
    print("Lista ordenada:", insertion_sort(exemplo))