"""
Implementação do algoritmo Radix Sort (LSD - Least Significant Digit).

Complexidade de Tempo: O(N * K), onde K é o número de dígitos da maior chave.
Complexidade de Espaço: O(N + Base) para os baldes auxiliares do counting sort.
Propriedade: Estável por definição de LSD.
Ideal para ordenação não-comparativa de números inteiros (IDs, anos, contadores).
"""

from typing import Any, Callable, Iterable, TypeVar

T = TypeVar("T")


def radix_sort(
    items: Iterable[T],
    *,
    key: Callable[[T], int] | None = None,
    reverse: bool = False,
) -> list[T]:
    """
    Ordena uma coleção com base em chaves inteiras utilizando Radix Sort LSD.
    Suporta inteiros positivos, negativos e zero.

    Args:
        items: Elementos a ordenar.
        key: Função que mapeia cada item a um inteiro. Se None, o próprio item deve ser int.
        reverse: Se True, retorna em ordem decrescente mantendo estabilidade.
    """
    arr = list(items)
    if len(arr) <= 1:
        return arr

    key_fn: Callable[[T], int] = key if key is not None else (lambda x: int(x))

    # Separa em negativos e não-negativos para tratar sinal adequadamente
    negativos: list[T] = []
    nao_negativos: list[T] = []

    for item in arr:
        val = key_fn(item)
        if val < 0:
            negativos.append(item)
        else:
            nao_negativos.append(item)

    # Ordena não-negativos diretamente por Radix Sort LSD
    nao_negativos_ord = _radix_sort_non_negative(nao_negativos, key_fn)

    # Para negativos: invertemos o valor absoluto (-val), ordenamos e depois invertemos a lista
    # Ex: [-10, -2]. Chaves absolutas: [10, 2].
    # Ordenado por abs: [-2 (chave 2), -10 (chave 10)]
    # Invertido: [-10, -2] (ordem crescente correta)
    if negativos:
        # Note que queremos manter a estabilidade relativa para números com mesmo valor negativo
        negativos_ord = _radix_sort_non_negative(negativos, lambda x: -key_fn(x))
        negativos_ord.reverse()
    else:
        negativos_ord = []

    resultado = negativos_ord + nao_negativos_ord
    if reverse:
        resultado.reverse()
    return resultado


def _radix_sort_non_negative(items: list[T], key_fn: Callable[[T], int]) -> list[T]:
    """Ordena itens com chaves inteiras >= 0 utilizando Counting Sort dígito a dígito."""
    if len(items) <= 1:
        return list(items)

    max_val = max(key_fn(x) for x in items)
    if max_val == 0:
        return list(items)

    exp = 1
    current = list(items)
    n = len(current)

    while max_val // exp > 0:
        # Counting sort estável no dígito (current_val // exp) % 10
        output: list[T | None] = [None] * n
        count = [0] * 10

        for item in current:
            digito = (key_fn(item) // exp) % 10
            count[digito] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        # Itera de trás para frente para garantir estabilidade estrita
        for i in range(n - 1, -1, -1):
            item = current[i]
            digito = (key_fn(item) // exp) % 10
            pos = count[digito] - 1
            output[pos] = item
            count[digito] -= 1

        current = [x for x in output if x is not None]
        exp *= 10

    return current
