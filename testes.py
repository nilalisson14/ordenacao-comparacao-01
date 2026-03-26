from insertion_sort import insertion_sort
from selection_sort import selection_sort


def executar_testes():
    casos_de_teste = [
        [5, 3, 1, 4, 2],
        [10, 9, 8, 7, 6],
        [1, 2, 3, 4, 5],
        [4],
        [],
        [3, 1, 2, 3, 1]
    ]

    print("=== TESTES INSERTION SORT ===")
    for caso in casos_de_teste:
        print(f"Entrada: {caso} -> Saída: {insertion_sort(caso)}")

    print("\n=== TESTES SELECTION SORT ===")
    for caso in casos_de_teste:
        print(f"Entrada: {caso} -> Saída: {selection_sort(caso)}")


if __name__ == "__main__":
    executar_testes()