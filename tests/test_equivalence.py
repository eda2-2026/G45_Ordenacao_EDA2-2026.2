"""
Testes de equivalência sistemática contra Python sorted() usando geradores pseudoaleatórios.
Valida corretude de todos os algoritmos para entradas aleatórias, invertidas e com duplicatas.
"""

import random
import unittest

from lextrack_sorting import heap_sort, merge_sort, quick_sort, radix_sort


class TestEquivalence(unittest.TestCase):

    def setUp(self):
        # Semente fixa para reprodutibilidade estrita
        self.rng = random.Random(2026)

    def test_all_algorithms_on_random_integers(self):
        for size in [0, 1, 5, 50, 500]:
            dados = [self.rng.randint(-1000, 1000) for _ in range(size)]
            esperado = sorted(dados)

            self.assertEqual(merge_sort(dados), esperado)
            self.assertEqual(radix_sort(dados), esperado)
            self.assertEqual(heap_sort(dados), esperado)
            self.assertEqual(quick_sort(dados), esperado)

    def test_all_algorithms_reverse_integers(self):
        dados = [self.rng.randint(-500, 500) for _ in range(200)]
        esperado = sorted(dados, reverse=True)

        self.assertEqual(merge_sort(dados, reverse=True), esperado)
        self.assertEqual(radix_sort(dados, reverse=True), esperado)
        self.assertEqual(heap_sort(dados, reverse=True), esperado)
        self.assertEqual(quick_sort(dados, reverse=True), esperado)

    def test_all_algorithms_many_duplicates(self):
        """Testa comportamento quando há grande repetição de valores (poucas chaves únicas)."""
        dados = [self.rng.choice([1, 2, 3, 4, 5]) for _ in range(300)]
        esperado = sorted(dados)

        self.assertEqual(merge_sort(dados), esperado)
        self.assertEqual(radix_sort(dados), esperado)
        self.assertEqual(heap_sort(dados), esperado)
        self.assertEqual(quick_sort(dados), esperado)

    def test_stability_parity_with_python_sorted(self):
        """
        Garante que para elementos com chaves repetidas, todos os 4 algoritmos
        produzem exatamente a mesma ordem que o sorted() padrão do CPython.
        """
        # Itens com chaves inteiras entre 1 e 5 e IDs sequenciais de 0 a 199
        itens = [{"chave": self.rng.randint(1, 5), "id": i} for i in range(200)]
        esperado = sorted(itens, key=lambda x: x["chave"])

        self.assertEqual(merge_sort(itens, key=lambda x: x["chave"]), esperado)
        self.assertEqual(radix_sort(itens, key=lambda x: x["chave"]), esperado)
        self.assertEqual(heap_sort(itens, key=lambda x: x["chave"]), esperado)
        self.assertEqual(quick_sort(itens, key=lambda x: x["chave"]), esperado)


if __name__ == "__main__":
    unittest.main()
