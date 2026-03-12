import pyautogui
import time

# tempo de espera entre os comandos do Pyautogui
pyautogui.PAUSE = 0.7

# abrir o sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# fazer o login
time.sleep(5) # tempo para executar

pyautogui.click(x=785, y=508)
pyautogui.write("diegoomarcelo@gmail.com")
pyautogui.press("tab")
pyautogui.write("essasenhateste")
pyautogui.press("tab")
pyautogui.press("enter")



