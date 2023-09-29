import tkinter as tk

from tkinter import messagebox

 

# Função para exibir uma mensagem informativa

def exibir_mensagem(mensagem):

    messagebox.showinfo("Mensagem", mensagem)

 

# Função para avançar para a próxima tela

def avancar_tela():

    global tela_atual

    tela_atual += 1

    atualizar_tela()

 

# Função para voltar para a tela anterior

def voltar_tela():

    global tela_atual

    tela_atual -= 1

    atualizar_tela()

 

# Função para realizar o login

def fazer_login():

    usuario = entrada_usuario.get()

    senha = entrada_senha.get()

   

    if not usuario or not senha:

        exibir_mensagem("Preencha todos os campos para fazer o login.")

    else:

        # Adicione aqui a lógica de login, por exemplo, verificar credenciais

        # Neste exemplo, estamos apenas simulando um login bem-sucedido

        exibir_mensagem("Login bem-sucedido!")

        avancar_tela()

 

# Função para fazer um pedido

def fazer_pedido():

    global pedido, total_a_pagar, pedido_id

    pedido = ""

    total_a_pagar = 0

    hamburgo = hamburgo_var.get()

    combo = combo_var.get()

   

    if hamburgo != "":

        preco_hamburgo = precos[hamburgo]

        pedido += f"Hambúrguer ({hamburgo}): R$ {preco_hamburgo:.2f}\n"

        total_a_pagar += preco_hamburgo

 

    if combo != "":

        preco_combo = combos[combo]

        pedido += f"Combo ({combo}): R$ {preco_combo:.2f}\n"

        total_a_pagar += preco_combo

 

    if batata_var.get():

        pedido += "Batata: R$ 11.99\n"

        total_a_pagar += 11.99

 

    if refrigerante_var.get():

        pedido += "Refrigerante: R$ 13.49\n"

        total_a_pagar += 2.49

 

    pedido_id += 1

    pedido += f"Pedido ID: {pedido_id}\n"

   

    if pedido == "":

        exibir_mensagem("Selecione pelo menos um item para fazer o pedido.")

    else:

        exibir_mensagem(f"Pedido:\n{pedido}\nTotal a Pagar: R$ {total_a_pagar:.2f}")

        avancar_tela()

 

# Função para finalizar o pedido

def finalizar_pedido():

    forma_pagamento = pagamento_var.get()

    if not forma_pagamento:

        exibir_mensagem("Selecione a forma de pagamento.")

    else:

        exibir_mensagem(f"Pedido finalizado com sucesso!\nForma de pagamento: {forma_pagamento}\nTotal a Pagar: R$ {total_a_pagar:.2f}")

 

# Função para fazer o cadastro do cliente

def fazer_cadastro():

    global cliente_info

    cliente_info = ""

    nome_cliente = nome_var.get()

    telefone_cliente = telefone_var.get()

   

    if not nome_cliente or not telefone_cliente:

        exibir_mensagem("Preencha todos os campos para fazer o cadastro.")

    else:

        cliente_info += f"Nome: {nome_cliente}\n"

        cliente_info += f"Telefone: {telefone_cliente}\n"

        avancar_tela()

 

# Função para atualizar a tela com base no valor de tela_atual

def atualizar_tela():

    if tela_atual == 0:

        tela_login.pack()

        tela_cadastro.pack_forget()

        tela_pedido.pack_forget()

        tela_pagamento.pack_forget()

        botao_voltar.config(state="disabled")

    elif tela_atual == 1:

        tela_login.pack_forget()

        tela_cadastro.pack()

        tela_pedido.pack_forget()

        tela_pagamento.pack_forget()

        botao_voltar.config(state="active")

        botao_avancar.config(state="active")

    elif tela_atual == 2:

        tela_login.pack_forget()

        tela_cadastro.pack_forget()

        tela_pedido.pack()

        tela_pagamento.pack_forget()

        botao_voltar.config(state="active")

        botao_avancar.config(state="active")

    elif tela_atual == 3:

        if cliente_info:

            tela_login.pack_forget()

            tela_cadastro.pack_forget()

            tela_pedido.pack_forget()

            tela_pagamento.pack()

            botao_avancar.config(state="disabled")

        else:

            exibir_mensagem("Você deve fazer o cadastro antes de continuar.")

 

# Inicialização

tela_atual = 0

pedido = ""

cliente_info = ""

total_a_pagar = 0

pedido_id = 0

 

# Configuração dos preços dos produtos

precos = {

    "Hambúrguer Simples": 15.99,

    "Hambúrguer Duplo": 18.99,

    "Batata": 11.99,

    "Refrigerante": 13.49

}

 

# Configuração dos combos

combos = {

    "Combo 1 (Simples + Batata + Refrigerante)": 29.99,

    "Combo 2 (Duplo + Batata + Refrigerante)": 39.99

}

 

# Configuração da janela principal

root = tk.Tk()

