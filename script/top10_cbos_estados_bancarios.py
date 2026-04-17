import pandas as pd
from pathlib import Path

# =========================================================================
# CONFIGURAÇÃO DE CAMINHOS
# =========================================================================
DIRETORIO_ATUAL = Path(__file__).parent 
DIRETORIO_RAIZ = DIRETORIO_ATUAL.parent 
PASTA_DADOS = DIRETORIO_RAIZ / "Data"

# =========================================================================
# CARREGAR DADOS
# =========================================================================
caminho_classificacao = PASTA_DADOS / "CBOs por exposição à IA generativa - Página1 (1).csv"
caminho_rais = PASTA_DADOS / "vinculos_cbo_bancarios_uf.csv"

df_classificacao = pd.read_csv(caminho_classificacao)
df_rais_estados = pd.read_csv(caminho_rais)

# =========================================================================
# LIMPEZA E TRATAMENTO
# =========================================================================
if 'sigla_uf' in df_rais_estados.columns:
    df_rais_estados['sigla_uf'] = df_rais_estados['sigla_uf'].astype(str).str.strip().str.upper()

df_classificacao['Código CBO'] = df_classificacao['Código CBO'].astype(str).str.replace('.0', '', regex=False).str.strip().str.zfill(4)
df_rais_estados['codigo_cbo_4'] = df_rais_estados['codigo_cbo_4'].astype(str).str.replace('.0', '', regex=False).str.strip().str.zfill(4)

# Cruzamento com RIGHT JOIN para manter o Gradiente 0
df_impacto = pd.merge(
    df_classificacao, 
    df_rais_estados, 
    left_on='Código CBO', 
    right_on='codigo_cbo_4', 
    how='right' 
)

# Preencher os vazios do Gradiente 0
df_impacto['Gradiente'] = df_impacto['Gradiente'].fillna('0')
df_impacto['Código CBO'] = df_impacto['Código CBO'].fillna(df_impacto['codigo_cbo_4'])
df_impacto['Título da Família Ocupacional'] = df_impacto['Título da Família Ocupacional'].fillna('Não mapeado no estudo original')
df_impacto['total_vinculos_ativos'] = df_impacto['total_vinculos_ativos'].fillna(0)

# =========================================================================
# EXTRAIR O TOP 10 POR ESTADO E GRADIENTE
# =========================================================================
# 1. Ordenar primeiro por Estado (A-Z), depois por Gradiente, e então por volume de vínculos (Maior pro Menor)
df_ordenado = df_impacto.sort_values(by=['sigla_uf', 'Gradiente', 'total_vinculos_ativos'], ascending=[True, True, False])

# 2. Agrupar por Estado e Gradiente, pegando as 10 primeiras linhas de cada grupo
top_10_uf_gradiente = df_ordenado.groupby(['sigla_uf', 'Gradiente']).head(10)

# 3. Limpar colunas para o arquivo final
colunas_para_salvar = ['sigla_uf', 'Gradiente', 'Código CBO', 'Título da Família Ocupacional', 'total_vinculos_ativos']
top_10_limpo = top_10_uf_gradiente[colunas_para_salvar]

# =========================================================================
# SALVAR E EXIBIR
# =========================================================================
caminho_top10 = PASTA_DADOS / "Top_10_CBOs_por_Estado_e_Gradiente_bancarios.csv"
top_10_limpo.to_csv(caminho_top10, index=False, sep=';', encoding='utf-8-sig')

print(f"✅ Arquivo salvo com sucesso em: {caminho_top10}\n")

# Exibir na tela uma amostra (Top 3 do Gradiente 4 no Estado do Ceará, por exemplo)
amostra = top_10_limpo[(top_10_limpo['sigla_uf'] == 'CE') & (top_10_limpo['Gradiente'] == 'Gradiente 4')].head(3)
print("Amostra: Top 3 Profissões de Alta Exposição (Gradiente 4) no Ceará:")
print(amostra[['Código CBO', 'Título da Família Ocupacional', 'total_vinculos_ativos']])