'''
A função deste script é abrir o arquivo .pbix e 
realizar a atualização do banco de dados.
'''

# importando as bibliotecas
import pyautogui as pa

# abrindo o arquivo
pa.hotkey('win', 'r')
pa.sleep(1)

pa.write(r"C:\Users\julio\Documents\teste\power_bi_teste.pbix")
pa.sleep(1)

pa.press('enter')
pa.sleep(20)

pa.click(x=706, y=113)  # clica para atualizar
pa.sleep(20)

pa.click(x=1355, y=9)  # clica para fechar
pa.sleep(3)

pa.click(x=706, y=406)  # clica para salvar