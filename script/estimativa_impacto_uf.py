import pandas as pd

# 1. Carregar as planilhas (Lembre-se de apontar para o NOVO arquivo que veio do BigQuery)
df_classificacao = pd.read_csv(r"../Data/CBOs por exposição à IA generativa - Página1 (1).csv")
df_rais_estados = pd.read_csv(r"../Data/vinculos_cbo_uf_2024.csv")

# 2. Converter CBO para texto
df_classificacao['Código CBO'] = df_classificacao['Código CBO'].astype(str)
df_rais_estados['codigo_cbo_4'] = df_rais_estados['codigo_cbo_4'].astype(str)

# 3. Fazer o cruzamento (Merge) - Continua igual, cruzando pelo CBO
df_impacto = pd.merge(
    df_classificacao, 
    df_rais_estados, 
    left_on='Código CBO', 
    right_on='codigo_cbo_4', 
    how='left' 
)

df_impacto['total_vinculos_ativos'] = df_impacto['total_vinculos_ativos'].fillna(0)

# =========================================================================
# 4. A MÁGICA MUDA AQUI: Agrupar por Estado E Gradiente
# =========================================================================
# Nota: Confirme se o nome da coluna que veio do BigQuery é 'sigla_uf'. Se for outro, mude abaixo.
resumo_estados = df_impacto.groupby(['sigla_uf', 'Gradiente'])['total_vinculos_ativos'].sum().reset_index()

# 5. Calcular o percentual DENTRO de cada estado
# Primeiro, descobrimos o total de vínculos de cada estado separadamente
totais_por_estado = resumo_estados.groupby('sigla_uf')['total_vinculos_ativos'].sum().reset_index()
totais_por_estado = totais_por_estado.rename(columns={'total_vinculos_ativos': 'total_do_estado'})

# Juntamos esse total de volta na tabela principal
resumo_estados = pd.merge(resumo_estados, totais_por_estado, on='sigla_uf', how='left')

# Agora calculamos a porcentagem (Vínculos do Gradiente X / Total do Estado Y)
resumo_estados['percentual_no_estado (%)'] = (resumo_estados['total_vinculos_ativos'] / resumo_estados['total_do_estado']) * 100

# 6. Limpar e organizar para salvar
# Vamos deixar a tabela ordenada por Estado (A-Z) e depois pelo Gradiente
resumo_estados = resumo_estados.sort_values(by=['sigla_uf', 'Gradiente'])

# Salvar o CSV para análise (números crus)
caminho_estados = r"../Data/Resumo_Impacto_IA_por_Estado_2024.csv"
resumo_estados.to_csv(caminho_estados, index=False, sep=';', encoding='utf-8-sig')

print(f"✅ Arquivo por estados salvo com sucesso em: {caminho_estados}")

# Printar na tela o resultado de um estado (ex: SP) para você ver como ficou
print("\nExemplo de como ficou o cenário em São Paulo (SP):")
# Formatando apenas para a tela
resumo_tela = resumo_estados[resumo_estados['sigla_uf'] == 'SP'].copy()
resumo_tela['percentual_no_estado (%)'] = resumo_tela['percentual_no_estado (%)'].round(2)
print(resumo_tela[['sigla_uf', 'Gradiente', 'total_vinculos_ativos', 'percentual_no_estado (%)']])
