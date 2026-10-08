"""
Testes unitários para o algoritmo Merge Sort, compatíveis com unittest e pytest.
"""

import unittest
from lextrack_sorting import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_merge_sort_empty_and_single(self):
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([42]), [42])

    def test_merge_sort_numbers(self):
        dados = [9, 3, 7, 1, 5, 2, 8, 4, 6, 0]
        esperado = sorted(dados)
        self.assertEqual(merge_sort(dados), esperado)

    def test_merge_sort_reverse(self):
        dados = [9, 3, 7, 1, 5, 2, 8, 4, 6, 0]
        esperado = sorted(dados, reverse=True)
        self.assertEqual(merge_sort(dados, reverse=True), esperado)

    def test_merge_sort_custom_key(self):
        dados = ["banana", "uva", "abacaxi", "kiwi", "figo"]
        esperado = sorted(dados, key=len)
        self.assertEqual(merge_sort(dados, key=len), esperado)

    def test_merge_sort_strict_stability(self):
        """
        Testa que elementos com mesma chave preservam estritamente a ordem de inserção original.
        Simula eventos legislativos na mesma data com IDs distintos.
        """
        eventos = [
            {"data": "2026-05-10", "id": 1, "tipo": "Parecer"},
            {"data": "2026-05-08", "id": 2, "tipo": "Apresentação"},
            {"data": "2026-05-10", "id": 3, "tipo": "Votação"},
            {"data": "2026-05-09", "id": 4, "tipo": "Distribuição"},
            {"data": "2026-05-10", "id": 5, "tipo": "Despacho"},
        ]

        ordenados = merge_sort(eventos, key=lambda e: e["data"])

        # Elementos do dia 2026-05-10 devem manter rigorosamente a ordem 1, 3, 5
        ids_dia_10 = [e["id"] for e in ordenados if e["data"] == "2026-05-10"]
        self.assertEqual(ids_dia_10, [1, 3, 5])

    def test_merge_sort_composite_key(self):
        """Testa ordenação com chave composta (data, sequencia)."""
        eventos = [
            {"data": "2026-06-01", "seq": 3},
            {"data": "2026-06-01", "seq": 1},
            {"data": "2026-05-30", "seq": 2},
            {"data": "2026-06-01", "seq": 2},
        ]
        esperado = sorted(eventos, key=lambda x: (x["data"], x["seq"]))
        self.assertEqual(merge_sort(eventos, key=lambda x: (x["data"], x["seq"])), esperado)


if __name__ == "__main__":
    unittest.main()