root.title("Hamburgueria App")

 

# Tela de Login

tela_login = tk.Frame(root)

 

label_login = tk.Label(tela_login, text="Login")

label_login.pack()

 

# Campos de entrada de usuário e senha

label_usuario = tk.Label(tela_login, text="Usuário:")

label_usuario.pack()

 

entrada_usuario = tk.Entry(tela_login)

entrada_usuario.pack()

 

label_senha = tk.Label(tela_login, text="Senha:")

label_senha.pack()

 

entrada_senha = tk.Entry(tela_login, show="*")

entrada_senha.pack()

 

botao_login = tk.Button(tela_login, text="Login", command=fazer_login)

botao_login.pack()

 

# Tela de Cadastro

tela_cadastro = tk.Frame(root)

 

label_cadastro = tk.Label(tela_cadastro, text="Cadastro de Cliente")

label_cadastro.pack()

 

label_nome = tk.Label(tela_cadastro, text="Nome:")

label_nome.pack()

 

nome_var = tk.StringVar()

entrada_nome = tk.Entry(tela_cadastro, textvariable=nome_var)

entrada_nome.pack()

 

label_telefone = tk.Label(tela_cadastro, text="Telefone:")

label_telefone.pack()

 

telefone_var = tk.StringVar()

entrada_telefone = tk.Entry(tela_cadastro, textvariable=telefone_var)

entrada_telefone.pack()

 

botao_cadastro = tk.Button(tela_cadastro, text="Cadastrar", command=fazer_cadastro)

botao_cadastro.pack()

 

# Tela de Pedido

tela_pedido = tk.Frame(root)

 

label_pedido = tk.Label(tela_pedido, text="Faça seu Pedido")

label_pedido.pack()

 

hamburgo_var = tk.StringVar()

hamburgo_var.set("")  # Opção padrão

 

label_hamburgo = tk.Label(tela_pedido, text="Escolha o Hambúrguer:")

label_hamburgo.pack()

 

hamburgo_optionmenu = tk.OptionMenu(tela_pedido, hamburgo_var, *precos.keys())

hamburgo_optionmenu.pack()

 

combo_var = tk.StringVar()

combo_var.set("")  # Opção padrão

 

label_combo = tk.Label(tela_pedido, text="Escolha um Combo:")

label_combo.pack()

 

combo_optionmenu = tk.OptionMenu(tela_pedido, combo_var, *combos.keys())

combo_optionmenu.pack()

 

label_preco = tk.Label(tela_pedido, text="Preço:")

label_preco.pack()

 

preco_label = tk.Label(tela_pedido, text="")

preco_label.pack()

 

def atualizar_preco():

    hamburgo_selecionado = hamburgo_var.get()

    combo_selecionado = combo_var.get()

    preco_hamburgo = precos.get(hamburgo_selecionado, 0)

    preco_combo = combos.get(combo_selecionado, 0)

    preco_total = preco_hamburgo + preco_combo

    preco_label.config(text=f"Preço: R$ {preco_total:.2f}")

 

hamburgo_var.trace_add("write", lambda *args: atualizar_preco())

combo_var.trace_add("write", lambda *args: atualizar_preco())

 

batata_var = tk.BooleanVar()

batata_checkbox = tk.Checkbutton(tela_pedido, text="Batata (R$ 4.99)", variable=batata_var)

batata_checkbox.pack()

 

refrigerante_var = tk.BooleanVar()

refrigerante_checkbox = tk.Checkbutton(tela_pedido, text="Refrigerante (R$ 2.49)", variable=refrigerante_var)

refrigerante_checkbox.pack()

 

botao_pedido = tk.Button(tela_pedido, text="Fazer Pedido", command=fazer_pedido)

botao_pedido.pack()

 

# Tela de Pagamento

tela_pagamento = tk.Frame(root)

 

label_pagamento = tk.Label(tela_pagamento, text="Pagamento")

label_pagamento.pack()

 

# Opções de pagamento

pagamento_var = tk.StringVar()

pagamento_var.set("")  # Opção padrão

 

label_forma_pagamento = tk.Label(tela_pagamento, text="Escolha a Forma de Pagamento:")

label_forma_pagamento.pack()

 

pagamento_optionmenu = tk.OptionMenu(tela_pagamento, pagamento_var, "Cartão de Crédito", "Dinheiro", "Pix")

pagamento_optionmenu.pack()

 

botao_pagamento = tk.Button(tela_pagamento, text="Finalizar Pedido", command=finalizar_pedido)

botao_pagamento.pack()

 

# Botões para avançar e voltar

botao_voltar = tk.Button(root, text="Voltar", command=voltar_tela, state="disabled")

botao_voltar.pack(side=tk.LEFT)

 

botao_avancar = tk.Button(root, text="Avançar", command=avancar_tela)

botao_avancar.pack(side=tk.RIGHT)

 

# Iniciar com a tela de login

atualizar_tela()

 

root.mainloop()
