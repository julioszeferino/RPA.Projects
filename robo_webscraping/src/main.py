import rpa as r
import pyautogui as p
import pandas as pd
import xlrd
import openpyxl
import os as o

r.init()
r.url('https://rpachallengeocr.azurewebsites.net/')

janela = p.getActiveWindow()
janela.maximize()
p.sleep(7)

countpage = 1
while countpage <= 3:
    if countpage == 1:
        r.table('//*[@id="tableSandbox"]', 'Temp.csv')  # a tabela
        dados = pd.read_csv("Temp.csv")
        dados.to_csv(r'WebTable.csv', mode='a', index=None, header=True)
        r.click('//*[@id="tableSandbox_next"]')  # botao next
        countpage = countpage + 1
    else:
        r.table('//*[@id="tableSandbox"]', 'Temp.csv')  # a tabela
        dados = pd.read_csv("Temp.csv")
        dados.to_csv(r'WebTable.csv', mode='a', index=None,
                     header=False)  # sem cabeçalho
        r.click('//*[@id="tableSandbox_next"]')  # botao next
        countpage = countpage + 1
r.close()

o.remove('Temp.csv')  # removendo o arquivo temporario

csv_xlsx = pd.read_csv(r'WebTable.csv')
csv_xlsx.to_excel(r'WebTable.xlsx')
