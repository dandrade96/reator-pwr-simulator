import tkinter as tk

# Função chamada quando o botão é clicado
def botao_clicado():
    label.config(text="Botão clicado!")

# Criar a janela
janela = tk.Tk()

# Criar um rótulo
label = tk.Label(janela, text="Olá, mundo!")
label.pack()

# Criar um botão
botao = tk.Button(janela, text="Clique aqui", command=botao_clicado)
botao.pack()

# Executar a janela principal
janela.mainloop()
