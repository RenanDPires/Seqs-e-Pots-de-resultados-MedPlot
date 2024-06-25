# Tensões e Correntes de Seq+ além de Potências calculadas pelas Seq+ e pelas somas das potências em cada fase
Projeto 100% em python com arquivo de configuração em JSON;

Para usar certinho, também é necessário que tenhamos consultas no padrão MedPlot;

Módulos necessários: json, numpy, pandas, math, cmath e os .

## Ajustes para execução
Necessário ajustar diretórios da pasta_consulta e pasta_resultado ao fim do arquivo main.py;

Onde, pasta_consulta é a pasta com os arquivos .txt objetivados;

E a pasta_resultado é a pasta de salvamento dos dados originais+calculados.


Nessa build, temos as pastas Consultas/...(pasta_consulta) e Resultados(pasta_resultado) setadas como input e output respectivamente. -- Sinta-se livre para ajustar às suas necessidades

## Issue a resolver
.txt com colunas das 3 fases, mas com dados de apenas 1 (demais com dados = 0) acaba tendo o processamento realizado. O que está errado!


Exemplo de ocorrência:

PMUs de barra com 3 fases, mas dados em apenas 1 -- Ou casos semelhantes
