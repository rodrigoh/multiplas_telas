import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Página de Gráficos", page_icon="📊")

st.markdown("# Página de Gráficos")
st.write("Visualize seus gráficos aqui!")

df = pd.DataFrame({
    "Categoria": ["A", "B", "C", "D"],
    "Valor": [10, 20, 15, 25]
})
fig = px.bar(df, x="Categoria", y="Valor", title="Exemplo de Gráfico de Barras")
st.plotly_chart(fig)