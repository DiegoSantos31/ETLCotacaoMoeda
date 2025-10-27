import requests
import json
import pandas as pd
from datetime import datetime
import os


API_URL = "https://economia.awesomeapi.com.br/json/all"
DATA_DIR = "data"
CAMADA_BRONZE = os.path.join(DATA_DIR, "bronze")
CAMADA_PRATA = os.path.join(DATA_DIR, "prata")
CAMADA_OURO = os.path.join(DATA_DIR, "ouro")
HORA_EXECUCAO = datetime.now().strftime("%Y%m%d_%H%M%S")


for folder in [CAMADA_BRONZE, CAMADA_PRATA, CAMADA_OURO]:
    os.makedirs(folder, exist_ok=True)


# 1. BRONZE: Extração (E) e Carga (L) Bruta

def extracao_bronze():
    print("Iniciando Camada Bronze...")
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        dados_brutos = response.json()

        caminho_arquivo = os.path.join(CAMADA_BRONZE, f"cotacoes_brutas_{HORA_EXECUCAO}.json")
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_brutos, f, ensure_ascii=False, indent=4)
        
        print(f"Dados brutos salvos em: {caminho_arquivo}")
        return dados_brutos

    except Exception as e:
        print(f"Erro na Camada BRONZE: {e}")
        return None


 # 2. PRATA: Transformação (T) e Carga (L) Limpa

def transformacao_prata(dados_brutos):
    print("\nIniciando Camada Prata...")
    if not dados_brutos:
        print("Dados brutos não encontrados.")
        return None
    
    try:
       
        df_prata = pd.DataFrame(dados_brutos.values())

        
        df_prata = df_prata[[
            'code', 'codein', 'name', 'bid', 'ask', 'varBid', 'pctChange', 'create_date'
        ]]
        df_prata.columns = [
            'moeda_origem', 'moeda_destino', 'nome', 'compra', 'venda', 'variacao', 'percentual_variacao', 'data_hora_cotacao'
        ]

        
        colunas_numericas = ['compra', 'venda', 'variacao', 'percentual_variacao']
        for col in colunas_numericas:
           
            df_prata[col] = df_prata[col].str.replace(',', '.', regex=False).astype(float)
        
      
        df_prata['data_processamento'] = HORA_EXECUCAO.split('_')[0]

       
        caminho_arquivo = os.path.join(CAMADA_PRATA, f"cotacoes_limpas_{HORA_EXECUCAO}.csv")
        df_prata.to_csv(caminho_arquivo, index=False)
        
        print(f"Dados limpos salvos em: {caminho_arquivo}")
        return df_prata

    except Exception as e:
        print(f"Erro na Camada PRATA: {e}")
        return None    

 
# 3. OURO: Transformação (T) e Carga (L) Modelada

def transformacao_ouro(df_prata):
    print("\nIniciando Camada Ouro...")
    if df_prata is None or df_prata.empty:
        print("Dados limpos não encontrados.")
        return None

    try:
       
        moedas_interesse = ['USD', 'EUR', 'BTC']
        df_ouro = df_prata[df_prata['moeda_origem'].isin(moedas_interesse)].copy()

       
        def determinar_status(variacao):
            if variacao > 0:
                return 'Subiu'
            elif variacao < 0:
                return 'Caiu'
            else:
                return 'Estável'

        df_ouro['status_variacao'] = df_ouro['variacao'].apply(determinar_status)

      
        df_ouro = df_ouro[[
            'nome', 'moeda_origem', 'compra', 'venda', 'status_variacao', 'percentual_variacao'
        ]]
        
       
        caminho_arquivo = os.path.join(CAMADA_OURO, f"cotacoes_analiticas_{HORA_EXECUCAO}.csv")
        df_ouro.to_csv(caminho_arquivo, index=False)
        
        print(f"Dados modelados salvos em: {caminho_arquivo}")
        print("\n--- AMOSTRA CAMADA OURO ---")
        print(df_ouro.head())
        
        return df_ouro

    except Exception as e:
        print(f"Erro na Camada OURO: {e}")
        return None     

 
# EXECUÇÃO DO PIPELINE

if __name__ == "__main__":
   
    dados_bronze = extracao_bronze()

    df_prata = transformacao_prata(dados_bronze)

    if df_prata is not None:
        transformacao_ouro(df_prata)

    print("\n Pipeline ETL Medallion Concluído!")

