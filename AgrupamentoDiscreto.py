from customtkinter import *
from math import sqrt

estatistica = CTk()  # Nome do tk (aplicativo, aplicação, janela...)
estatistica.title("Estátistica")  # Título
estatistica.geometry("900x600")  # Tamanho da janela

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
    global fis, dados, valores_xi, valores_fi
    fis = []
    dados = []
    valores_xi = []
    valores_fi = []

def mostrar_xi():
    limpar_frames()

def mostrar_entrys_discreto():
    limpar_frames()

    quadro_dados.place(x=125, y=235)

    txt_xi = CTkLabel(quadro_dados, text="Xi", font=("Arial Bold", 16))
    txt_xi.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

    txt_fi = CTkLabel(quadro_dados, text="fi", font=("Arial Bold", 16))
    txt_fi.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

    btn_calcular = CTkButton(quadro_calcular, text="Calcular", command=lambda:(coletar_dados(), coletar_fis(), calcular_xi()), width=350, height=35, font=("Arial Bold", 16))
    btn_calcular.place(x=20, y=8)

    for i in range(coletar_quantidade()):
        xi = CTkEntry(quadro_dados, width=80, height=35, font=("Arial Bold", 14), border_width=1, corner_radius=0)
        xi.grid(row=i+1, column=0, padx=5, pady=0, sticky='ew')
        dados.append(xi)

        fi = CTkEntry(quadro_dados, width=80, height=35, font=("Arial Bold", 14), border_width=1, corner_radius=0)
        fi.grid(row=i+1, column=1, padx=5, pady=0, sticky='ew')
        fis.append(fi)

    return dados

def coletar_dados():
    valores_xi.clear()
    for entry in dados:
        valor = entry.get()
        valores_xi.append(float(valor))
    return valores_xi

def coletar_fis():
    valores_fi.clear()
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

    for i in range(coletar_quantidade()):
        N += valores_fi[i]
        soma_Xi_vezes_fi += valores_xi[i] * valores_fi[i]

    for i in range(coletar_quantidade()):
        soma_Xi_vezes_fi = round(soma_Xi_vezes_fi, 2)

    N = round(N, 2)
    media = round(soma_Xi_vezes_fi / N, 2)
    for i in range(coletar_quantidade()):
        variancias.append(round((valores_xi[i] - media) ** 2 * valores_fi[i], 2))

    for i in variancias:
        S2 += i

    S2 = round(S2 / (N - 1), 2)
    s = round(sqrt(S2), 2)
    cv = round((100 * s) / media, 2)
    x = 150

    
    resultados = CTkLabel(quadro_resultados, text="Resultados", anchor="w", font=("Arial Bold", 32), text_color="#242424")
    resultados.place(y=30, x=150)

    medidas = CTkLabel(quadro_resultados, text="Medidas de Dispersão", font=("Arial Bold", 18), text_color="#242424")
    medidas.place(anchor="w", y=80, x=135)

    #quadros

    quadro_n = CTkFrame(quadro_resultados, width=340, height=70, fg_color="#1F6AA5", corner_radius= 15)
    quadro_n.place(x=55, y=130)

    quadro_media = CTkFrame(quadro_resultados, width=340, height=70, fg_color="#1F6AA5", corner_radius= 15)
    quadro_media.place(x=55, y=220)

    quadro_variancia = CTkFrame(quadro_resultados, width=340, height=70, fg_color="#1F6AA5", corner_radius= 15)
    quadro_variancia.place(x=55, y=310)

    quadro_desvio_padrao = CTkFrame(quadro_resultados,width=340, height=70, fg_color="#1F6AA5", corner_radius= 15)
    quadro_desvio_padrao.place(x=55, y=400)

    quadro_coeficiente_padrao = CTkFrame(quadro_resultados, width=340, height=70, fg_color="#1F6AA5", corner_radius= 15)
    quadro_coeficiente_padrao.place(x=55, y=490)

    #Resultados

    valor_n = CTkLabel(quadro_n, text=f"{N:.2f}", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")
    valor_n.place(x=260, y=30)

    valor_media = CTkLabel(quadro_media, text=f"{media:.2f}", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")
    valor_media.place(x=260, y=30)

    valor_variancia = CTkLabel(quadro_variancia, text=f"{S2:.2f}", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")
    valor_variancia.place(x=260, y=30)

    valor_desvio_padrao = CTkLabel(quadro_desvio_padrao, text=f"{s:.2f}", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")
    valor_desvio_padrao.place(x=260, y=30)

    valor_coeficiente_padrao = CTkLabel(quadro_coeficiente_padrao, text=f"{cv:.2f}%", width=70, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")
    valor_coeficiente_padrao.place(x=260, y=30)

    #Textos

    txt_N = CTkLabel(quadro_n, text="N", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")
    txt_N.place(x=15, y=10)

    txt_media = CTkLabel(quadro_media, text="Média", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")
    txt_media.place(x=15, y=10)

    txt_variacia = CTkLabel(quadro_variancia, text="Variância", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")
    txt_variacia.place(x=15, y=10)

    txt_desvio_padrao = CTkLabel(quadro_desvio_padrao, text="Desvio Padrão", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")
    txt_desvio_padrao.place(x=15, y=10)

    txt_coeficiente_padrao = CTkLabel(quadro_coeficiente_padrao, text="Coeficiênte Padrão", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")
    txt_coeficiente_padrao.place(x=15, y=10)

def coletar_quantidade():
    return int(entrada_quant_xi.get())

l_x = 50
l_y = 130

titulo = CTkLabel(estatistica, text="Estatística Aplicada", anchor="w", font=("Arial Bold", 32))
titulo.place(anchor="w", y=50, x=85)

orientacao = CTkLabel(estatistica, text="Agrupamento Discreto", font=("Arial Bold", 18))
orientacao.place(anchor="w", y=85, x=130)

txt_quantidade = CTkLabel(estatistica, text="Digite quantos Dados(Xi) a amostra contém", font=("Arial Bold", 18))
txt_quantidade.place(x=l_x, y=l_y)

entrada_quant_xi = CTkEntry(estatistica, width=240, height=25, font=("Arial Bold", 14), border_width=1, corner_radius=0)
entrada_quant_xi.place(x=l_x, y=170)

quadro_ok = CTkFrame(estatistica, width=150, height=35, fg_color="#242424")
quadro_ok.place(x=300, y=165)

quadro_dados = CTkScrollableFrame(estatistica, width=185, height=240, fg_color="#242424")

quadro_resultados = CTkFrame(estatistica, width=450, height=600, fg_color="#F9F9FA", corner_radius=0)
quadro_resultados.place(x=450, y=0)

quadro_calcular = CTkFrame(estatistica, width=390, height=50, fg_color="#242424")
quadro_calcular.place(x=30, y=520)

btn_ok = CTkButton(quadro_ok, text="OK", width=95, height=28, font=("Arial Bold", 12), command=mostrar_entrys_discreto)
btn_ok.place(x=1, y=3)

estatistica.mainloop()
