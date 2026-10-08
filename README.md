# G45 - Algoritmos de Ordenação Multicritério aplicados ao LexTrack

Repositório dedicado ao Trabalho 2 (Algoritmos de Ordenação) da disciplina de **Estruturas de Dados 2 (EDA2)** da Universidade de Brasília (UnB), semestre **2026.2**, ministrada pelo Prof. Maurício Serrano.

## 👥 Aluno
* **Nome:** Caio Martins
* **Matrícula:** 231011168
* **GitHub:** [@caioflmjr](https://github.com/caioflmjr)
* **Grupo:** G45 (Trabalho Individual)

---

## 🎯 Contexto e Problema do Mundo Real: LexTrack

O **LexTrack** ([unb-mds/2026-1-Squad13](https://github.com/unb-mds/2026-1-Squad13)) é uma plataforma em produção desenvolvida na UnB para monitoramento e análise analítica do fluxo de tramitação legislativa de proposições no Congresso Nacional (Câmara dos Deputados e Senado Federal).

Em sistemas dessa natureza, o backend frequentemente manipula coleções em memória provenientes de consultas a APIs externas e agregações estatísticas. A escolha de algoritmos de ordenação adequados é essencial para garantir propriedades matemáticas indispensáveis:
1. **Histórico e Linha do Tempo de Tramitação:** Eventos unificados de múltiplas fontes podem ocorrer na mesma data (`dataEvento`). Preservar a ordem temporal e sequencial original (`sequencia`) exige algoritmos com **garantia formal de estabilidade**, evitando inversões de causalidade no histórico legislativo.
2. **Priorização de Coleta e Gaps:** Lotes de proposições com chaves numéricas fixas (`ano`) processados por rotinas em background exigem ordenação rápida e estável.
3. **Métricas de Gargalos e Rankings no Dashboard:** Ranqueamento de taxas de atraso e indicadores por órgão demandam extração precisa de prioridades.

Este projeto implementou 4 algoritmos clássicos do zero em Python puro, com interfaces compatíveis com funções de ordem superior (`key=`, `reverse=`), sendo integrado diretamente aos serviços de negócio do LexTrack via Pull Request.

---

## 🧩 Algoritmos Implementados e Motivação Técnica

| Algoritmo | Complexidade (Médio / Pior) | Estabilidade | Motivação e Aplicação Real no LexTrack |
| :--- | :---: | :---: | :--- |
| **Merge Sort** | $\mathcal{O}(N \log N)$ / $\mathcal{O}(N \log N)$ | **Estável** | **Eventos de Tramitação e Fases:** Utilizado em `ListarMovimentacoesService`, `AgregarPorFaseService` e `calcular_tempo_por_fase`. A estabilidade estrita garante que eventos ocorridos na mesma data preservem sua precedência original. |
| **Radix Sort (LSD)** | $\mathcal{O}(N \cdot K)$ / $\mathcal{O}(N \cdot K)$ | **Estável** | **Priorização de Gaps de Coleta:** Utilizado em `ColetarEmLoteService`. Como as chaves de gap são anos (inteiros de 4 dígitos), a ordenação dígito a dígito do Radix Sort supera o limite inferior $\Omega(N \log N)$ de comparações diretas. |
| **Heap Sort** | $\mathcal{O}(N \log N)$ / $\mathcal{O}(N \log N)$ | Estabilizado por índice | **Ranking de Gargalos Institucionais:** Utilizado em `SqlDashboardRepository` para ranquear órgãos legislativos pela `taxaAtraso`. Evita degradação quadrática de tempo. |
| **Quick Sort (Mediana de 3)** | $\mathcal{O}(N \log N)$ / $\mathcal{O}(N^2)$ | Estabilizado por índice | **Comparação de Temas no Dashboard:** Utilizado em `DashboardService` para classificar o tempo médio de tramitação por tema. O pivô por mediana de três mitiga o risco de pior caso em entradas parcialmente ordenadas. |

---

## 📊 Benchmark Empírico

Os testes de desempenho foram executados comparando as quatro implementações puras contra o `sorted()` nativo do CPython (Timsort em C).

### Tempos Médios de Execução (Milissegundos - ms)

#### 1. Entrada Aleatória (Random)
| Tamanho (N) | MergeSort (ms) | RadixSort (ms) | HeapSort (ms) | QuickSort (ms) | CPython Timsort (ms) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **100** | 0.138 | 0.313 | 0.206 | 0.165 | 0.005 |
| **1.000** | 1.192 | 2.244 | 1.944 | 1.251 | 0.075 |
| **5.000** | 6.882 | 7.966 | 12.213 | 7.684 | 0.487 |
| **10.000** | 17.824 | 17.788 | 26.312 | 15.275 | 1.033 |

#### 2. Entrada Já Ordenada (Sorted)
| Tamanho (N) | MergeSort (ms) | RadixSort (ms) | HeapSort (ms) | QuickSort (ms) | CPython Timsort (ms) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **100** | 0.101 | 0.147 | 0.119 | 0.070 | 0.001 |
| **1.000** | 0.888 | 1.695 | 1.896 | 0.852 | 0.005 |
| **5.000** | 5.776 | 7.722 | 11.987 | 5.312 | 0.026 |
| **10.000** | 11.347 | 15.377 | 26.152 | 11.647 | 0.037 |

#### 3. Entrada Invertida (Reversed)
| Tamanho (N) | MergeSort (ms) | RadixSort (ms) | HeapSort (ms) | QuickSort (ms) | CPython Timsort (ms) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **100** | 0.121 | 0.150 | 0.099 | 0.063 | 0.001 |
| **1.000** | 1.342 | 1.579 | 1.715 | 0.868 | 0.006 |
| **5.000** | 5.665 | 7.693 | 10.481 | 5.221 | 0.032 |
| **10.000** | 11.130 | 16.430 | 23.799 | 11.040 | 0.051 |

> **Nota de Rigor Técnico:** As implementações deste repositório foram escritas em Python puro de alto nível para fins pedagógicos e de estudo analítico de estruturas. O `sorted()` do CPython é compilado diretamente em linguagem C; logo, a justificativa para a aplicação em produção apoia-se em garantias determinísticas de estabilidade, controle estrito do desempate por índice e aplicação de Radix Sort sobre chaves inteiras uniformes.

---

## 🚀 Como Executar Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/eda2-2026/G45_Ordenacao_EDA2-2026.2.git
cd G45_Ordenacao_EDA2-2026.2
```

### 2. Executar a Suíte de Testes Automatizados (26 testes)
```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p "test_*.py" -v
```

### 3. Executar o Benchmark Empírico
```bash
PYTHONPATH=src python3 benchmarks/run_benchmark.py
```

### 4. Executar a Demonstração CLI Interativa
```bash
PYTHONPATH=src python3 demo/cli.py
```

---

## 🔗 Integração Real com o Software LexTrack (Menção SS)

O módulo desenvolvido neste trabalho foi incorporado ao repositório central da plataforma LexTrack:

* **Repositório LexTrack:** [unb-mds/2026-1-Squad13](https://github.com/unb-mds/2026-1-Squad13)
* **Pull Request de Integração:** [PR #321 — feat(sort): integra modulo de ordenacao customizado para o fluxo legislativo (EDA2)](https://github.com/unb-mds/2026-1-Squad13/pull/321)
* **Branch:** `feat/ordenacao-algoritmos-eda2` direcionada para `develop`
