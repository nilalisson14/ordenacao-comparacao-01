import sys
from insertion_sort import insertion_sort
from selection_sort import selection_sort


def converter_argumentos_em_lista(argumentos):
    try:
        return [int(x) for x in argumentos]
    except ValueError:
        print("Erro: todos os valores da lista devem ser números inteiros.")
        sys.exit(1)


def main():
    if len(sys.argv) < 3:
        print("Uso:")
        print("python main.py insertion 5 3 1 4 2")
        print("python main.py selection 5 3 1 4 2")
        sys.exit(1)

    algoritmo = sys.argv[1].lower()
    numeros = converter_argumentos_em_lista(sys.argv[2:])

    if algoritmo == "insertion":
        resultado = insertion_sort(numeros)
    elif algoritmo == "selection":
        resultado = selection_sort(numeros)
    else:
        print("Erro: algoritmo inválido.")
        print("Use 'insertion' ou 'selection'.")
        sys.exit(1)

    print("Lista original :", numeros)
    print("Lista ordenada :", resultado)


if __name__ == "__main__":
    main()