"""
Testes unitários para o Quick Sort com pivô de mediana de três.
"""

import unittest

from lextrack_sorting import quick_sort


class TestQuickSort(unittest.TestCase):

    def test_quick_sort_empty_and_single(self):
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([10]), [10])

    def test_quick_sort_numbers(self):
        dados = [84, 12, 99, 3, 45, 23, 7, -5, 0]
        esperado = sorted(dados)
        self.assertEqual(quick_sort(dados), esperado)

    def test_quick_sort_reverse(self):
        dados = [84, 12, 99, 3, 45, 23, 7, -5, 0]
        esperado = sorted(dados, reverse=True)
        self.assertEqual(quick_sort(dados, reverse=True), esperado)

    def test_quick_sort_already_sorted_and_reversed(self):
        """Testa conjuntos que seriam o pior caso no QuickSort ingênuo."""
        crescente = list(range(100))
        decrescente = list(range(100, -1, -1))
        self.assertEqual(quick_sort(crescente), crescente)
        self.assertEqual(quick_sort(decrescente), sorted(decrescente))

    def test_quick_sort_identical_elements(self):
        dados = [42] * 50
        self.assertEqual(quick_sort(dados), dados)

    def test_quick_sort_dashboard_temas(self):
        """
        Simula a ordenação do endpoint de comparação de temas do LexTrack:
        ordena por tempoMedioDias ascendente.
        """
        temas = [
            {"tema": "Educação", "tempoMedioDias": 450, "velocidade": "medio"},
            {"tema": "Saúde", "tempoMedioDias": 220, "velocidade": "rapido"},
            {"tema": "Tributário", "tempoMedioDias": 890, "velocidade": "lento"},
            {"tema": "Segurança", "tempoMedioDias": 310, "velocidade": "medio"},
        ]

        ordenados = quick_sort(temas, key=lambda t: t["tempoMedioDias"])
        tempos = [t["tempoMedioDias"] for t in ordenados]
        self.assertEqual(tempos, [220, 310, 450, 890])
        self.assertEqual(ordenados[0]["tema"], "Saúde")
        self.assertEqual(ordenados[-1]["tema"], "Tributário")


if __name__ == "__main__":
    unittest.main()
