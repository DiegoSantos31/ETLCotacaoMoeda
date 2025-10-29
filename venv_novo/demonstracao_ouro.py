import streamlit as st
import pandas as pd
import plotly.express as px
import os

 
CAMADA_OURO = "data/ouro"

 
@st.cache_data
def carregar_dados_ouro():
    
    arquivos = [f for f in os.listdir(CAMADA_OURO) if f.endswith('.csv')]
    if not arquivos:
        st.error("Nenhum arquivo de dados encontrado na Camada OURO. Execute o etl_medallion.py primeiro!")
        return pd.DataFrame()  

  
    arquivo_mais_recente = sorted(arquivos)[-1]
    caminho_completo = os.path.join(CAMADA_OURO, arquivo_mais_recente)
    
    st.info(f"Carregando dados modelados de: {caminho_completo}")
    return pd.read_csv(caminho_completo)


st.set_page_config(
    page_title="Demonstração da Camada Ouro",
    layout="wide"
)

st.title("💰 Demonstração de Uso da Camada OURO")
st.markdown("---")

df_ouro = carregar_dados_ouro()

if not df_ouro.empty:
    st.header("1. Dados Finais (Prontos para BI)")
    st.dataframe(df_ouro)
    
    st.markdown("Os dados estão filtrados (USD, EUR, BTC) e incluem a lógica de negócio **Status da Variação**.")
    st.markdown("---")

   
    st.header("2. Análise de Desempenho (Uso do `status_variacao`)")

    
    fig_status = px.bar(
        df_ouro,
        x='moeda_origem',
        y='percentual_variacao',
        color='status_variacao',
        title='Percentual de Variação por Moeda',
        labels={'moeda_origem': 'Moeda', 'percentual_variacao': 'Variação (%)'},
        color_discrete_map={'Subiu': 'green', 'Caiu': 'red', 'Estável': 'blue'}
    )
    st.plotly_chart(fig_status, use_container_width=True)
    
    st.markdown("""
        **Interpretação:** Este gráfico usa a coluna `status_variacao` (criada na Camada Ouro) para classificar visualmente o desempenho.
        * Mostra claramente que o **Bitcoin** foi a única moeda principal a subir na última coleta.
        * Permite à área de negócios tomar decisões rápidas sobre a performance.
    """)
    st.markdown("---")

    st.header("3. Comparação de Cotação de Venda")
    
    fig_venda = px.bar(
        df_ouro,
        x='nome',
        y='venda',
        color='moeda_origem',
        title='Valor de Venda (em Reais)',
        labels={'nome': 'Cotação', 'venda': 'Preço de Venda (R$)'}
    )
    st.plotly_chart(fig_venda, use_container_width=True)
    
    st.markdown("""
        **Interpretação:** Esta visualização compara diretamente o preço de venda, que é a informação mais relevante para quem vai comprar a moeda.
    """)