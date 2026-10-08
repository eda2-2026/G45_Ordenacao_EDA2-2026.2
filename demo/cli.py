#!/usr/bin/env python3
"""
Demonstração CLI interativa dos algoritmos de ordenação aplicados a dados reais do LexTrack.
Permite ordenar eventos de tramitação de proposições legislativas por diferentes critérios
e comparar o resultado visualmente no terminal.
"""

from lextrack_sorting import heap_sort, merge_sort, quick_sort, radix_sort

# Amostra realista de eventos de tramitação de uma PEC legislativa no Congresso Nacional
EVENTOS_EXEMPLO = [
    {
        "proposicaoId": "PEC-45-2019",
        "dataEvento": "2026-05-12T14:30:00",
        "sequencia": 4,
        "siglaOrgao": "PLEN",
        "descricao": "Aprovação em segundo turno no Plenário da Câmara dos Deputados",
    },
    {
        "proposicaoId": "PEC-45-2019",
        "dataEvento": "2026-03-01T10:00:00",
        "sequencia": 1,
        "siglaOrgao": "MESA",
        "descricao": "Apresentação da Proposta de Emenda à Constituição",
    },
    {
        "proposicaoId": "PEC-45-2019",
        "dataEvento": "2026-04-15T09:00:00",
        "sequencia": 2,
        "siglaOrgao": "CCJC",
        "descricao": "Designação de Relator na Comissão de Constituição e Justiça",
    },
    {
        "proposicaoId": "PEC-45-2019",
        "dataEvento": "2026-05-12T10:00:00",
        "sequencia": 3,
        "siglaOrgao": "PLEN",
        "descricao": "Aprovação em primeiro turno com substitutivo",
    },
    {
        "proposicaoId": "PEC-45-2019",
        "dataEvento": "2026-06-20T16:00:00",
        "sequencia": 5,
        "siglaOrgao": "SF-PLEN",
        "descricao": "Remessa ao Senado Federal para apreciação revisora",
    },
]


def imprimir_tabela_eventos(eventos: list[dict], titulo: str):
    print(f"\n📌 {titulo}")
    print("-" * 95)
    print(f"{'Seq':<4} | {'Data/Hora':<19} | {'Órgão':<8} | {'Descrição'}")
    print("-" * 95)
    for ev in eventos:
        print(f"{ev['sequencia']:<4} | {ev['dataEvento']:<19} | {ev['siglaOrgao']:<8} | {ev['descricao'][:55]}")
    print("-" * 95)


def main():
    print("=" * 95)
    print("      DEMONSTRAÇÃO CLI — ORDENAÇÃO DE EVENTOS LEGISLATIVOS (LEXTRACK / EDA2)")
    print("=" * 95)

    imprimir_tabela_eventos(EVENTOS_EXEMPLO, "Entrada Original Desordenada")

    # 1. Merge Sort estável por Data e Sequência (como no ListarMovimentacoesService)
    ordenados_merge = merge_sort(
        EVENTOS_EXEMPLO,
        key=lambda e: (e["dataEvento"], e["sequencia"]),
    )
    imprimir_tabela_eventos(
        ordenados_merge,
        "Ordenado por MergeSort (Estável: Cronológico + Sequencial)",
    )

    # 2. Radix Sort por Sequência
    ordenados_radix = radix_sort(
        EVENTOS_EXEMPLO,
        key=lambda e: e["sequencia"],
    )
    imprimir_tabela_eventos(
        ordenados_radix,
        "Ordenado por RadixSort LSD (Chave inteira: Sequência do Evento)",
    )

    # 3. Quick Sort reverso por Sequência (linha do tempo retrospectiva)
    ordenados_quick_rev = quick_sort(
        EVENTOS_EXEMPLO,
        key=lambda e: e["sequencia"],
        reverse=True,
    )
    imprimir_tabela_eventos(
        ordenados_quick_rev,
        "Ordenado por QuickSort Reverso (Eventos mais recentes primeiro)",
    )

    print("\n✅ Demonstração concluída com sucesso!")


if __name__ == "__main__":
    main()
