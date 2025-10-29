# Guia de Execução do Projeto: ETL Medallion (Cotação de Moedas)

Este documento detalha o procedimento completo, passo a passo, para configurar, executar e visualizar os resultados.

## Guia Completo de Execução


### 1. Configuração Inicial do Ambiente Python

Para garantir a consistência e o isolamento das dependências, iniciamos criando um ambiente virtual. O comando `python -m venv venv_novo` cria a estrutura do ambiente em uma pasta isolada. Em seguida, é **fundamental ativar** o ambiente com o comando `.\venv_novo\Scripts\activate`; seu prompt de comando deve passar a exibir o prefixo `(venv_novo)`, indicando que a ativação foi bem-sucedida. Com o ambiente ativo, todas as bibliotecas essenciais (`pandas`, `requests`, `streamlit`, etc.) são instaladas em um único passo usando o arquivo de requisitos: `pip install -r requirements.txt`.

### 2. Execução do Pipeline ETL (Extração, Transformação e Carga)

Com o ambiente pronto, o núcleo do projeto é executado. O comando `python etl_medallion.py` inicia o pipeline de dados, que segue rigorosamente a **Arquitetura Medallion** em três fases:
1.  **Bronze:** Extrai os dados brutos da API e os salva em JSON.
2.  **Prata:** Limpa, padroniza e converte os dados para o formato tabular CSV.
3.  **Ouro:** Aplica a lógica de negócio (filtragem de USD, EUR, BTC e criação da coluna `status_variacao`).
A execução gera e preenche a pasta `data/` com arquivos separados para cada camada.

### 3. Demonstração e Visualização dos Dados Finais

Após o ETL, os dados modelados da Camada Ouro estão prontos para consumo. O comando `streamlit run demonstracao_ouro.py` inicia um dashboard interativo no seu navegador (via uma URL local). Esta aplicação lê o arquivo final da Camada Ouro para apresentar a tabela de dados modelados e gráficos analíticos, comprovando que o pipeline de ETL gerou um produto de dados de alto valor para a área de negócios.

### 4. Finalização

Ao concluir o uso e a demonstração, saia do ambiente virtual isolado executando o comando `deactivate` no terminal.

---