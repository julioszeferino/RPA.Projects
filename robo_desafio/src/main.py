'''
Robo que insere dados em um formulario web
'''

import rpa as r
import pyautogui as p
import pandas as pd
import xlrd
import openpyxl

r.init()
r.url('http://rpachallenge.com')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(20)

r.download(
    'http://rpachallenge.com/assets/downloadFiles/challenge.xlsx', 'challenge.xlsx')
p.sleep(20)

dados = pd.read_excel('challenge.xlsx', sheet_name='Sheet1')
df = pd.DataFrame(dados, columns=['First Name', 'Last Name ',
                                  'Company Name', 'Role in Company', 'Address', 'Email', 'Phone Number'])

# clicando em start
r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')

for row in df.itertuples():  # transforma cada linha em tuplas
    r.type('//*[@ng-reflect-name="labelFirstName"]', row[1])
    r.type('//*[@ng-reflect-name="labelLastName"]', row[2])
    r.type('//*[@ng-reflect-name="labelCompanyName"]', row[3])
    r.type('//*[@ng-reflect-name="labelRole"]', row[4])
    r.type('//*[@ng-reflect-name="labelAdress"]', row[5])
    r.type('//*[@ng-reflect-name="labelEmail"]', row[6])
    r.type('//*[@ng-reflect-name="labelPhone"]', str(row[7]))

    # clicando em submeter
    r.click('/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')

p.sleep(5)
p.screenshot('score.png')
r.close()
