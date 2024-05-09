from tkinter import *

estatistica = Tk() #nome do tk(aplicativo, aplicação, janela...)

estatistica.title("Estátistica") #titulo
estatistica.geometry("500x300") #tamanho da janela
estatistica.configure(background="#ADD8E6") #cor de fundo


fis = []
classes1 = []
classes2 = []

def exibir_quantidade():
    quant_xi = int(entrada_quant_xi.get())
    return quant_xi

Button(estatistica, text="ok", command=exibir_quantidade).place(x=400, y=3, width=30, height=20)

dados = {}
def mostrar_agrupamento_discreto():
    quadro_btn_classes.destroy()

    txt_xi = Label(quadro_dados, text="Xi", background="#ADD8E6", foreground = "#000", anchor=W).place(x=15,y=1, width=100, height = 20)

    txt_fi = Label(quadro_dados, text="fi", background="#ADD8E6", foreground = "#000", anchor=W).place(x=50,y=1, width=100, height = 20)


    for i in range(0, exibir_quantidade()):
        var_nome_xi = f'xi{i}'
        dados[var_nome_xi] = Entry(quadro_dados).place(x=10, y = 21 * (i+1), width=30, height=20)
    
        fis.append(Entry(quadro_dados).place(x=45, y= 21 * (i+1), width=30, height=20))
    return dados
        
def mostrar_agrupamento_classes():
    quadro_btn_discreto.destroy()

    instru_classe = Label(quadro_dados, text="Digite apenas uma classe: ", background="#ADD8E6", foreground = "#000", anchor=W).place(x=10, y= 1, width = 145, height = 20)

    txtclasse = Label(quadro_dados, text="Classes", background="#ADD8E6", foreground = "#000", anchor=W).place(x=10,y=20, width=100, height = 20)

    txtfi = Label(quadro_dados, text="fi", background = "#ADD8E6", foreground = "#000", anchor = W).place(x=80,y=20, width=50, height = 20)

    for i in range(1, exibir_quantidade()+1):
        classes1.append(Entry(quadro_dados).place(x=10, y=21 * (i+1), width=30, height=20))
        classes2.append(Entry(quadro_dados).place(x=40, y=21 * (i+1), width=30, height=20))
        fis.append(Entry(quadro_dados).place(x=75, y=21 * (i+1), width=30, height=20))

    

txt_quantidade = Label(estatistica, text="Digite quantos dados(Xi) ou Classes a amostra contém: ", background="#ADD8E6", foreground = "#000").place(x=-30, y=1, width=400, height=25)

# não mexer aqui, pode dar um erro que não sei o pq que da esse erro
entrada_quant_xi = Spinbox(estatistica, values=(0,1,2,3,4,5)) #aqui
entrada_quant_xi.place(x=310, y=3, width=30, height=20) #e aqui

quadro_btn_discreto = Frame(estatistica,borderwidth = 1, relief= "flat")
quadro_btn_discreto.configure(background="#ADD8E6")
quadro_btn_discreto.place(x=10, y=40, width=160, height=30)

quadro_btn_classes = Frame(estatistica,borderwidth = 1, relief= "flat")
quadro_btn_classes.configure(background="#ADD8E6")
quadro_btn_classes.place(x=220, y=40, width=160, height=30)

quadro_dados = Frame(estatistica,borderwidth = 1, relief= "flat")
quadro_dados.configure(background="#ADD8E6")
quadro_dados.place(x=10, y=70, width=160, height=200)

Button(quadro_btn_discreto, text="Agrupamento discreto", command=mostrar_agrupamento_discreto).place(x=1, y=1, width=150, height=25)

Button(quadro_btn_classes, text="Agrupamento em classes", command=mostrar_agrupamento_classes).place(x=1, y=1, width=150, height=25)


dados = mostrar_agrupamento_discreto()
dados.update()

def listar():
    lista_xi = []
    for i in range(exibir_quantidade()+1):
        indice = dados[f'var{i}']
        lista_xi.append(indice)
    print(lista_xi)

def adicionar_valor():
    # for i in range(0, exibir_quantidade()):
    #     var_nome_xi = f'xi{i}'
    #     dados[var_nome_xi] = Entry(quadro_dados).place(x=10, y = 21 * (i+1), width=30, height=20)
    
    #     fis.append(Entry(quadro_dados).place(x=45, y= 21 * (i+1), width=30, height=20))
    print(dados.get('xi0'))
    return dados

Button(estatistica, text="exibir", command=adicionar_valor).place(x=50, y=230, width=150, height=25)

estatistica.mainloop()