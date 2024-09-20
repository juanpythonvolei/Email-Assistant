import streamlit as st 
from emails_gmail import carregar_emails,detalhes,carregar_emails_nao_lidos
from analise_emails import analisar_email
import firebase_admin
from firebase_admin import credentials, firestore,db
import requests
import os
import random
st.markdown("""
    <style>
       [aria-expanded='true'] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
criar_login = st.text_input('Insira um email')
criar_senha = st.text_input('Criar Senha')
col1,col2,col3 = st.columns(3)
with col1:
  criar = st.button('Criar Conta')
with col2:
  voltar = st.button('Voltar ao login')
if criar:
  ref_criar_conta = db.reference('usuario')
  ref_criar_conta.child(f'{random.randint(10,10000)}/{criar_login}').set(f'{criar_senha}')
  st.switch_page('pages/Geral.py')
if voltar:
  st.switch_page('login.py')
