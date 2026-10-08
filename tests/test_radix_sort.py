"""
Testes unitários para o Radix Sort LSD.
"""

import unittest
from lextrack_sorting import radix_sort


class TestRadixSort(unittest.TestCase):

    def test_radix_sort_empty_and_single(self):
        self.assertEqual(radix_sort([]), [])
        self.assertEqual(radix_sort([100]), [100])

    def test_radix_sort_positive_integers(self):
        dados = [170, 45, 75, 90, 802, 24, 2, 66]
        esperado = sorted(dados)
        self.assertEqual(radix_sort(dados), esperado)

    def test_radix_sort_with_negatives_and_zero(self):
        dados = [-5, 23, 0, -100, 42, -1, 15, -5]
        esperado = sorted(dados)
        self.assertEqual(radix_sort(dados), esperado)

    def test_radix_sort_reverse(self):
        dados = [2020, 2024, 2019, 2026, 2022]
        esperado = sorted(dados, reverse=True)
        self.assertEqual(radix_sort(dados, reverse=True), esperado)

    def test_radix_sort_custom_key_and_stability(self):
        """
        Simula a ordenação de gaps de coleta do LexTrack por ano (decrescente),
        preservando a ordem de inserção original para anos iguais.
        """
        gaps = [
            {"ano": 2024, "tipo": "PL", "fonte": "camara"},
            {"ano": 2026, "tipo": "PL", "fonte": "camara"},
            {"ano": 2024, "tipo": "PEC", "fonte": "senado"},
            {"ano": 2025, "tipo": "MPV", "fonte": "camara"},
            {"ano": 2026, "tipo": "PLP", "fonte": "senado"},
        ]

        ordenados = radix_sort(gaps, key=lambda g: g["ano"], reverse=True)

        # Anos devem ser 2026, 2026, 2025, 2024, 2024
        anos = [g["ano"] for g in ordenados]
        self.assertEqual(anos, [2026, 2026, 2025, 2024, 2024])

        # Estabilidade para 2026: camara deve vir antes de senado
        fontes_2026 = [g["fonte"] for g in ordenados if g["ano"] == 2026]
        self.assertEqual(fontes_2026, ["camara", "senado"])

        # Estabilidade para 2024: camara deve vir antes de senado
        fontes_2024 = [g["fonte"] for g in ordenados if g["ano"] == 2024]
        self.assertEqual(fontes_2024, ["camara", "senado"])


if __name__ == "__main__":
    unittest.main()
