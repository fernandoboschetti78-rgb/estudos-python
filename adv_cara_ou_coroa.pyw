import tkinter as tk
import random

def jogar(escolha):
    resultado = random.choice(["Cara", "Coroa"])
    if escolha == resultado:
        resultado_label.config(text="Você venceu!")
    else:
        resultado_label.config(text="Você perdeu")

janela = tk.Tk()
janela.title("Cara ou Coroa")
janela.geometry("300x200")
texto_label = tk.Label(janela, text="Escolha Cara ou Coroa:")
texto_label.pack(pady=10)
button_cara = tk.Button(janela, text="Cara", command=lambda: jogar("Cara"))
button_coroa = tk.Button(janela, text="Coroa", command=lambda: jogar("Coroa"))
button_cara.pack(pady=10) 
button_coroa.pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=10)

janela.mainloop()