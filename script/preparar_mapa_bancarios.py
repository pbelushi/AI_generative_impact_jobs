import pandas as pd
from pathlib import Path

# =========================================================================
# CONFIGURAÇÃO DE CAMINHOS
# =========================================================================
DIRETORIO_ATUAL = Path(__file__).parent 
DIRETORIO_RAIZ = DIRETORIO_ATUAL.parent 
PASTA_DADOS = DIRETORIO_RAIZ / "Data" 

# =========================================================================
# CARREGAR DADOS BANCÁRIOS
# =========================================================================
# MUDANÇA: Apontando para o arquivo específico do setor bancário
caminho_entrada = PASTA_DADOS / "Resumo_Impacto_IA_por_Estado_bancarios.csv"

if not caminho_entrada.exists():
    print(f"❌ Erro: O arquivo {caminho_entrada} não foi encontrado!")
else:
    # Lendo o CSV (separador ';' conforme definido nos scripts anteriores)
    df_estados = pd.read_csv(caminho_entrada, sep=';')

    # =========================================================================
    # FILTRAR DADOS PARA O MAPA (EX: FOCO NO GRADIENTE 4 - ALTA EXPOSIÇÃO)
    # =========================================================================
    # O Datawrapper geralmente precisa de uma linha por estado. 
    # Vamos filtrar apenas o Gradiente 4 para mostrar o impacto severo no mapa.
    df_mapa = df_estados[df_estados['Gradiente'] == 'Gradiente 4'].copy()

    # Organizar as colunas para o Datawrapper
    # Precisamos da sigla do estado e do percentual
    colunas_mapa = ['sigla_uf', 'percentual_no_estado (%)']
    df_final = df_mapa[colunas_mapa]

    # Renomear colunas para ficar bonito no mapa
    df_final.columns = ['Estado', 'Percentual de Alta Exposição (%)']

    # =========================================================================
    # SALVAR ARQUIVO PARA O DATAWRAPPER
    # =========================================================================
    caminho_saida = PASTA_DADOS / "Dados_Mapa_Bancarios_G4.csv"
    
    # Salvar com tabulação (\t) ou vírgula, o Datawrapper aceita ambos. 
    # Usaremos vírgula para facilitar a importação direta.
    df_final.to_csv(caminho_saida, index=False, sep=',', encoding='utf-8-sig')

    print(f"✅ Arquivo para o mapa gerado com sucesso: {caminho_saida}")
    print("\nResumo do que será plotado (Top 5 estados mais expostos):")
    print(df_final.sort_values(by='Percentual de Alta Exposição (%)', ascending=False).head(5))