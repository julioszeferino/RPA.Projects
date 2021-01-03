#pip install numpy==1.19.3
import pyautogui as p 

p.doubleClick(x=100, y=49) #abre o navegador
p.sleep(4)

p.write('www.udemy.com')
p.press('enter')

p.sleep(3)


localpesq = p.locateOnScreen(r'C:\Users\julio\Documents\Local_Github\RPA.projects\RPA.Projects\robo_visual_automation\pesquisa.png', confidence = 0.9) #4 coordenadas da imagem
localpesquisa = p.center(localpesq)
print(localpesq)

x_pesq, y_pesq = localpesquisa

p.move(x_pesq, y_pesq, duration=1)

p.click(x_pesq, y_pesq)

p.sleep(1)
p.write('Charles Lima')


#p.sleep(2)
#print(p.position())