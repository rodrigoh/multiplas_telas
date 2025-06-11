import streamlit as st

st.set_page_config(
  page_title="Minha Super App Multi-Páginas",
  page_icon="👋",
  
)

st.title("Bem-vindo à Minha Super App!")
st.sidebar.success("Selecione uma página acima.")

st.markdown(
  """
  Esta é a página inicial da sua aplicação multi-páginas Streamlit.
  👈 Selecione uma página na barra lateral para começar!
  """
)