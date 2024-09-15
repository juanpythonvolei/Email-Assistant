import streamlit as st 
from emails_gmail import carregar_emails,detalhes
from analise_emails import analisar_email





usuario = st.text_input(label='',placeholder='Insira seu gmail')
if usuario:
        data = st.date_input(value=None,label='Insira uma data')
        if data:
            dia = str(data).split('-')
            for info in carregar_emails(email = usuario,password = st.secrets["EMAIl"],host='imap.gmail.com',data_informar=data):
                if int(info['data'][4:7]) == int(dia[2]):
                    st.info(info['texto'])
                    st.divider()

