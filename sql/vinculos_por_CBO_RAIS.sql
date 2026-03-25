SELECT 
  SUBSTR(CAST(cbo_2002 AS STRING), 1, 4) AS codigo_cbo_4,
  COUNT(*) AS total_vinculos_ativos
FROM `basedosdados.br_me_rais.microdados_vinculos`
WHERE CAST(ano AS INT64) = 2024 
  AND CAST(vinculo_ativo_3112 AS STRING) = '1'
GROUP BY 1
ORDER BY 2 DESC