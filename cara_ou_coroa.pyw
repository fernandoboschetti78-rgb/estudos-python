import tkinter as tk
import random

def jogar():
    resultado = random.choice(["cara", "coroa"])
    resultado_label.config(text=f"caiu {resultado}")

janela = tk.Tk()
janela.title("Cara ou Coroa")
janela.geometry("200x150")
texto_label = tk.Label(janela, text="jogue a moeda")
texto_label.pack(pady=10)

button_jogar = tk.Button(janela, text="Jogar", command=jogar)
button_jogar.pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=10)

janela.mainloop()