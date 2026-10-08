import ctypes
import tkinter as tk
import os
import shutil
def atualizar():
    if not os.path.exists("C:\\Users\\Public\\Documents\\NewFolder"):
        delete_folder_btn.config(state=tk.DISABLED)
        create_folder.config(state=tk.NORMAL)
        create_txt_btn.config(state=tk.DISABLED)
        delete_txt_btn.config(state=tk.DISABLED)
        create_sourcecode_btn.config(state=tk.DISABLED)
        delete_sourcecode_btn.config(state=tk.DISABLED)
    elif os.path.exists("C:\\Users\\Public\\Documents\\NewFolder"):
        delete_folder_btn.config(state=tk.NORMAL)   
        create_folder.config(state=tk.DISABLED)
        create_sourcecode_btn.config(state=tk.NORMAL)
        delete_sourcecode_btn.config(state=tk.DISABLED)
        if os.path.exists("C:\\Users\\Public\\Documents\\NewFolder\\painel.py"):
            delete_sourcecode_btn.config(state=tk.NORMAL)
            create_sourcecode_btn.config(state=tk.DISABLED)
        else:
            delete_sourcecode_btn.config(state=tk.DISABLED)
            create_sourcecode_btn.config(state=tk.NORMAL)
        if os.path.exists("C:\\Users\\Public\\Documents\\NewFolder\\txt.txt"):
            create_txt_btn.config(state=tk.DISABLED)
            delete_txt_btn.config(state=tk.NORMAL)
        else:
            create_txt_btn.config(state=tk.NORMAL)
            delete_txt_btn.config(state=tk.DISABLED)
    janela.after(1000, atualizar)
def shutdown():
    confirm = ctypes.windll.user32.MessageBoxW(0, "Tem certeza que deseja desligar o computador?", "Confirmação", 0x40 | 0x1)
    if confirm == 1:  
        os.system("shutdown /s /t 0")
def createfolder():
    os.makedirs("C:\\Users\\Public\\Documents\\NewFolder", exist_ok=True)
    atualizar()
def notify():
    ctypes.windll.user32.MessageBoxW(0, "você se notificou", "painel", 0x40 | 0x1)
def delete_folder():
    folder_path = "c:\\users\\public\\documents\\newfolder"   
    shutil.rmtree(folder_path)
    atualizar()
def create_txt():
    with open("C:\\Users\\Public\\Documents\\NewFolder\\txt.txt", "w") as f:
        f.write("arquivo padrão")
def delete_txt():
    txt_path = "C:\\Users\\Public\\Documents\\NewFolder\\txt.txt"
    os.remove(txt_path)
    atualizar()
def copy_sourcecode():
    source_path = os.path.abspath(__file__)
    destination_path = "C:\\Users\\Public\\Documents\\NewFolder\\painel.py"
    shutil.copy(source_path, destination_path)
    atualizar()

def delete_sourcecode():
    source_path = "C:\\Users\\Public\\Documents\\NewFolder\\painel.py"
    os.remove(source_path)
    atualizar()

def exit_program():
    janela.destroy()

janela = tk.Tk()
janela.title("painel")
janela.geometry("400x420")

shut = tk.Button(janela, text="desligar", command=shutdown)
shut.pack(pady=10)

create_folder = tk.Button(janela, text="criar pasta", command=createfolder)
create_folder.pack(pady=10)

delete_folder_btn = tk.Button(janela, text="deletar pasta", command=delete_folder)
delete_folder_btn.pack(pady=10)

create_txt_btn = tk.Button(janela, text="criar txt", command=create_txt)
create_txt_btn.pack(pady=10)

delete_txt_btn = tk.Button(janela, text="deletar txt", command=delete_txt)
delete_txt_btn.pack(pady=10)

create_sourcecode_btn = tk.Button(janela, text="copiar código fonte", command=copy_sourcecode)
create_sourcecode_btn.pack(pady=10)

delete_sourcecode_btn = tk.Button(janela, text="deletar código fonte", command=delete_sourcecode)
delete_sourcecode_btn.pack(pady=10)

notify_btn = tk.Button(janela, text="notificar", command=notify)
notify_btn.pack(pady=10)

exit_btn = tk.Button(janela, text="sair", command=exit_program)
exit_btn.pack(pady=10)

atualizar()

janela.mainloop()