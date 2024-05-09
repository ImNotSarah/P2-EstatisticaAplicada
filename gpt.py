from tkinter import *

# Criar o Tkinter root
estatistica = Tk() 

# Configurações da janela
estatistica.title("Estatística")
estatistica.geometry("500x300")
estatistica.configure(background="#ADD8E6")

# Lista para armazenar widgets Entry
dados_entries = []

# Função para obter a quantidade do Spinbox
def exibir_quantidade():
    return int(entrada_quant_xi.get())

# Função para criar e armazenar Entries
def mostrar_agrupamento_discreto():
    # Obter a quantidade de Entries
    quantidade = exibir_quantidade()

    # Limpar a lista de Entries para uma nova iteração
    dados_entries.clear()

    # Criar e posicionar as Entries, adicionando-as à lista
    for i in range(quantidade):
        entry = Entry(estatistica)
        entry.place(x=10, y=21 * (i + 1), width=30, height=20)  # Ajustar a posição
        dados_entries.append(entry)  # Adicionar à lista

# Função para coletar o texto de cada Entry e armazenar em uma lista de valores
def coletar_dados():
    valores = []
    for entry in dados_entries:
        valor = entry.get()  # Obter o valor digitado no Entry
        valores.append(valor)
    return valores

# Configuração do Spinbox e botão para coletar os dados
entrada_quant_xi = Spinbox(estatistica, from_=1, to_=10)  # Defina o intervalo conforme necessário
entrada_quant_xi.place(x=10, y=10)

# Botão para criar Entries com a função definida
Button(estatistica, text="Criar Entries", command=mostrar_agrupamento_discreto).place(x=150, y=10)

# Botão para coletar valores digitados
Button(estatistica, text="Coletar Dados", command=lambda: print(coletar_dados())).place(x=250, y=10)

# Loop principal
estatistica.mainloop()