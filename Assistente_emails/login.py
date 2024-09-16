import streamlit as st 
from emails_gmail import carregar_emails,detalhes,carregar_emails_nao_lidos
from analise_emails import analisar_email

st.markdown("""
    <style>
       [aria-expanded='true'] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
login  = st.text_input(label='',placeholder='Insira seu usuário de login')
senha = st.text_input(label='',placeholder='Insira sua senha')
entrar = st.button('logar')

