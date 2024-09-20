import streamlit as st 
from emails_gmail import carregar_emails,detalhes,carregar_emails_nao_lidos
from analise_emails import analisar_email
import firebase_admin
from firebase_admin import credentials, firestore,db
import requests
import os
st.markdown("""
    <style>
       [aria-expanded='true'] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
if not firebase_admin._apps:
    autenticacao  = {
            "type": st.secrets["firebase"]["type"],
            "project_id": st.secrets["firebase"]["project_id"],
            "private_key_id": st.secrets["firebase"]["private_key_id"],
            "private_key": st.secrets["firebase"]["private_key"],
            "client_email": st.secrets["firebase"]["client_email"],
            "client_id": st.secrets["firebase"]["client_id"],
            "auth_uri": st.secrets["firebase"]["auth_uri"],
            "token_uri": st.secrets["firebase"]["token_uri"],
            "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
            "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"]
    }

    cred = credentials.Certificate(autenticacao)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://bancodedadosroteirooficial-default-rtdb.firebaseio.com'  # Substitua pelo URL do seu Realtime Database
    })
else:
    pass
ref_login = db.reference('usuarios')
login  = st.text_input(label='',placeholder='Insira seu usuário de login')
senha = st.text_input(label='',placeholder='Insira sua senha')
col1,col2,col3 = st.columns(3)
with col1:
    entrar = st.button('logar')
with col2:
    criar_conta = st.button('Criar Conta')
if entrar:
    requiscao = requests.get('https://bancodedadosroteirooficial-default-rtdb.firebaseio.com/.json')
    data = requiscao.json()
    for item in data:
        if login == item:
            senha_comparar = data[f'{item}']
            if senha == senha_comparar:
                st.switch_page('pages/Geral.py')
if criar_conta:
    st.switch_page('Criar_conta.py')
