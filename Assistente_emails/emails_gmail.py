from imbox import Imbox
from datetime import datetime
from imap_tools import MailBox, AND
import smtplib
from email.mime.text import MIMEText



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
                if msg.attachments:
                    lista_anexos = []
                    for anexo in msg.attachments:
                        arquivo = anexo.get('filename')
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
                dict_detalhes = {'remetente':remetente,'data':data}
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




