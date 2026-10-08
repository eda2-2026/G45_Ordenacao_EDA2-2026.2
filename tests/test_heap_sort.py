"""
Testes unitários para o Heap Sort.
"""

import unittest

from lextrack_sorting import heap_sort


class TestHeapSort(unittest.TestCase):

    def test_heap_sort_empty_and_single(self):
        self.assertEqual(heap_sort([]), [])
        self.assertEqual(heap_sort([7]), [7])

    def test_heap_sort_numbers(self):
        dados = [12, 11, 13, 5, 6, 7, -2, 0]
        esperado = sorted(dados)
        self.assertEqual(heap_sort(dados), esperado)

    def test_heap_sort_reverse(self):
        dados = [12, 11, 13, 5, 6, 7, -2, 0]
        esperado = sorted(dados, reverse=True)
        self.assertEqual(heap_sort(dados, reverse=True), esperado)

    def test_heap_sort_custom_key(self):
        dados = ["banana", "pera", "uva", "abacaxi", "kiwi"]
        esperado = sorted(dados, key=len)
        self.assertEqual(heap_sort(dados, key=len), esperado)

    def test_heap_sort_dashboard_gargalos(self):
        """
        Simula a ordenação do endpoint de gargalos do LexTrack:
        taxaAtraso decrescente, mantendo a ordem original se as taxas forem iguais.
        """
        gargalos = [
            {"orgao": "CCJC", "taxaAtraso": 45, "tempo": 12.0},
            {"orgao": "CFT", "taxaAtraso": 80, "tempo": 18.5},
            {"orgao": "PLEN", "taxaAtraso": 45, "tempo": 6.2},
            {"orgao": "MESA", "taxaAtraso": 10, "tempo": 2.1},
        ]

        ordenados = heap_sort(gargalos, key=lambda g: g["taxaAtraso"], reverse=True)

        taxas = [g["taxaAtraso"] for g in ordenados]
        self.assertEqual(taxas, [80, 45, 45, 10])

        # Desempate estável no 45: CCJC apareceu antes de PLEN no input
        orgaos_45 = [g["orgao"] for g in ordenados if g["taxaAtraso"] == 45]
        self.assertEqual(orgaos_45, ["CCJC", "PLEN"])


if __name__ == "__main__":
    unittest.main()
