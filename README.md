# Impacto da IA Generativa no Mercado de Trabalho Brasileiro: Recorte Setor Bancário e Financeiro

Este repositório contém um estudo detalhado sobre o impacto potencial da Inteligência Artificial Generativa (IAGen) nas ocupações do mercado de trabalho brasileiro, com um foco específico no setor de bancos, fintechs e arranjos de pagamento.

## 📊 Visão Geral do Projeto
A análise utiliza como base a metodologia de exposição ocupacional da Organização Internacional do Trabalho (OIT), especificamente o Working Paper 140 de maio de 2025: "Generative AI and Jobs: A Refined Global Index of Occupational Exposure".

Os dados de emprego são extraídos da base da RAIS (2024) via BigQuery, filtrando especificamente os CNAEs 64 (Serviços Financeiros) e 66 (Atividades Auxiliares) para o recorte bancário.

## 📝 Nota Metodológica: O "Ponto Cego" e o Gradiente 0
Um diferencial fundamental deste repositório é o tratamento de ocupações que não possuíam correspondência direta na matriz de exposição original da OIT.

* **Gradiente 0 (Não Mapeado/Baixa Exposição):** Durante o estudo, identificamos que ocupações críticas para o setor bancário — como Gerentes de Contas (CBO 2532) e Gerentes Financeiros (CBO 1421) — não constavam no mapeamento genérico de automação.

* **Barreiras de Automação:** Conforme corroborado pelo estudo da OIT, certas funções de alta complexidade ou responsabilidade legal (ex: Advogados e Engenheiros Civis) apresentam tarefas que a IAGen atual não pode assumir integralmente devido a barreiras regulatórias, de responsabilidade civil ou interação física.

* **Tratamento de Dados:** Para este estudo, todas as ocupações ativas na RAIS que não foram classificadas pelo índice global foram incluídas como Gradiente 0, garantindo que o volume total de trabalhadores seja contabilizado e que o impacto não seja subestimado ou distorcido.


## 📂 Estrutura do Repositório
**1. sql/**
Contém as consultas realizadas na Base dos Dados (BigQuery):

vinculos_cbo_bancarios.sql: Extrai o total de vínculos ativos por CBO no setor financeiro.

vinculos_cbo_bancarios_uf.sql: Segmenta os vínculos por Unidade Federativa.

**2. script/**
Scripts Python para processamento e análise:

estimativa_impacto_bancarios.py: Cruza os dados da RAIS com a matriz de classificação da OIT e gera o ranking de ocupações impactadas.

estimativa_impacto_bancarios_uf.py: Gera o resumo de impacto percentual por estado.

preparar_mapa_bancarios.py: Filtra os dados de "Alta Exposição" (Gradiente 4) para visualização no Datawrapper.

**3. Data/**
Arquivos CSV gerados e utilizados no estudo, incluindo o mapeamento consolidado de CBOs e os resultados finais de impacto por estado e por ocupação.

## 🚀 Como Executar
1. Execute as queries SQL na base de microdados da RAIS no BigQuery.
2. Salve os resultados na pasta Data/.
3. Execute estimativa_impacto_bancarios.py para obter o cenário nacional.
4. Execute estimativa_impacto_bancarios_uf.py para a visão estadual.
5. Utilize o output de preparar_mapa_bancarios.py para gerar mapas de calor.

## 📊 Principais Entregáveis (Outputs)
Os scripts automatizam o cruzamento, a limpeza e o cálculo de percentuais, gerando análises prontas para uso:
* `Resumo_Impacto_IA_2024.csv`: Consolidado nacional da exposição por gradiente.
* `Resumo_Impacto_IA_por_Estado_2024.csv`: Recorte geográfico com o percentual de impacto relativo dentro de cada estado.
* `Top_10_CBOs_por_Gradiente.csv`: Ranking das profissões com maior volume absoluto de trabalhadores em risco/transformação.

## 📄 Referências
Gmyrek, P., et al. (2025). Generative AI and Jobs: A Refined Global Index of Occupational Exposure. ILO Working Paper 140.
Dados de emprego: Microdados da RAIS (2024) via Base dos Dados.

