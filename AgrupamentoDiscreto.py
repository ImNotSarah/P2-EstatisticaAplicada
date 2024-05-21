from customtkinter  import *
from math import sqrt

estatistica = CTk() #nome do tk(aplicativo, aplicação, janela...)

estatistica.title("Estátistica") #titulo
estatistica.geometry("900x600") #tamanho da janela

set_appearance_mode("dark")

fis = []
dados = []
valores_xi = []
valores_fi = []

def limpar_frames():
    for widget in quadro_dados.winfo_children():
        widget.destroy()
    for valor in quadro_resultados.winfo_children():
        valor.destroy()
    for item in quadro_calcular.winfo_children():
        item.destroy()
    fis = []
    dados = []
    valores_xi = []
    valores_fi = []






def mostrar_xi():
    limpar_frames()


def mostrar_entrys_discreto():
    limpar_frames()

    txt_xi = CTkLabel(quadro_dados, text="Xi", width=100, height = 20, anchor="w", font=("Arial Bold", 16))
    txt_xi.place(x=145,y=10)

    txt_fi = CTkLabel(quadro_dados, text="fi", width=100, height = 20, anchor="w", font=("Arial Bold", 16))
    txt_fi.place(x=235,y=10)

    btn_calcular = CTkButton(quadro_calcular, text="Calcular", command=lambda:(coletar_dados(), coletar_fis(), calcular_xi()), width=350, height=35, font=("Arial Bold", 16))
    btn_calcular.place(x=20, y=8)

    for i in range(coletar_quantidade()):
        xi = CTkEntry(quadro_dados, width=80, height=35, font=("Arial Bold", 16), border_width=1, corner_radius=0)
        xi.place(x=110, y=(31 * (i+1)) + 5)
        dados.append(xi)

        fi = CTkEntry(quadro_dados, width=80, height=35, font=("Arial Bold", 16), border_width=1, corner_radius=0)
        fi.place(x=200, y= 31 * (i+1) + 5)
        fis.append(fi)
    return dados

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

def calcular_xi():
    valores_xi = coletar_dados()
    valores_fi = coletar_fis()

    N = 0
    S2 = 0
    variancias = []
    soma_Xi_vezes_fi = 0

    for i in range(0, coletar_quantidade()):
        i = i+1
        N += valores_fi[i]
        soma_Xi_vezes_fi += valores_xi[i] * valores_fi[i]
        
    for i in range(0, coletar_quantidade()):
        soma_Xi_vezes_fi = round(soma_Xi_vezes_fi, 2)

    N = round(N, 2)
    media = round(soma_Xi_vezes_fi / N, 2)
    for i in range(0, coletar_quantidade()):
        variancias.append(round((valores_xi[i] - media) ** 2 * valores_fi[i],2))

    for i in variancias:
        S2 += i

    S2 = round(S2/(N-1), 2)
    s = round(sqrt(S2),2)
    cv = round((100 * s) / media, 2)
    x= 150
    
    CTkLabel(quadro_resultados, text=f"Média = {media}", width=100, height = 20, anchor=W, font=("Arial Bold", 16), text_color="black").place(x=x, y=91)
    CTkLabel(quadro_resultados, text=f"Variância = {S2}", width=100, height = 20, anchor=W, font=("Arial Bold", 16), text_color="black").place(x=x,y=111)
    CTkLabel(quadro_resultados, text=f"Desvio Padrão = {s}", width=100, height = 20, anchor=W, font=("Arial Bold", 16), text_color="black").place(x=x,y=131)
    CTkLabel(quadro_resultados, text=f"Coeficiente Padrão = {cv}", width=100, height = 20, anchor=W, font=("Arial Bold", 16), text_color="black").place(x=x,y=151)

def coletar_quantidade():
    return int(entrada_quant_xi.get())

l_x = 50
l_y = 130

txt_quantidade = CTkLabel(estatistica, text="Digite quantos Dados(Xi) a amostra contém", font=("Arial Bold", 18))
txt_quantidade.place(x=l_x, y=l_y)



entrada_quant_xi = CTkEntry(estatistica, width=240, height=25, font=("Arial Bold", 14), border_width=1, corner_radius=0)
entrada_quant_xi.place(x=l_x, y=170) 

titulo = CTkLabel(estatistica, text="Estatística Aplicada", anchor="w", font=("Arial Bold", 32))
titulo.place(anchor="w", y=50, x=85)

orientacao = CTkLabel(estatistica, text= "Agrupamento Discreto", font=("Arial Bold", 18))
orientacao.place(anchor="w", y=85, x=130)

#frames
# quadro_btn_discreto = CTkFrame(estatistica, width=207, height=35, fg_color="#242424")
# quadro_btn_discreto.place(x=18, y=120)

quadro_dados = CTkFrame(estatistica,width=390, height=220, fg_color="#242424")
quadro_dados.place(x=30, y=280)

quadro_resultados = CTkFrame(estatistica,width=450, height=600, fg_color="white")
quadro_resultados.place(x=450, y=0)

quadro_ok = CTkFrame(estatistica, width = 150, height= 35, fg_color="#242424")
quadro_ok.place(x=300, y=165)

quadro_calcular = CTkFrame(estatistica, width=390, height=50, fg_color="#242424")
quadro_calcular.place(x=30, y=520)

#Botões
# btn_discreto = CTkButton(quadro_btn_discreto, text="Agrupamento discreto", command=mostrar_xi, width=200, height=30, font=("Arial Bold", 14))
# btn_discreto.place(x=3, y=2)

btn_ok = CTkButton(quadro_ok, text="OK", width=95, height=28, font=("Arial Bold", 12), command=mostrar_entrys_discreto)
btn_ok.place(x=1,y=3)

estatistica.mainloop()