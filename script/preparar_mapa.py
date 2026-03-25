import pandas as pd
from pathlib import Path

# =========================================================================
# CONFIGURAÇÃO DE CAMINHOS
# =========================================================================
DIRETORIO_ATUAL = Path(__file__).parent 
DIRETORIO_RAIZ = DIRETORIO_ATUAL.parent 
PASTA_DADOS = DIRETORIO_RAIZ / "Data" 

# Carregar o resumo estadual gerado anteriormente
caminho_resumo = PASTA_DADOS / "Resumo_Impacto_IA_por_Estado_2024.csv"
df_estados = pd.read_csv(caminho_resumo, sep=';')

# =========================================================================
# FILTRAR E PREPARAR PARA O MAPA
# =========================================================================
# 1. Pegar apenas as linhas onde o Gradiente é igual a 4
df_g4 = df_estados[df_estados['Gradiente'] == 'Gradiente 4'].copy()

# 2. Selecionar as colunas úteis para o Datawrapper
# Mantivemos o total de vínculos para você colocar como "Tooltip" (balãozinho de informação) ao passar o mouse no mapa!
df_mapa = df_g4[['sigla_uf', 'percentual_no_estado (%)', 'total_vinculos_ativos']]

# 3. Renomear as colunas para ficarem bonitas no mapa do Datawrapper
df_mapa = df_mapa.rename(columns={
    'sigla_uf': 'Estado',
    'percentual_no_estado (%)': 'Impacto (%)',
    'total_vinculos_ativos': 'Total de Vínculos'
})

# =========================================================================
# SALVAR E EXIBIR
# =========================================================================
# Salvar um CSV caso você prefira fazer upload no Datawrapper
caminho_mapa = PASTA_DADOS / "Dados_Mapa_Datawrapper_G4.csv"
df_mapa.to_csv(caminho_mapa, index=False, sep='\t', encoding='utf-8-sig')

print("✅ Dados filtrados! Copie a tabela abaixo e cole no Datawrapper:\n")

# O to_string() imprime a tabela formatada, perfeita para copiar e colar
print(df_mapa.to_string(index=False))