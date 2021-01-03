import rpa as r
import pyautogui as p

r.init()
r.url('https://www.google.com')

janela = p.getActiveWindow()
janela.maximize()

r.wait(2.0)  # esperar 2 seg
r.type('//*[@name="q"]', 'RPA[enter]')
# r.type('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input', 'RPA[enter]')
r.wait(2.0)
r.snap('page', 'rpa_page.png')  # tira o print
r.wait(2.0)
r.close()
