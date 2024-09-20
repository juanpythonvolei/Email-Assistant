import streamlit as st 
from emails_gmail import carregar_emails,detalhes,carregar_emails_nao_lidos
from analise_emails import analisar_email

st.logo('https://www.logolynx.com/images/logolynx/fe/fe346f78d111e1d702b44186af59b568.jpeg')
tab1,tab2 = st.tabs(['Email caixa de entrada','Não lidos'])
with tab1:
        usuario = st.text_input(label='',placeholder='Insira seu gmail',key = 'caixa de entrada')
        if usuario:
                data = st.date_input(value=None,label='Insira uma data',key = 'data_caixa_de_entrada')
                if data:
                        dia = str(data).split('-')
                        for info in carregar_emails(email = usuario,password = st.secrets["EMAIl"],host='imap.gmail.com',data_informar=data):
                            if int(info['data'][4:7]) == int(dia[2]):
                                st.info(info['texto'])
                                st.divider()
with tab2:
        usuario = st.text_input(label='',placeholder='Insira seu gmail',key = 'email_nao_lido')
        if usuario:
                data = st.date_input(value=None,label='Insira uma data',key = 'data_email_nao_lido')
                if data:
                    dia = str(data).split('-')
                    for info in carregar_emails_nao_lidos(email = usuario,password = st.secrets["EMAIl"],host='imap.gmail.com',data_informar=data):
                        if int(info['data'][4:7]) == int(dia[2]):
                            st.info(info['texto'])
                            st.divider()

