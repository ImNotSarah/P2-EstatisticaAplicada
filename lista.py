from customtkinter  import *

from math import sqrt

estatistica = CTk() #nome do tk(aplicativo, aplicação, janela...)

estatistica.title("Estátistica") #titulo
estatistica.geometry("800x500") #tamanho da janela

set_appearance_mode("dark")

fis = []
classes1 = []
classes2 = []
dados = []
valores_xi = []
valores_fi = []

opções = ["Agrupamento Discreto", "Agrupamento em Classes"]

def escolher(value):
    sla = str(combobox.get())
    if sla == "Agrupamento Discreto":
        mostrar_agrupamento_discreto()
    else:
        mostrar_agrupamento_classes()

combobox = CTkComboBox(estatistica, values=["Agrupamento Discreto", "Agrupamento em Classes"], command=escolher, width= 185, height=30, )
combobox.place(x=165, y=40)

def quantidade_xi():
    return int(entrada_quant_xi.get())


def limpar_frame():
    for widget in quadro_dados.winfo_children():
        widget.destroy()

def mostrar_agrupamento_discreto():
    limpar_frame()
    
    txt_xi = CTkLabel(quadro_dados, text="Xi", width=100, height = 20, anchor=W)
    txt_xi.place(x=40,y=20)

    txt_fi = CTkLabel(quadro_dados, text="fi", width=100, height = 20, anchor=W)
    txt_fi.place(x=105,y=20)

    for i in range(quantidade_xi()):
        xi = CTkEntry(quadro_dados, width=45, height=20)
        xi.place(x=25, y=(21 * (i+1)) + 20)
        dados.append(xi)

        fi = CTkEntry(quadro_dados, width=45, height=20)
        fi.place(x=85, y= 21 * (i+1) + 20)
        fis.append(fi)
    return dados
        
def mostrar_agrupamento_classes():

    limpar_frame()
    
    instru_classe = CTkLabel(quadro_dados, text="Digite apenas uma classe: ", width = 145, height = 20, anchor=W).place(x=10, y= 1)

    txtclasse = CTkLabel(quadro_dados, text="Classes", width=100, height = 20, anchor=W).place(x=10,y=20)

    txtfi = CTkLabel(quadro_dados, text="fi", width=50, height = 20, anchor = W).place(x=80,y=20)

    for i in range(1, quantidade_xi()+1):
        classes1.append(CTkEntry(quadro_dados, width=30, height=20).place(x=10, y=21 * (i+1)))
        classes2.append(CTkEntry(quadro_dados, width=30, height=20).place(x=40, y=21 * (i+1)))
        fis.append(CTkEntry(quadro_dados, width=30, height=20).place(x=75, y=21 * (i+1),))

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
    x= 150
    
    CTkLabel(estatistica, text=f"Média = {media}", width=100, height = 20, anchor=W).place(x=x, y=91)
    CTkLabel(estatistica, text=f"Variância = {S2}", width=100, height = 20, anchor=W).place(x=x,y=111)
    CTkLabel(estatistica, text=f"Desvio Padrão = {s}", width=100, height = 20, anchor=W).place(x=x,y=131)
    CTkLabel(estatistica, text=f"Coeficiente Padrão = {cv}", width=100, height = 20, anchor=W).place(x=x,y=151)

txt_quantidade = CTkLabel(estatistica, text="Digite quantos dados(Xi) ou Classes a amostra contém: ")
txt_quantidade.place(x=10, y=1)

# não mexer aqui, pode dar um erro sem explicação (até o momento)
entrada_quant_xi = CTkEntry(estatistica, width=30, height=20)
entrada_quant_xi.place(x=330, y=3) #e aqui

#frames
# quadro_btn_discreto = CTkFrame(estatistica, width=170, height=40)
# quadro_btn_discreto.place(x=15, y=180)

# quadro_btn_classes = CTkFrame(estatistica,width=180, height=40)
# quadro_btn_classes.place(x=205, y=180)

quadro_dados = CTkFrame(estatistica,width=160, height=180)
quadro_dados.place(x=120, y=230)

quadro_resultados = CTkFrame(estatistica,width=400, height=500)
quadro_resultados.place(x=400, y=0)

#Botões
#btn_discreto = CTkButton(quadro_btn_discreto, text="Agrupamento discreto", command=mostrar_agrupamento_discreto, width=150, height=25)
#btn_discreto.place(x=8.8, y=8)

# btn_classes = CTkButton(quadro_btn_classes, text="Agrupamento em classes", command=mostrar_agrupamento_classes, width=150, height=25)
# btn_classes.place(x=11, y=8)

# btn_calcular = CTkButton(estatistica, text="Calcular", command=lambda:(coletar_dados(), coletar_fis(), calculos()), width=100, height=25)
# btn_calcular.place(x=165, y=450)

estatistica.mainloop()