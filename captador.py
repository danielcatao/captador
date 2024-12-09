from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import time
from tkinter import *

temperature = 0
umidade = 0
dia_hora = ''

def search_result():
    bot = webdriver.Firefox()
    bot.get('https://www.google.com/')
    time.sleep(2)
    result = bot.find_element(By.XPATH, '//*[@id="APjFqb"]')
    result.clear()
    result.send_keys('temperatura são paulo')
    result.send_keys(Keys.ENTER)
    time.sleep(2)

    global temperature
    temperature = bot.find_element(By.ID, 'wob_tm').text
    global umidade
    umidade = bot.find_element(By.ID, 'wob_hm').text
    global dia_hora
    dia_hora = bot.find_element(By.ID, 'wob_dts').text

    text_box.delete('1.0', END)
    text_box.insert(END, 'Temp:'+temperature+'°C Umid:'+umidade)

def save_result():
    wb = load_workbook('C:\\Users\\Daniel\\Desktop\\temperaturas-sp.xlsx')
    page = wb.active
    page.append([dia_hora, temperature, umidade])
    wb.save('C:\\Users\\Daniel\\Desktop\\temperaturas-sp.xlsx')

window = Tk()
window.geometry("450x200")
window.title("Captador")

b1 = Button(window, text="Buscar Dados", command=search_result, width=12, bg="gray")
b1.place(x=150,y=50)

b2 = Button(window, text="Salvar Dados", command=save_result, width=12, bg="gray")
b2.place(x=150,y=100)

text_box = Text(window, height=1, width=40)
text_box.place(x=50,y=15)
text_box.pack()

window.mainloop()