import tkinter as tk
import os
import shutil as s
import ctypes as c
import string

discos = [f"{letra}:\\" for letra in string.ascii_uppercase if os.path.exists(f"{letra}:\\")]

def procurar():
    target = text.get()
    encontrado = False
    if target != "":
        for disco in discos:
            for root, dirs, files in os.walk(disco):
                for arquivo in files + dirs:
                    if target == arquivo:
                        caminho = os.path.join(root, arquivo)
                        notificação = c.windll.user32.MessageBoxW(0, f"o arquivo foi encontrado em {caminho} deseja abrir?", "arquivo", 0x40 | 0x1)
                        encontrado = True
                        if notificação == 1:
                            os.startfile(caminho)
                        break
                if encontrado:
                    break
        if not encontrado:
            c.windll.user32.MessageBoxW(0, "arquivo não encontrado", "falha", 0x40 | 0x1)
    
janela = tk.Tk()
janela.title("procurar")
janela.geometry("300x300")

text = tk.Entry(janela)
text.pack(pady=20)

botão = tk.Button(janela, text="localizar", command=procurar)
botão.pack(pady=20)


janela.mainloop()