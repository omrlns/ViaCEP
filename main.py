import tkinter as tk
from tkinter import messagebox
import requests

# configuração do tkinter
# janela principal
root = tk.Tk()
root.title("CONSULTA DE CEP")
root.geometry("400x300")

# labels e entradas
tk.Label(root, text="CEP").pack()
entry_cep = tk.Entry(root)
entry_cep.pack()

tk.Label(root, text="LOGRADOURO").pack()
entry_logradouro = tk.Entry(root, width=50)
entry_logradouro.pack()

tk.Label(root, text="BAIRRO").pack()
entry_bairro =  tk.Entry(root, width=50)
entry_bairro.pack()

tk.Label(root, text="CIDADE").pack()
entry_cidade = tk.Entry(root, width=50)
entry_cidade.pack()

tk.Label(root, text="ESTADO").pack()
entry_estado = tk.Entry(root, width=50)
entry_estado.pack()

def buscar_cep():
    cep = entry_cep.get().replace("-", "").strip() # usando entry para fazer referencia ao componente Entry do Tkinter.
    
    if (not cep.isdigit() or len(cep) != 8):
        messagebox.showerror("ERRO!", "DIGITE UM CEP VÁLIDO!")
        return
    
    try:
        url = "https://viacep.com.br/ws/{}/json/".format(cep)
        response = requests.get(url, timeout = 5)
        data = response.json()
    
        if ("erro" in data):
            messagebox.showerror("ERRO!", "CEP NÃO ENCONTRADO!")
            return
        
        entry_logradouro.delete(0, tk.END)
        entry_bairro.delete(0, tk.END)
        entry_cidade.delete(0, tk.END)
        entry_estado.delete(0, tk.END)

        entry_logradouro.insert(0, data.get("logradouro", ""))
        entry_bairro.insert(0, data.get("bairro", ""))
        entry_cidade.insert(0, data.get("localidade", ""))
        entry_estado.insert(0, data.get("uf", ""))
        
    except Exception as e:
        messagebox.showerror("ERRO!", "ERRO AO BUSCAR CEP!\n{}".format(e))

tk.Button(root, text="BUSCAR", command=buscar_cep).pack(pady=10)

root.mainloop()