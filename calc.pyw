import tkinter as tk
import ctypes as c

janela = tk.Tk()
janela.title("test")
janela.geometry("200x200")

def custom_notify():
    text = txt.get().lower().strip()
    if "x" in text:
        text = text.replace("x", "*")
    if "÷" in text:
        text = text.replace("÷", "/")
    if "^" in text:
        text = text.replace("^", "**")
    try:
        result = eval(text)
        c.windll.user32.MessageBoxW(0, f"o resultado é {result}", "resultado", 0x40 | 0x1)
    except:
        c.windll.user32.MessageBoxW(0,"erro", "algo deu errado", 0x40 | 0x1)
    
        


txt = tk.Entry(janela)
txt.pack(pady=20)

enviar = tk.Button(janela, text="enviar", command=custom_notify)
enviar.pack(pady=20)
janela.mainloop()

