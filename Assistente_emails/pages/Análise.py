import streamlit as st 
from emails_gmail import carregar_emails,detalhes
from analise_emails import analisar_email



GOOGLE_API_KEY = st.secrets["GOOGLE"]



usuario = st.text_input(label='',placeholder='Insira seu gmail',key='analise')
if usuario:
        data = st.date_input(value=None,label='Insira uma data',key='data_analise')
        if data:
            contador_emails = 0
            contador_remetentes = []
            contador_emails_nao_lidos = 0
            lista_vizualizar_depois = []
            lista_vizualizar = []
            lista_remetentes = []
            lista_anexos  = []    
            dia = str(data).split('-')
            for info in carregar_emails(email = usuario,password = st.secrets["EMAIl"],host='imap.gmail.com',data_informar=data):
                    try:
                           anexo =  info['anexo'][0]
                           if anexo in lista_anexos:
                                   pass
                           else:
                                   lista_anexos.append(anexo)
                    except:
                            pass
                    if int(info['data'][4:7]) == int(dia[2]):
                        contador_emails += 1 
                        try:
                            lista_vizualizar.append(analisar_email(key=GOOGLE_API_KEY,pergunta=f'Você está recebendo emails. Por favor, resuma as informações dos emails e apresente uma resposta com tom formal. seguem os emails {info['texto']}'))
                        except:
                            contador_emails_nao_lidos +=1
                            lista_vizualizar_depois.append(info)
            for remetente in detalhes(email = usuario,password = 'ibdlxbnrjwczltuo',host='imap.gmail.com',data=data):
                dia = str(data).split('-')
                data_remetente = remetente['data']
                if int(dia[2]) == int(data_remetente[4:7]):
                    if remetente['remetente'] in contador_remetentes:
                        pass
                    else:
                        contador_remetentes.append(remetente['remetente'])
            col1,col2,col3 = st.columns(3)     
            with col1:
                st.metric(label='Total de E-mails',value=contador_emails)
            with col2:
                st.metric(label='Total de Remetentes',value=len(contador_remetentes))
            with col3:
                st.metric(label='E-mails não carregados',value=contador_emails_nao_lidos)
            for resposta in list(set(lista_vizualizar)):
                st.info(resposta)
                st.divider()    

            if len(lista_vizualizar_depois) > 0:
                    sim = st.popover('Vizualizar E-mails não lidos')
                        
                    with sim:
                        for item in lista_vizualizar_depois:
                            try:
                                data_analise = str(item).split('Data')
                                print(data_analise)
                                st.info(analisar_email(key=GOOGLE_API_KEY,pergunta=f'Você está recebendo emails. Por favor, resuma as informações dos emails e apresente uma resposta com tom formal. seguem os emails {item}'))
                                st.divider()
                            except:
                                    pass
            if len(lista_anexos) > 0:
                      ver_anexo = st.popover('Vizualizar Anexos')
                      with ver_anexo:
                              st.info(lista_anexos[0])
