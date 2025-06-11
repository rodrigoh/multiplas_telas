import streamlit as st

st.set_page_config(page_title="Página de Dados", page_icon="🎲")

st.markdown("# Página de Dados")
st.write("Aqui você encontrará seus dados!")
st.dataframe({"Coluna A": [1, 2, 3], "Coluna B": ["X", "Y", "Z"]})