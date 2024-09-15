import streamlit as st 
from emails_gmail import carregar_emails,detalhes,remetentes,enviar_email
from analise_emails import analisar_email


email = st.text_input(label='',placeholder='Insira seu email')
if email:
    data = st.date_input(value=None,label='Insira uma data',key='data_analise')
    lista_dados = []    
    lista_remetentes = []
    if data:
        for remetente in remetentes(email = email,password = st.secrets["EMAIl"],host='imap.gmail.com',data=data):
                if remetente in lista_remetentes:
                        pass
                else:
                        lista_remetentes.append(remetente['remetente'])
        pesquisa_email = st.selectbox(label='',placeholder='Selecione um remetente',index=None,options=list(set(lista_remetentes)))
        if pesquisa_email:
                exibir = False
                key = 0
                dia = str(data).split('-')
                for remetente in remetentes(email = email,password = st.secrets["EMAIl"],host='imap.gmail.com',data=data):
                        if remetente['remetente'] == pesquisa_email:
                                if {'info':remetente['info'],'email':remetente['email']} in lista_dados:
                                       pass
                                else:
                                        lista_dados.append({'info':remetente['info'],'email':remetente['email']})
                st.divider()        
                st.title("E-mails a responder")
                for item in lista_dados:
                        st.info(item['info'])
                        resposta = st.text_input(label='',placeholder='Insira a sua mensagem',key=key)
                        st.divider()
                        conteudo = st.popover('Vizualizar Conteúdo')
                        with conteudo:
                               st.info(item['email'])
                        key +=1
                        if resposta:
                               enviar_email(email=email,senha=st.secrets["EMAIl"],destinatario=pesquisa_email,conteudo=resposta,assunto='Resposta a mensagem')
                               st.success("Email enviado com sucesso")
                               
                        
               

                

                    
