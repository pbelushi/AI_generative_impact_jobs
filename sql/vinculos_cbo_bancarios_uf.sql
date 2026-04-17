SELECT 
    sigla_uf,
    SUBSTR(CAST(cbo_2002 AS STRING), 1, 4) AS codigo_cbo_4,
    COUNT(*) AS total_vinculos_ativos 
FROM `basedosdados.br_me_rais.microdados_vinculos`
WHERE CAST(ano AS INT64) = 2024 
  AND CAST(vinculo_ativo_3112 AS STRING) = '1'
  -- NOVO FILTRO: Apenas setor financeiro, fintechs e pagamentos (CNAEs 64 e 66)
  AND SUBSTR(CAST(cnae_2 AS STRING), 1, 2) IN ('64', '66')
GROUP BY 
    sigla_uf,
    codigo_cbo_4