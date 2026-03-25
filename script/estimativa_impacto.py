import pandas as pd

# 1. Carregar a sua planilha de classificação de IA
df_classificacao = pd.read_csv(r"../Data/CBOs por exposição à IA generativa - Página1 (1).csv")

# 2. Carregar o arquivo exportado da Base dos Dados referente a 2024
df_rais = pd.read_csv(r"../Data/vinculos_por_cbo_2024.csv")

# Converter a coluna de CBO para texto (string) para garantir o cruzamento perfeito
df_classificacao['Código CBO'] = df_classificacao['Código CBO'].astype(str)
df_rais['codigo_cbo_4'] = df_rais['codigo_cbo_4'].astype(str)

# 3. Fazer o cruzamento (Merge) das bases
df_impacto = pd.merge(
    df_classificacao, 
    df_rais, 
    left_on='Código CBO', 
    right_on='codigo_cbo_4', 
    how='left' 
)

# Preencher com 0 caso algum CBO da sua lista não tenha tido vínculos ativos em 2024
df_impacto['total_vinculos_ativos'] = df_impacto['total_vinculos_ativos'].fillna(0)

# 4. Calcular os totais agregados por Gradiente
resumo_impacto = df_impacto.groupby('Gradiente')['total_vinculos_ativos'].sum().reset_index()

# Calcular a porcentagem em relação ao total de empregos mapeados na sua lista
total_mapeado = resumo_impacto['total_vinculos_ativos'].sum()
resumo_impacto['percentual (%)'] = (resumo_impacto['total_vinculos_ativos'] / total_mapeado) * 100

# 5. SALVAR OS ARQUIVOS (com números crus e formatação amigável para Excel BR)
caminho_detalhado = r"../Data/Estimativa_Detalhada_Impacto_IA_2024.csv"
caminho_resumo = r"../Data/Resumo_Impacto_IA_2024.csv"

df_impacto.to_csv(caminho_detalhado, index=False, sep=';', encoding='utf-8-sig')
resumo_impacto.to_csv(caminho_resumo, index=False, sep=';', encoding='utf-8-sig')

# 6. EXIBIR NA TELA (criando uma cópia só para deixar bonito no terminal)
resumo_tela = resumo_impacto.copy()
resumo_tela['total_vinculos_ativos'] = resumo_tela['total_vinculos_ativos'].apply(lambda x: f"{int(x):,}".replace(",", "."))
resumo_tela['percentual (%)'] = resumo_tela['percentual (%)'].round(2)

print("Estimativa de Empregos Impactados por Gradiente de IA em 2024:")
print(resumo_tela)
print(f"\n✅ Arquivos salvos com sucesso na pasta Data!")

# 7. Levantar as 10 principais ocupações por Gradiente
# Ordenamos primeiro por Gradiente (A-Z) e depois pelo total de vínculos (Maior para Menor)
df_ordenado = df_impacto.sort_values(by=['Gradiente', 'total_vinculos_ativos'], ascending=[True, False])

# Agrupamos por Gradiente e pegamos as 10 primeiras linhas de cada grupo
top_10_por_gradiente = df_ordenado.groupby('Gradiente').head(10)

# (Opcional) Vamos selecionar apenas as colunas que importam para esse ranking ficar limpo.
# Dê uma olhada se o nome da coluna com o nome da profissão é 'Título' ou 'Ocupação' na sua base original
# e substitua abaixo se for diferente:
colunas_para_salvar = ['Gradiente', 'Código CBO', 'total_vinculos_ativos'] 
# Dica: se tiver o nome da ocupação, adicione na lista acima! Ex: 'Título CBO'

top_10_limpo = top_10_por_gradiente[colunas_para_salvar]

# 8. Salvar esse novo recorte em um CSV configurado para o Excel
caminho_top10 = r"../Data/Top_10_CBOs_por_Gradiente.csv"
top_10_limpo.to_csv(caminho_top10, index=False, sep=';', encoding='utf-8-sig')

print(f"✅ Arquivo com o Top 10 Ocupações por Gradiente salvo com sucesso em: {caminho_top10}")

# Exibir um pedacinho na tela para você conferir como ficou:
print("\nTop 3 de cada Gradiente (apenas para visualização rápida):")
print(top_10_limpo.groupby('Gradiente').head(3))
