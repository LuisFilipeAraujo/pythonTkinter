import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title('Treinanado Tkinter')
root.geometry("600x300")
root.maxsize(600,320)
root.minsize(600,320)
root.configure(background='#E6E6FA')

def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text='Olá, ' + nome_usuario)
    
def get_data():
    data_atual = strftime(' %a, %d %b %Y')
    data.config(text=data_atual)
    
def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text=hora_atual)
    horas.after(1000, get_horas)

tela = tk.Canvas(root, width=600, height=60, bg='#E6E6FA', bd=0, highlightthickness=0, relief='ridge')
tela.pack()

saudacao = Label(root, bg='#E6E6FA', fg='#DC143C', font=('Montserrat', 16))
saudacao.pack()

data = Label(root, bg='#E6E6FA', fg='#DC143C', font=('Montserrat', 14))
data.pack(pady=2)

horas = Label(root, bg='#E6E6FA', fg='#DC143C', font=('Montserrat', 64, 'bold'))
horas.pack(pady=2)



get_saudacao()
get_data()
get_horas()
root.mainloop()