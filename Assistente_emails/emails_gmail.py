from imbox import Imbox
from datetime import datetime,date
from imap_tools import MailBox, AND
import smtplib
from email.mime.text import MIMEText
import streamlit as st


def carregar_emails(host,email,password,data_informar):
    lista = []
    with Imbox(host, username=email, password=password) as imbox:
        mensagens = imbox.messages(date__gt=data_informar)
        for msg_tupla in mensagens:
            try:
                msg = msg_tupla[1]  # A segunda posição da tupla contém a mensagem
                conteudo = msg.body["plain"][0]  # Conteúdo em texto simples
                descricao = f'''Assunto: {msg.subject}\n
                Remetente: {msg.sent_from[0]['email']}\n
        Data: {msg.date}'''
                texto  = f'''{descricao}\n
    {conteudo}'''
                if len(msg.attachments) >0:
                    lista_anexos = []
                    for anexo in msg.attachments:
                        with open(anexo.get('filename'),'wb') as arquivo:
                            arquivo.write(anexo.get('content'))
                            lista_anexos.append(arquivo)
                    dict_email = {'texto':texto,'data':msg.date,'anexo':lista_anexos}
                else:
                    dict_email = {'texto':texto,'data':msg.date}

                if dict_email in lista:
                    pass
                else:
                    lista.append(dict_email)
            except:
                pass
        return lista
    
def detalhes(host,email,password,data):
    lista_detalhes = []
    with Imbox(host, username=email, password=password) as imbox:
        mensagens = imbox.messages(date__gt=data)
        for msg_tupla in mensagens:
            try:
                msg = msg_tupla[1]  # A segunda posição da tupla contém a mensagem
                conteudo = msg.body["plain"][0]  # Conteúdo em texto simples
                remetente = msg.sent_from[0]['email']
                dict_detalhes = {'remetente':remetente,'data':msg.date}
                if dict_detalhes in lista_detalhes:
                    pass
                else:
                    lista_detalhes.append(dict_detalhes)
            except:
                pass
    return lista_detalhes

def remetentes(host,email,password,data):
    lista_remetentes_infos = []
    with Imbox(host, username=email, password=password) as imbox:
        mensagens = imbox.messages(date__gt=data)
        for msg_tupla in mensagens:
            try:
                msg = msg_tupla[1]  # A segunda posição da tupla contém a mensagem
                conteudo = msg.body["plain"][0]  # Conteúdo em texto simples
                remetente = msg.sent_from[0]['email']
                info = f'''Remetente: {msg.sent_from[0]['email']}\n

Assunto: {msg.subject}'''
                dict_remetente = {'remetente':msg.sent_from[0]['email'],'info':info,'email': msg.body["plain"][0]}
                if dict_remetente in lista_remetentes_infos:
                    pass
                else:
                   lista_remetentes_infos.append(dict_remetente)
            except:
                pass
    return lista_remetentes_infos

def enviar_email(email,senha,destinatario,conteudo,assunto):
    servidor_email = smtplib.SMTP('smtp.gmail.com', 587) 
    servidor_email.starttls()
    servidor_email.login(email, senha)  
    assunto = assunto
    corpo = conteudo
    mensagem = MIMEText(corpo)
    mensagem['Subject'] = assunto
    mensagem['From'] = email
    mensagem['To'] = destinatario
    servidor_email.send_message(mensagem)
    servidor_email.quit()


def carregar_emails_nao_lidos(host,email,password,data_informar):
    lista_nao_lidos = []
    with Imbox(host, username=email, password=password) as imbox:
        mensagens = imbox.messages(date__gt=data_informar,unread=True)
        for msg_tupla in mensagens:
            try:
                msg = msg_tupla[1]  # A segunda posição da tupla contém a mensagem
                conteudo = msg.body["plain"][0]  # Conteúdo em texto simples
                descricao = f'''Assunto: {msg.subject}\n
                Remetente: {msg.sent_from[0]['email']}\n
        Data: {msg.date}'''
                texto  = f'''{descricao}\n
    {conteudo}'''
                if msg.attachments:
                    lista_anexos_nao_lidos = []
                    for anexo in msg.attachments:
                        arquivo_nao_lido = anexo.get('filename')
                        lista_anexos_nao_lidos.append(arquivo_nao_lido)
                    dict_email_nao_lido = {'texto':texto,'data':msg.date,'anexo':arquivo_nao_lido}
                else:
                    dict_email_nao_lido = {'texto':texto,'data':msg.date}

                if dict_email_nao_lido in lista_nao_lidos:
                    pass
                else:
                    lista_nao_lidos.append(dict_email_nao_lido)
            except:
                pass
        return lista_nao_lidos

def baixar_emails(email):
        lista_anexos = []
        data_hoje = date.today()
        meu_email = MailBox('imap.gmail.com').login(email, st.secrets['EMAIl'])
        lista_emails = meu_email.fetch(AND(date=data_hoje))
        for email in lista_emails:
            for anexo in email.attachments:
                nome_arquivo = anexo.filename
                conteudo_arquivo = anexo.payload
                tipo = anexo.content_type
                lista_anexos.append({'conteudo':conteudo_arquivo,"nome":nome_arquivo,"remetente":email.sent_from,"assunto":email.subject})
        download = st.download_button(label="Faça o download do anexo aqui",data=lista_anexos[0]['conteudo'] in lista_anexos,file_name=f"{nome_arquivo}",mime=f"{tipo}")                                                                                            
        if download:
                                st.success('Arquivo excel baixado com sucesso')
                                st.divider() 
        return lista_anexos
