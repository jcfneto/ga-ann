import numpy as np


def start_population(k: int, D: int, n: int) -> np.array:
    """
    Inicializa de forma aleatória a população de indivíduos.

    Args:
        k: Número de bits para representar cada variável.
        D: Dimensão do problema.
        n: Número de indivíduos na população.
    """
    pop = [np.random.randint(0, 2, k * D) for _ in range(n)]
    return np.array(pop)


def binary_to_decimal(population: np.array, k: int, D: int,
                      search_range: list) -> np.array:
    """
    Converte os valores binários de cada variável em valores decimais.

    Args:
        population: Matriz contendo a população dos indivíduos.
        k: Número de bits para representar cada variável.
        D: Dimensão do problema.
        search_range: Intervalo de busca para cada variável.
    """
    pop_decimal = []
    for chrom in population:
        d = []
        bit_string = ''.join([str(i) for i in chrom])
        for i in range(D):
            di = int(bit_string[i * k:k * (i + 1)], 2)
            di = search_range[i][0] + di * (search_range[i][1] -
                                            search_range[i][0]) / (2 ** k - 1)
            d.append(di)
        pop_decimal.append(d)
    return np.array(pop_decimal)
