from tkinter import *
from math import sqrt

estatistica = Tk() #nome do tk(aplicativo, aplicação, janela...)

estatistica.title("Estátistica") #titulo
estatistica.geometry("500x300") #tamanho da janela
estatistica.configure(background="#ADD8E6") #cor de fundo

fis = []
classes1 = []
classes2 = []

def quantidade_xi():
    return int(entrada_quant_xi.get())
     
dados = []
valores_xi = []
valores_fi = []
def mostrar_agrupamento_discreto():
    quadro_btn_classes.destroy()

    txt_xi = Label(quadro_dados, text="Xi", background="#ADD8E6", foreground = "#000", anchor=W)
    txt_xi.place(x=15,y=1, width=100, height = 20)

    txt_fi = Label(quadro_dados, text="fi", background="#ADD8E6", foreground = "#000", anchor=W)
    txt_fi.place(x=50,y=1, width=100, height = 20)

    for i in range(quantidade_xi()):
        xi = Entry(quadro_dados)
        xi.place(x=10, y=21 * (i + 1), width=30, height=20)
        dados.append(xi)

        fi = Entry(quadro_dados)
        fi.place(x=45, y= 21 * (i+1), width=30, height=20)
        fis.append(fi)

    return dados
        
def mostrar_agrupamento_classes():
    quadro_btn_discreto.destroy()

    instru_classe = Label(quadro_dados, text="Digite apenas uma classe: ", background="#ADD8E6", foreground = "#000", anchor=W).place(x=10, y= 1, width = 145, height = 20)

    txtclasse = Label(quadro_dados, text="Classes", background="#ADD8E6", foreground = "#000", anchor=W).place(x=10,y=20, width=100, height = 20)

    txtfi = Label(quadro_dados, text="fi", background = "#ADD8E6", foreground = "#000", anchor = W).place(x=80,y=20, width=50, height = 20)

    for i in range(1, quantidade_xi()+1):
        classes1.append(Entry(quadro_dados).place(x=10, y=21 * (i+1), width=30, height=20))
        classes2.append(Entry(quadro_dados).place(x=40, y=21 * (i+1), width=30, height=20))
        fis.append(Entry(quadro_dados).place(x=75, y=21 * (i+1), width=30, height=20))

def coletar_dados():
    
    for entry in dados:
        valor = entry.get()  
        valores_xi.append(float(valor))
    return valores_xi

def coletar_fis():
    
    for entry in fis:
        valor = entry.get()  
        valores_fi.append(float(valor))
    return valores_fi

txt_quantidade = Label(estatistica, text="Digite quantos dados(Xi) ou Classes a amostra contém: ", background="#ADD8E6", foreground = "#000").place(x=-30, y=1, width=400, height=25)

# não mexer aqui, pode dar um erro que não sei o pq que da esse erro
entrada_quant_xi = Spinbox(estatistica, values=(0,1,2,3,4,5)) #aqui
entrada_quant_xi.place(x=315, y=3, width=30, height=20) #e aqui

#frames
quadro_btn_discreto = Frame(estatistica,borderwidth = 1, relief= "flat")
quadro_btn_discreto.configure(background="#ADD8E6")
quadro_btn_discreto.place(x=10, y=40, width=160, height=30)

quadro_btn_classes = Frame(estatistica,borderwidth = 1, relief= "flat")
quadro_btn_classes.configure(background="#ADD8E6")
quadro_btn_classes.place(x=220, y=40, width=160, height=30)

quadro_dados = Frame(estatistica,borderwidth = 1, relief= "flat")
quadro_dados.configure(background="#ADD8E6")
quadro_dados.place(x=10, y=70, width=160, height=200)

#Botões
btn_discreto = Button(quadro_btn_discreto, text="Agrupamento discreto", command=mostrar_agrupamento_discreto)
btn_discreto.place(x=1, y=1, width=150, height=25)



def calculos():
    
    valores_xi = coletar_dados()
    valores_fi = coletar_fis()

    N = 0
    S2 = 0
    variancias = []
    soma_Xi_vezes_fi = 0

    for i in range(0, quantidade_xi()):
        i = i+1
        N += valores_fi[i]
        soma_Xi_vezes_fi += valores_xi[i] * valores_fi[i]
        
    for i in range(0, quantidade_xi()):
        soma_Xi_vezes_fi = round(soma_Xi_vezes_fi, 2)

    N = round(N, 2)
    media = round(soma_Xi_vezes_fi / N, 2)
    for i in range(0, quantidade_xi()):
        variancias.append(round((valores_xi[i] - media) ** 2 * valores_fi[i],2))

    for i in variancias:
        S2 += i

    S2 = round(S2/(N-1), 2)
    s = round(sqrt(S2),2)
    cv = round((100 * s) / media, 2)

    print("-=" * 5 ,"Resultados", "=-" * 5)
    print("ẋ = ", media)
    print("S2 = ", S2)
    print("s = ", s)
    print("CV = ", cv)

btn_classes = Button(quadro_btn_classes, text="Agrupamento em classes", command=mostrar_agrupamento_classes)
btn_classes.place(x=1, y=1, width=150, height=25)

Button(estatistica, text="Calcular", command=calculos).place(x=50, y=230, width=150, height=25)
Button(estatistica, text="Exibir F", command=lambda: print(coletar_fis())).place(x=50, y=270, width=150, height=25)
Button(estatistica, text="Exibir D", command=lambda: print(coletar_dados())).place(x=50, y=300, width=150, height=25)




estatistica.mainloop()