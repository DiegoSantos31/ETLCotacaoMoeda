# 🧠 **Projeto ETL Medallion - Cotação de Moedas**

Este projeto implementa um pipeline completo de **ETL (Extração, Transformação e Carga)** baseado na **Arquitetura Medallion**, com foco na coleta, tratamento e visualização de cotações de moedas (USD, EUR, BTC).  
O objetivo é demonstrar, de forma prática, um fluxo de engenharia de dados que vai desde a extração de dados brutos até a entrega de informações analíticas em uma camada de valor (Ouro).

---

## 📘 **Sumário**

1. [Introdução](#-introdução)
2. [Arquitetura do Projeto](#-arquitetura-do-projeto)
3. [Tecnologias Utilizadas](#-tecnologias-utilizadas)
4. [Estrutura de Pastas](#-estrutura-de-pastas)
5. [Guia Completo de Execução](#-guia-completo-de-execução)
   - [1. Configuração Inicial do Ambiente Python](#1-configuração-inicial-do-ambiente-python)
   - [2. Execução do Pipeline ETL](#2-execução-do-pipeline-etl-extração-transformação-e-carga)
   - [3. Demonstração e Visualização dos Dados](#3-demonstração-e-visualização-dos-dados-finais)
   - [4. Finalização](#4-finalização)
6. [Resultados Esperados](#-resultados-esperados)
7. [Autor](#-autor)

---

## 💡 **Introdução**

O projeto **ETL Medallion (Cotação de Moedas)** foi desenvolvido com o intuito de aplicar boas práticas de engenharia de dados, utilizando a arquitetura Medallion para garantir qualidade, rastreabilidade e valor agregado aos dados.  

Através do pipeline, os dados são extraídos de uma API pública de cotações de moedas, tratados e transformados em diferentes camadas de qualidade, culminando em uma camada final pronta para análise e visualização interativa.

---

## 🏗️ **Arquitetura do Projeto**

A **Arquitetura Medallion** organiza o fluxo de dados em três camadas principais:

1. **Bronze:**  
   - Dados brutos, diretamente extraídos da API.  
   - Armazenamento em formato JSON.  

2. **Prata:**  
   - Dados limpos e padronizados.  
   - Conversão para o formato CSV (tabular).  

3. **Ouro:**  
   - Aplicação das regras de negócio.  
   - Filtragem das moedas USD, EUR e BTC.  
   - Criação da coluna `status_variacao`, que indica a tendência de valorização ou desvalorização.  

Essa abordagem facilita o versionamento, reprocessamento e auditoria dos dados ao longo do ciclo de vida.

---

## 🧰 **Tecnologias Utilizadas**

- **Linguagem:** Python 3.10+
- **Bibliotecas Principais:**
  - `pandas` – Manipulação e transformação de dados
  - `requests` – Consumo de APIs
  - `streamlit` – Visualização interativa dos resultados
- **Gerenciamento de Ambiente:** `venv`
- **Formato de Armazenamento:** JSON / CSV

---

## 📂 **Estrutura de Pastas**

```bash
ETL_Medallion/
│
├── data/
│   ├── bronze/
│   ├── prata/
│   └── ouro/
│
├── etl_medallion.py
├── demonstracao_ouro.py
├── requirements.txt
└── README.md
