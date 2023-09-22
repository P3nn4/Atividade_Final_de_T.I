import tkinter as tk

# Função para exibir o menu fictício
def exibir_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title('Menu da Hamburgueria')
    
    # Itens do menu fictício
    menu_items = [
        {'nome': 'Hamburguer Clássico', 'descricao': 'hambúrguer com queijo e alface com batatas e refrigerante grande', 'preco': 29.99},
        {'nome': 'Hamburguer Vegetariano', 'descricao': 'Opção saudável com vegetais frescos', 'preco': 25.99},
        {'nome': 'Combo Infantil', 'descricao': 'Mini hambúrguer com batatas fritas e refrigerante pequeno', 'preco': 9.99},
        
    ]

    # Exibir os itens do menu na janela
    for item in menu_items:
        item_label = tk.Label(menu_window, text=f"{item['nome']} - {item['descricao']} - ${item['preco']:.2f}")
        item_label.pack()

# Configuração da janela principal
root = tk.Tk()
root.title('Aplicativo de Hamburgueria')

# Botão 
menu_button = tk.Button(root, text='Ver Menu', command=exibir_menu)
menu_button.pack()

# Iniciar o loop principal da interface gráfica
root.mainloop()
import tkinter as tk
from tkinter import messagebox

# Função para calcular o total
def calcular_total():
    total = 0
    for item in carrinho:
        total += item['preco']
    return total

# Função para processar o pagamento
def processar_pagamento():
    total = calcular_total()
    messagebox.showinfo("Pagamento", f"Total a pagar: ${total:.2f}\nPagamento processado com sucesso!")

# Função para adicionar item ao carrinho
def adicionar_ao_carrinho(item):
    carrinho.append(item)
    carrinho_listbox.insert(tk.END, item['nome'])

# Função para remover item do carrinho
def remover_do_carrinho():
    selecionado = carrinho_listbox.curselection()
    if selecionado:
        indice = selecionado[0]
        carrinho_listbox.delete(indice)
        carrinho.pop(indice)

# Configuração da janela principal
root = tk.Tk()
root.title('Pagamento - Hamburgueria')

# Inicialização do carrinho
carrinho = []

# Botão para processar pagamento
processar_pagamento_button = tk.Button(root, text='Processar Pagamento', command=processar_pagamento)
processar_pagamento_button.pack()

# Lista de itens no carrinho
carrinho_label = tk.Label(root, text='Carrinho:')
carrinho_label.pack()

carrinho_listbox = tk.Listbox(root)
carrinho_listbox.pack()

# Botão para adicionar itens ao carrinho
item1 = {'nome': 'Hamburguer Clássico', 'preco': 10.99}
item2 = {'nome': 'Hamburguer Vegetariano', 'preco': 9.99}

adicionar_item_button1 = tk.Button(root, text=f'Adicionar {item1["nome"]} - ${item1["preco"]:.2f}', command=lambda: adicionar_ao_carrinho(item1))
adicionar_item_button2 = tk.Button(root, text=f'Adicionar {item2["nome"]} - ${item2["preco"]:.2f}', command=lambda: adicionar_ao_carrinho(item2))

adicionar_item_button1.pack()
adicionar_item_button2.pack()

# Botão para remover itens do carrinho
remover_item_button = tk.Button(root, text='Remover Item', command=remover_do_carrinho)
remover_item_button.pack()

# Iniciar o loop principal da interface gráfica
root.mainloop()
