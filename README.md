# Guia Literário
Guia Literário da cidade do Rio de Janeiro do início do século XX. Parte do projeto de pesquisa do Programa de Pós Graduação em Urbanismo do Laboratório de Análise Urbana e Representação Digital da FAU-UFRJ.

## Preparando o projeto
```bash

# Altere o path de "Prefix" do arquivo .yml para o path correspondente no seu computador
# Criando o ambiente no seu miniconda ou anaconda a partir do arquivo environment.yml
$ conda env create -f environment.yml

# Ativando o ambiente
$ conda activate envconda
```

## Comandos
```bash

# Atualizando metadados
$ python update_data.py

# Exportando mapa em HTML
$ python export.py

```