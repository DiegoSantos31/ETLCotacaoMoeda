# 💰 **Projeto ETL Medallion - Cotação de Moedas**

Este projeto implementa um pipeline completo de **ETL (Extração, Transformação e Carga)** utilizando a **Arquitetura Medallion**, com foco na coleta, tratamento e visualização de cotações de moedas (USD, EUR, BTC).  
O objetivo é demonstrar, de forma prática, o fluxo de engenharia de dados desde a extração até a apresentação analítica em dashboard interativo.

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

O projeto **ETL Medallion (Cotação de Moedas)** aplica boas práticas de engenharia de dados com foco em modularidade, rastreabilidade e valor analítico.  
O pipeline coleta cotações de moedas via API pública, processa as informações em múltiplas etapas e fornece uma camada final pronta para visualização em **Streamlit**.

---

## 🏗️ **Arquitetura do Projeto**

A **Arquitetura Medallion** organiza o fluxo de dados em três camadas:

1. **Bronze:**  
   - Dados brutos extraídos da API.  
   - Armazenamento em formato JSON.  

2. **Prata:**  
   - Dados limpos e padronizados.  
   - Conversão para o formato tabular (CSV).  

3. **Ouro:**  
   - Aplicação de regras de negócio.  
   - Filtragem de moedas (USD, EUR, BTC) e criação da coluna `status_variacao`.  

Essa estrutura garante rastreabilidade, qualidade e consistência dos dados processados.

---

## 🧰 **Tecnologias Utilizadas**

- **Linguagem:** Python 3.10+
- **Bibliotecas:**
  - `pandas` – Manipulação e transformação de dados  
  - `requests` – Consumo de APIs  
  - `streamlit` – Dashboard interativo para visualização  
- **Ambiente Virtual:** `venv`
- **Formatos de Armazenamento:** JSON / CSV

---

## 📂 **Estrutura de Pastas**

```bash
ETLCotacaoMoeda/
│
├── venv_novo/
│   ├── etc/
│   ├── Lib/
│   ├── Scripts/
│   ├── share/
│   └── pyvenv.cfg
│
├── .gitignore
├── demonstracao_ouro.py
├── etl_medallion.py
└── README.md
