'''
A função deste script é abrir o arquivo .pbix e 
realizar a atualização do banco de dados.
'''

# importando as bibliotecas
import pyautogui as pa

# abrindo o arquivo
pa.hotkey('win', 'r')
pa.sleep(1)

pa.write("C: \Users\julio\Documents\power_bi_teste.pbix)
pa.sleep(1)

pa.press('enter')
pa.sleep(30)

pa.click(x=706, y=113)  # clica para atualizar
pa.sleep(30)

pa.click(x=1355, y=9)  # clica para fechar
pa.sleep(3)

pa.click(x=706, y=406)  # clica para salvar
