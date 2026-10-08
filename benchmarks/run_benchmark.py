#!/usr/bin/env python3
"""
Benchmark empírico de tempo de execução entre MergeSort, RadixSort, HeapSort,
QuickSort e o baseline do CPython (Timsort em C).

Avalia diferentes tamanhos de entrada (N = 100, 1.000, 5.000, 10.000)
e três distribuições de dados:
  1. Aleatória (Random)
  2. Já ordenada (Sorted)
  3. Invertida (Reversed)
"""

import random
import time
from typing import Callable, Sequence

from lextrack_sorting import heap_sort, merge_sort, quick_sort, radix_sort


def medir_tempo_ms(algoritmo: Callable[[Sequence[int]], list[int]], dados: list[int], repeticoes: int = 3) -> float:
    """Executa o algoritmo 'repeticoes' vezes sobre cópias da lista e retorna o tempo médio em milissegundos."""
    tempos = []
    for _ in range(repeticoes):
        copia = list(dados)
        t0 = time.perf_counter()
        _ = algoritmo(copia)
        t1 = time.perf_counter()
        tempos.append((t1 - t0) * 1000.0)
    return sum(tempos) / len(tempos)


def executar_benchmarks():
    tamanhos = [100, 1000, 5000, 10000]
    algoritmos = [
        ("MergeSort", merge_sort),
        ("RadixSort", radix_sort),
        ("HeapSort", heap_sort),
        ("QuickSort", quick_sort),
        ("CPython (Timsort)", sorted),
    ]

    rng = random.Random(2026)

    print("=" * 82)
    print("           BENCHMARK EMPÍRICO DE ALGORITMOS DE ORDENAÇÃO (G45 / EDA2)")
    print("=" * 82)

    for tamanho in tamanhos:
        print(f"\n>>> TAMANHO DO DATASET: N = {tamanho:,} elementos")
        print("-" * 82)
        print(f"{'Algoritmo':<22} | {'Aleatório (ms)':<15} | {'Já Ordenado (ms)':<17} | {'Invertido (ms)':<15}")
        print("-" * 82)

        # Gera distribuições
        base_random = [rng.randint(0, 100000) for _ in range(tamanho)]
        base_sorted = sorted(base_random)
        base_reversed = list(reversed(base_sorted))

        for nome, fn in algoritmos:
            t_rand = medir_tempo_ms(fn, base_random)
            t_sort = medir_tempo_ms(fn, base_sorted)
            t_rev = medir_tempo_ms(fn, base_reversed)

            print(f"{nome:<22} | {t_rand:>15.3f} | {t_sort:>17.3f} | {t_rev:>15.3f}")

    print("=" * 82)
    print("Observação: Os algoritmos implementados são em Python puro de alto nível;")
    print("o Timsort nativo roda compilado em C dentro da máquina virtual CPython.")
    print("=" * 82)


if __name__ == "__main__":
    executar_benchmarks()
