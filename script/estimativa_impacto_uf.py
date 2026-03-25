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
caminho_rais = PASTA_DADOS / "vinculos_cbo_uf_2024.csv"

# Carregando os DataFrames
df_classificacao = pd.read_csv(caminho_classificacao)
df_rais_estados = pd.read_csv(caminho_rais) # CORRIGIDO: Agora a variável tem o nome certo

# 2. Converter CBO para texto
df_classificacao['Código CBO'] = df_classificacao['Código CBO'].astype(str)
df_rais_estados['codigo_cbo_4'] = df_rais_estados['codigo_cbo_4'].astype(str)

# 3. Fazer o cruzamento (Merge) cruzando pelo CBO
df_impacto = pd.merge(
    df_classificacao, 
    df_rais_estados, 
    left_on='Código CBO', 
    right_on='codigo_cbo_4', 
    how='left' 
)

df_impacto['total_vinculos_ativos'] = df_impacto['total_vinculos_ativos'].fillna(0)

# =========================================================================
# 4. Agrupar por Estado E Gradiente
# =========================================================================
resumo_estados = df_impacto.groupby(['sigla_uf', 'Gradiente'])['total_vinculos_ativos'].sum().reset_index()

# 5. Calcular o percentual DENTRO de cada estado
totais_por_estado = resumo_estados.groupby('sigla_uf')['total_vinculos_ativos'].sum().reset_index()
totais_por_estado = totais_por_estado.rename(columns={'total_vinculos_ativos': 'total_do_estado'})

# Juntamos esse total de volta na tabela principal
resumo_estados = pd.merge(resumo_estados, totais_por_estado, on='sigla_uf', how='left')

# Agora calculamos a porcentagem (Vínculos do Gradiente X / Total do Estado Y)
resumo_estados['percentual_no_estado (%)'] = (resumo_estados['total_vinculos_ativos'] / resumo_estados['total_do_estado']) * 100

# 6. Limpar e organizar para salvar
# Vamos deixar a tabela ordenada por Estado (A-Z) e depois pelo Gradiente
resumo_estados = resumo_estados.sort_values(by=['sigla_uf', 'Gradiente'])

# Salvar o CSV para análise (CORRIGIDO: usando o pathlib)
caminho_estados = PASTA_DADOS / "Resumo_Impacto_IA_por_Estado_2024.csv" 
resumo_estados.to_csv(caminho_estados, index=False, sep=';', encoding='utf-8-sig')

print(f"✅ Arquivo por estados salvo com sucesso em: {caminho_estados}")

# Printar na tela o resultado de um estado (ex: SP) para você ver como ficou
print("\nExemplo de como ficou o cenário em São Paulo (SP):")
resumo_tela = resumo_estados[resumo_estados['sigla_uf'] == 'SP'].copy()
resumo_tela['percentual_no_estado (%)'] = resumo_tela['percentual_no_estado (%)'].round(2)
# Formatar total com ponto para facilitar leitura na tela
resumo_tela['total_vinculos_ativos'] = resumo_tela['total_vinculos_ativos'].apply(lambda x: f"{int(x):,}".replace(",", "."))
print(resumo_tela[['sigla_uf', 'Gradiente', 'total_vinculos_ativos', 'percentual_no_estado (%)']])