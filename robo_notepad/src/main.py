import pyautogui as p 

p.hotkey('win', 'r')
p.sleep(1)

p.typewrite('notepad')
p.sleep(2)

p.press('enter')
p.sleep(2)

p.typewrite('Oi! Eu sou um texto')
p.sleep(2)

valor = p.getActiveWindow()
valor.close()

p.press('right')
p.sleep(2)

p.press('enter')