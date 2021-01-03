from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import rpa as r
import pyautogui as p
import pandas as pd

# capturando a informação do dolar
r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')
p.sleep(4)
janela = p.getActiveWindow()
janela.maximize()

dolar_comercial = r.read('//*[@id="comercial"]')
r.close()

# enviando por e-mail


# texto do email
texto_email = dolar_comercial + 'Hoje: ' + str(pd.Timestamp('today'))

# email remetente, senha, destinatário
de = 'julio.zeferino@salexpress.com.br'
senha = 'U_350juztc204'
para = 'julioszeferino@gmail.com'
# para02 = ''

# Setup the MIME
message = MIMEMultipart()
message['From'] = de
message['To'] = para
# message['To'] = para02
message['Subject'] = 'Cotação do dolar'  # Título do e-mail

# Corpo do E-mail com anexos
message.attach(MIMEText(texto_email, 'plain'))

# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
session.starttls()  # Habilita a segurança
session.login(de, senha)  # Login e senha de quem envia o e-mail
texto = message.as_string()
session.sendmail(de, para, texto)
session.quit()
