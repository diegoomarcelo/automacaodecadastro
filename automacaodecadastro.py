import pyautogui
import time
import pandas as pd

# importar a base de produtos no arquivo CSV
tabela = pd.read_csv("produtos.csv")

# tempo de espera entre os comandos do Pyautogui
pyautogui.PAUSE = 1

# abrir o sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# fazer o login
time.sleep(4) # tempo para executar

pyautogui.click(x=785, y=508)
pyautogui.write("diegoomarcelo@gmail.com")
pyautogui.press("tab")
pyautogui.write("essasenhateste")
pyautogui.press("tab")
pyautogui.press("enter")

# cadastrar os produtos
# para cada linha um produto será cadastrado. 
for linha in tabela.index:
    pyautogui.click(x=801, y=364) #clicar no primeiro campo
    pyautogui.write(str(tabela.loc[linha, "codigo"])) #pegando o código da tabela e escrevendo no campo
    pyautogui.press("tab") # passando para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]): #pra ver se tem observação, caso não tenha não vai preencher
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    time.sleep(0.7)
   # pyautogui.scroll(-380)
    pyautogui.click(x=848, y=687)
    pyautogui.scroll(1000)
        







