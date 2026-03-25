# 🤖 Impacto da IA Generativa nas Ocupações Brasileiras (2024)
Este projeto realiza uma análise de dados para estimar o grau de exposição e o impacto da Inteligência Artificial Generativa no mercado de trabalho brasileiro. Utilizando dados de vínculos empregatícios formais e uma matriz de classificação de impacto por ocupação, o script projeta o cenário atual de automação e transformação do trabalho.

# 🎯 Objetivo do Projeto
Mapear e quantificar o impacto da IA nas diferentes profissões do Brasil, respondendo a perguntas como:

Qual o percentual da força de trabalho brasileira altamente exposta à IA Generativa?

Quais são as top 10 ocupações mais impactadas dentro de cada nível (gradiente) de exposição?

Como esse impacto se distribui geograficamente (por Estado/UF)?

# 🗂️ Fontes de Dados
O projeto cruza duas bases de dados principais:

Dados de Emprego (RAIS 2024): Extraídos via BigQuery através da plataforma Base dos Dados, contendo o volume de vínculos ativos agrupados por CBO (Classificação Brasileira de Ocupações) e Unidade da Federação (UF).

Matriz de Exposição à IA: Uma base própria de classificação que divide os CBOs em 4 "Gradientes" distintos, baseados no potencial de automação ou assistência da IA Generativa nas tarefas do dia a dia.

# ⚙️ Tecnologias Utilizadas
Linguagem: Python

Bibliotecas: pandas (para manipulação e agregação dos dados)

Banco de Dados/SQL: Google BigQuery (para extração inicial dos microdados)

# 📊 Principais Análises Realizadas
O script Python (estimativa_impacto.py) automatiza o seguinte pipeline de dados:

Limpeza e Padronização: Conversão de chaves de cruzamento (CBOs) e tratamento de valores nulos.

Agregação Nacional: Cálculo do volume total e do percentual da força de trabalho alocada em cada um dos 4 Gradientes de impacto da IA.

Ranking de Ocupações: Recorte das 10 profissões com maior número de vínculos dentro de cada gradiente.

Distribuição Geográfica: Cálculo do percentual de impacto relativo por Estado, revelando quais regiões possuem uma matriz de trabalho mais vulnerável ou adaptável à IA.

# 🚀 Como Executar o Projeto
Clone este repositório:

Bash
git clone https://github.com/pbelushi/AI_generative_impact_jobs.git
Instale as dependências necessárias:

Bash
pip install pandas
Garanta que os arquivos de dados (CSVs) estejam na pasta Data/.

Execute o script principal:

Bash
python script/estimativa_impacto.py
(Nota: Os arquivos CSV de origem foram omitidos/adicionados ao .gitignore devido ao tamanho, mas as consultas SQL utilizadas para gerá-los estão documentadas no projeto).
