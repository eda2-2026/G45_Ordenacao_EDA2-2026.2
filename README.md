# G45 - Algoritmos de Ordenação Multicritério aplicados ao LexTrack

Repositório dedicado ao Trabalho 2 (Algoritmos de Ordenação) da disciplina de **Estruturas de Dados 2 (EDA2)** da Universidade de Brasília (UnB), semestre **2026.2**, ministrada pelo Prof. Maurício Serrano.

## 👥 Aluno
* **Nome:** Caio Martins
* **Matrícula:** 231011168
* **GitHub:** [@caioflmjr](https://github.com/caioflmjr)
* **Grupo:** G45

---

## 🎯 Contexto e Problema do Mundo Real: LexTrack

O **LexTrack** ([unb-mds/2026-1-Squad13](https://github.com/unb-mds/2026-1-Squad13)) é uma plataforma de monitoramento e análise do fluxo de tramitação legislativa de proposições do Congresso Nacional (Câmara dos Deputados e Senado Federal).

O sistema necessita lidar continuamente com eventos em memória que exigem garantias formais de ordenação:
1. **Histórico e Linha do Tempo de Tramitação:** Eventos unificados de múltiplas fontes (Câmara e Senado) podem ocorrer na mesma data (`dataEvento`). Preservar a ordem temporal e sequencial original (`sequencia`) exige algoritmos com **garantia estrita de estabilidade**.
2. **Priorização de Coleta e Gaps:** Lotes de proposições com chaves numéricas fixas (`ano`) processados por workers em background requerem ordenação não-comparativa rápida.
3. **Métricas de Gargalos e Rankings no Dashboard:** Ranqueamento de taxas de atraso e indicadores por órgão demandam extração de prioridades sem degradação quadrática.

Este módulo implementa algoritmos clássicos de ordenação do zero em Python puro, com interfaces padronizadas compatíveis com o comportamento de funções de ordem superior (`key=`, `reverse=`), sendo integrado diretamente aos serviços do LexTrack via Pull Request.

---

## 🧩 Algoritmos Implementados

| Algoritmo | Complexidade (Médio / Pior) | Estabilidade | Aplicação no LexTrack |
| :--- | :---: | :---: | :--- |
| **Merge Sort** | $\mathcal{O}(N \log N)$ / $\mathcal{O}(N \log N)$ | **Estável** | Ordenação de eventos de tramitação e transições de fases |
| **Radix Sort (LSD)** | $\mathcal{O}(N \cdot K)$ / $\mathcal{O}(N \cdot K)$ | **Estável** | Priorização e ordenação de lacunas de coleta por ano |
| **Heap Sort** | $\mathcal{O}(N \log N)$ / $\mathcal{O}(N \log N)$ | Estabilizado por índice | Ranqueamento de gargalos institucionais e atrasos |
| **Quick Sort (Mediana de 3)** | $\mathcal{O}(N \log N)$ / $\mathcal{O}(N^2)$ | Estabilizado por índice | Ordenação de indicadores médios por tema no dashboard |

---

## 🚀 Como Executar

### Pré-requisitos
* Python 3.11 ou superior instalado

### Instalação
```bash
git clone https://github.com/eda2-2026/G45_Ordenacao_EDA2-2026.2.git
cd G45_Ordenacao_EDA2-2026.2
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
```

### Executar Testes Automatizados
```bash
pytest -v
```

### Executar Verificação de Estilo / Lint
```bash
ruff check .
```

---

## 🔗 Integração com o Software LexTrack
* Repositório Principal: [unb-mds/2026-1-Squad13](https://github.com/unb-mds/2026-1-Squad13)
* Pull Request de Integração: *(em andamento)*
