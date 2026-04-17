import pandas as pd
from pathlib import Path

# =========================================================================
# CONFIGURAÇÃO DE CAMINHOS (À prova de falhas)
# =========================================================================
# 1. Descobre a pasta onde ESTE script está guardado (pasta 'script')
DIRETORIO_ATUAL = Path(__file__).parent 

# 2. Volta uma pasta atrás para chegar à raiz do projeto
DIRETORIO_RAIZ = DIRETORIO_ATUAL.parent 

# 3. Entra na pasta 'Data'
PASTA_DADOS = DIRETORIO_RAIZ / "Data" 


# =========================================================================
# CARREGAR DADOS
# =========================================================================
# O pathlib permite usar a barra '/' para juntar caminhos de forma segura
caminho_classificacao = PASTA_DADOS / "CBOs por exposição à IA generativa - Página1 (1).csv"
caminho_rais = PASTA_DADOS / "vinculos_cbo_bancarios.csv"

df_classificacao = pd.read_csv(caminho_classificacao)
df_rais = pd.read_csv(caminho_rais)

# Converter a coluna de CBO para texto (string)
df_classificacao['Código CBO'] = df_classificacao['Código CBO'].astype(str)
df_rais['codigo_cbo_4'] = df_rais['codigo_cbo_4'].astype(str)

# Fazer o cruzamento (Merge) das bases
# MUDANÇA: 'how' alterado para 'right' para manter todos os CBOs da RAIS
df_impacto = pd.merge(
    df_classificacao, 
    df_rais, 
    left_on='Código CBO', 
    right_on='codigo_cbo_4', 
    how='right' 
)

# MUDANÇA: Preencher CBOs não classificados como Gradiente 0
df_impacto['Gradiente'] = df_impacto['Gradiente'].fillna(0)

# MUDANÇA: Garantir que a coluna 'Código CBO' não fique vazia (puxando o código da RAIS)
df_impacto['Código CBO'] = df_impacto['Código CBO'].fillna(df_impacto['codigo_cbo_4'])

df_impacto['total_vinculos_ativos'] = df_impacto['total_vinculos_ativos'].fillna(0)

# Calcular os totais agregados por Gradiente
resumo_impacto = df_impacto.groupby('Gradiente')['total_vinculos_ativos'].sum().reset_index()

# Calcular a percentagem
total_mapeado = resumo_impacto['total_vinculos_ativos'].sum()
resumo_impacto['percentual (%)'] = (resumo_impacto['total_vinculos_ativos'] / total_mapeado) * 100

# =========================================================================
# SALVAR OS ARQUIVOS
# =========================================================================
caminho_detalhado = PASTA_DADOS / "Estimativa_Detalhada_Impacto_IA_bancarios.csv"
caminho_resumo = PASTA_DADOS / "Resumo_Impacto_IA_bancarios.csv"

df_impacto.to_csv(caminho_detalhado, index=False, sep=';', encoding='utf-8-sig')
resumo_impacto.to_csv(caminho_resumo, index=False, sep=';', encoding='utf-8-sig')

# Levantar as 10 principais ocupações por Gradiente
df_ordenado = df_impacto.sort_values(by=['Gradiente', 'total_vinculos_ativos'], ascending=[True, False])
top_10_por_gradiente = df_ordenado.groupby('Gradiente').head(10)

# MUDANÇA: 'Título da Família Ocupacional' adicionado à lista
colunas_para_salvar = ['Gradiente', 'Código CBO', 'Título da Família Ocupacional', 'total_vinculos_ativos'] 
top_10_limpo = top_10_por_gradiente[colunas_para_salvar]

# OPCIONAL: Como os CBOs do Gradiente 0 não estavam na base original, 
# o título deles ficará vazio. Podemos preencher com um aviso:
top_10_limpo['Título da Família Ocupacional'] = top_10_limpo['Título da Família Ocupacional'].fillna('Não mapeado no estudo original')

caminho_top10 = PASTA_DADOS / "Top_10_CBOs_por_Gradiente_bancarios.csv"
top_10_limpo.to_csv(caminho_top10, index=False, sep=';', encoding='utf-8-sig')

# Exibir na consola
resumo_tela = resumo_impacto.copy()
resumo_tela['total_vinculos_ativos'] = resumo_tela['total_vinculos_ativos'].apply(lambda x: f"{int(x):,}".replace(",", "."))
resumo_tela['percentual (%)'] = resumo_tela['percentual (%)'].round(2)

print("Estimativa de Empregos Impactados por Gradiente de IA no setor bancário em 2024:")
print(resumo_tela)
print("\n✅ Arquivos guardados com sucesso na pasta Data!")