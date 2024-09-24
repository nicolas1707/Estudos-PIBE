

# Relatório: Download e Organização de Dados do Censo Escolar Usando a Base dos Dados

## Objetivo
O objetivo foi baixar e organizar os dados do Censo Escolar, disponíveis na plataforma [Base dos Dados](https://basedosdados.org/), utilizando a API do BigQuery, filtrando por ano para os datasets grandes. Os dados foram baixados em formato CSV e organizados em pastas, separadas por ano.

## Passos Para o Download

### 1. **Análise e estimativa do espaço necessário para download**

Para isso, utilizamos uma __query de busca total__ para cada tabela, verificando tanto o __valor de processamento__ dado pela informação disponível no canto superior direito do console, quanto o __tamanho do arquivo__ baixando o arquivo CSV após a consulta.

```SQL
SELECT *
FROM `basedosdados.br_inep_censo_escolar.tabela`
```

![image](https://github.com/user-attachments/assets/b06d7ba3-54ae-4525-8e71-b2a6c1d3c853)

Após isso, efetuamos o download da tabela caso ela não estoure o limite de tamanho.

### 2. **Download para tabelas muito grandes**

Como dito anteriormente, para efetuarmos o download do arquivo ele deve possuir __até no máximo 1 Giga__, e algumas tabelas possuíam milhões de dados para download. Então, algumas tabelas tivemos que particionar para atender este requisito, divindo-as em pastas identificadas __por ano__ com um conjunto de arquivos CSV de no máximo __450MB__.

Para fazer estas pesquisas e downloads particionados, utilizamos uma __query de busca limitada__:

```SQL
SELECT *
FROM `basedosdados.br_inep_censo_escolar.tabela`
WHERE ano = x
LIMIT 1500000 OFFSET 0;
```
Com este tipo de busca, incrementamos o valor de _OFFSET_ até não termos mais dados, para assim, baixar todos os dados do ano sem que estejam num único arquivo muito grande.

### 3. **Envio dos arquivos para o LABMAC**

