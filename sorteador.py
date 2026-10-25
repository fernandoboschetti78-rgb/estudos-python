import sqlite3 as sq
import tkinter as tk
import random

conect = sq.connect("nomes")
cursor = conect.cursor()

cursor.execute("SELECT nome FROM nomes")

nomes = cursor.fetchall()

cursor.execute("SELECT complemento FROM complementos")

complementos = cursor.fetchall()

def sortear():
    r1 = random.choice(nomes)
    r1 = r1[0]
    r2 = random.choice(complementos)
    r2 = r2[0]
    result_label.config(text=f"{r1} {r2}")

janela = tk.Tk()
janela.geometry("300x130")
janela.title("seu nome de comercio")

botao = tk.Button(janela, text="criar", command=sortear)
result_label = tk.Label(janela, text="")
botao.pack(pady=20)
result_label.pack(pady=20)
janela.mainloop()