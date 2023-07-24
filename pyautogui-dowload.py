import time
import pyautogui

# Função para mover o mouse até as coordenadas x e y e clicar
def mover_e_clicar(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()

# Aguardar um momento antes de começar
time.sleep(5)

# Coordenadas dos links que serão acessados (pode variar dependendo do site)
links = [
    (100, 200),  # Coordenadas do primeiro link
    (300, 400),  # Coordenadas do segundo link
    (500, 600)   # Coordenadas do terceiro link
]

# Loop para acessar cada link e baixar o relatório
for link in links:
    mover_e_clicar(link[0], link[1])
    # Aguardar um momento para o download ser iniciado (pode variar dependendo do site)
    time.sleep(5)

# Aguardar um momento antes de finalizar o script
time.sleep(5)
