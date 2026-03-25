SELECT 
    sigla_uf,           -- ADICIONAR ESTA LINHA
    cbo_2002 AS codigo_cbo_4, -- (ou o nome da coluna de CBO que você usou)
    COUNT(*) AS total_vinculos_ativos 
FROM `basedosdados.br_me_rais.microdados_vinculos`
WHERE ano = 2024 -- (ou o filtro que você usou)
GROUP BY 
    sigla_uf,           -- ADICIONAR ESTA LINHA
    codigo_cbo_4