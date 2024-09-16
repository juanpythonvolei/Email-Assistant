import streamlit as st 
from emails_gmail import carregar_emails,detalhes,carregar_emails_nao_lidos
from analise_emails import analisar_email


login  = st.text_input(label='',placeholder='Insira seu usuário de login')
senha = st.text_input(label='',placeholder='Insira sua senha')
entrar = st.button('logar')

