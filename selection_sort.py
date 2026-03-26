def selection_sort(lista):
    lista = lista.copy()
    n = len(lista)

    for i in range(n):
        menor_indice = i

        for j in range(i + 1, n):
            if lista[j] < lista[menor_indice]:
                menor_indice = j

        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]

    return lista


if __name__ == "__main__":
    exemplo = [5, 3, 1, 4, 2]
    print("Lista original:", exemplo)
    print("Lista ordenada:", selection_sort(exemplo))