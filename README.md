# 🤖 Impacto da IA Generativa nas Ocupações Brasileiras (2024)

Este projeto realiza uma análise de dados em Python para estimar o grau de exposição e o impacto da Inteligência Artificial Generativa no mercado de trabalho brasileiro. Utilizando dados de vínculos empregatícios formais e uma matriz de classificação de impacto, o script projeta o cenário atual de automação e assistência no trabalho, tanto em nível nacional quanto estadual.

## 🎯 Objetivo do Projeto
Mapear e quantificar o impacto da IA nas diferentes profissões do Brasil, respondendo a perguntas como:
* Qual o percentual da força de trabalho brasileira altamente exposta à IA Generativa?
* Quais são as top 10 ocupações mais impactadas dentro de cada nível de exposição?
* Como esse impacto se distribui geograficamente pelas Unidades da Federação (UFs)?

## 🗺️ Distribuição Geográfica do Impacto
*(**Nota para o autor**: Cole aqui o link de compartilhamento (embed) do Datawrapper ou insira a imagem do mapa usando o formato `![Mapa de Impacto](link_da_imagem.png)`)*

## 🗂️ Fontes de Dados
O projeto cruza duas bases de dados principais:
1. **Dados de Emprego (RAIS 2024):** Extraídos via BigQuery através da plataforma [Base dos Dados](https://basedosdados.org/), contendo o volume de vínculos ativos agrupados por CBO (Classificação Brasileira de Ocupações) e UF.
2. **Matriz de Exposição à IA:** Uma base própria de classificação que divide os CBOs em 4 "Gradientes" distintos, baseados no potencial da IA Generativa em transformar as tarefas diárias.

## 📊 Principais Entregáveis (Outputs)
Os scripts automatizam o cruzamento, a limpeza e o cálculo de percentuais, gerando análises prontas para uso:
* `Resumo_Impacto_IA_2024.csv`: Consolidado nacional da exposição por gradiente.
* `Resumo_Impacto_IA_por_Estado_2024.csv`: Recorte geográfico com o percentual de impacto relativo dentro de cada estado.
* `Top_10_CBOs_por_Gradiente.csv`: Ranking das profissões com maior volume absoluto de trabalhadores em risco/transformação.

## ⚙️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas de Análise:** `pandas`
* **Arquitetura:** `pathlib` (para gestão de caminhos relativos, garantindo que o código rode em qualquer máquina).
* **Banco de Dados/SQL:** Google BigQuery
* **Visualização de Dados:** Datawrapper (https://datawrapper.dwcdn.net/cjuqo/1/)

## 🚀 Como Executar o Projeto

O projeto foi estruturado com caminhos relativos à prova de falhas. Você pode executá-lo de qualquer diretório.

1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/pbelushi/AI_generative_impact_jobs.git)
