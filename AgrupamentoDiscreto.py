from customtkinter import *
from math import sqrt

estatistica = CTk()  # Nome do tk (aplicativo, aplicação, janela...)
estatistica.title("Estátistica")  # Título
estatistica.geometry("900x600")  # Tamanho da janela

set_appearance_mode("dark") #Tema da janela (escuro)

fis = []
dados = []
valores_xi = []
valores_fi = []

def coletar_quantidade():
    return int(entrada_quant_xi.get())

def limpar_frames(): #Limpa elementos que estão dentro de um frame
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

def mostrar_entrys_discreto(): #Exibe os elementos referente ao Agrupamento Discreto
    limpar_frames()

    quadro_dados.place(x=125, y=235)

    #Textos Xi e fi (CTkLabel)
    txt_xi = CTkLabel(quadro_dados, text="Xi", font=("Arial Bold", 16))
    txt_xi.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

    txt_fi = CTkLabel(quadro_dados, text="fi", font=("Arial Bold", 16))
    txt_fi.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

    #Botão Calcular (CTkButton)
    btn_calcular = CTkButton(quadro_calcular, text="Calcular", command=lambda:(coletar_dados(), coletar_fis(), realizar_calculos()), width=350, height=35, font=("Arial Bold", 16))
    btn_calcular.place(x=20, y=8)

    #Exibe as caixas de entrada de texto (Xi e fi)
    for i in range(coletar_quantidade()):
        xi = CTkEntry(quadro_dados, width=80, height=35, font=("Arial Bold", 14), border_width=1, corner_radius=0)
        xi.grid(row=i+1, column=0, padx=5, pady=0, sticky='ew')
        dados.append(xi)

        fi = CTkEntry(quadro_dados, width=80, height=35, font=("Arial Bold", 14), border_width=1, corner_radius=0)
        fi.grid(row=i+1, column=1, padx=5, pady=0, sticky='ew')
        fis.append(fi)

    return dados

def coletar_dados(): #Coleta os valores de Xi
    valores_xi.clear()
    for entry in dados:
        valor = entry.get()
        valores_xi.append(float(valor))
    return valores_xi

def coletar_fis(): #Coleta os valores de FI
    valores_fi.clear()
    for entry in fis:
        valor = entry.get()
        valores_fi.append(float(valor))
    return valores_fi

def realizar_calculos():
    valores_xi = coletar_dados()
    valores_fi = coletar_fis()

    N = 0
    S2 = 0
    variancias = []
    soma_Xi_vezes_fi = 0

    #Multiplica os valores de Xi pelo seu fi correspondente
    #E realiza a soma dos resultados
    for i in range(coletar_quantidade()):
        N += valores_fi[i]
        soma_Xi_vezes_fi += valores_xi[i] * valores_fi[i]

    media = round(soma_Xi_vezes_fi / N, 2)

    #Realiza o calculo da variancia em cada dado
    for i in range(coletar_quantidade()):
        variancias.append(round((valores_xi[i] - media) ** 2 * valores_fi[i], 2))

    #Soma a variancia de cada dado
    for i in variancias:
        S2 += i

    S2 = round(S2 / (N - 1), 2)
    s = round(sqrt(S2), 2)
    cv = round((100 * s) / media, 2)

    #Exibe titulo "Resultados" (CTkLabel)
    resultados.place(y=30, x=150)
    medidas.place(anchor="w", y=80, x=135)

    #"Exibe" os quadros dos resultados (CTkFrame)
    quadro_n.place(x=55, y=130)
    quadro_media.place(x=55, y=220)
    quadro_variancia.place(x=55, y=310)
    quadro_desvio_padrao.place(x=55, y=400)
    quadro_coeficiente_padrao.place(x=55, y=490)

    #Exibi resultados dos calculos (CTkLabel)
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

    #Exibe textos dos resultados (CTkLabel)
    txt_N.place(x=15, y=10)
    txt_media.place(x=15, y=10)
    txt_variacia.place(x=15, y=10)
    txt_desvio_padrao.place(x=15, y=10)
    txt_coeficiente_padrao.place(x=15, y=10)

#Quadros (CTkFrame)
quadro_ok = CTkFrame(estatistica, width=150, height=35, fg_color="#242424")
quadro_ok.place(x=300, y=165)

quadro_calcular = CTkFrame(estatistica, width=390, height=50, fg_color="#242424")
quadro_calcular.place(x=30, y=520)

quadro_resultados = CTkFrame(estatistica, width=450, height=600, fg_color="#F9F9FA", corner_radius=0)
quadro_resultados.place(x=450, y=0)

quadro_n = CTkFrame(quadro_resultados, width=340, height=70, fg_color="#1F6AA5", corner_radius= 15)
quadro_media = CTkFrame(quadro_resultados, width=340, height=70, fg_color="#1F6AA5", corner_radius= 15)
quadro_variancia = CTkFrame(quadro_resultados, width=340, height=70, fg_color="#1F6AA5", corner_radius= 15)
quadro_desvio_padrao = CTkFrame(quadro_resultados,width=340, height=70, fg_color="#1F6AA5", corner_radius= 15)
quadro_coeficiente_padrao = CTkFrame(quadro_resultados, width=340, height=70, fg_color="#1F6AA5", corner_radius= 15)

#Quadro com barra de rolagem (CTkScrollableFrame)
quadro_dados = CTkScrollableFrame(estatistica, width=185, height=240, fg_color="#242424")

#Textos/Titulos da "tela" principal (CTkLabel)
titulo = CTkLabel(estatistica, text="Estatística Aplicada", anchor="w", font=("Arial Bold", 32))
titulo.place(anchor="w", y=50, x=85)

tema = CTkLabel(estatistica, text="Agrupamento Discreto", font=("Arial Bold", 18))
tema.place(anchor="w", y=85, x=130)

txt_quantidade = CTkLabel(estatistica, text="Digite quantos Dados(Xi) a amostra contém", font=("Arial Bold", 18))
txt_quantidade.place(x=50, y=130)

#Caixa de entrada de texto para a o tamanho da amostra (CTkEntry)
entrada_quant_xi = CTkEntry(estatistica, width=240, height=25, font=("Arial Bold", 14), border_width=1, corner_radius=0)
entrada_quant_xi.place(x=50, y=170)

#Botão OK (CTkButton)
btn_ok = CTkButton(quadro_ok, text="OK", width=95, height=28, font=("Arial Bold", 12), command=mostrar_entrys_discreto)
btn_ok.place(x=1, y=3)

#Textos/Titulos da "tela" branca (CTkLabel)
resultados = CTkLabel(quadro_resultados, text="Resultados", anchor="w", font=("Arial Bold", 32), text_color="#242424")
medidas = CTkLabel(quadro_resultados, text="Medidas de Dispersão", font=("Arial Bold", 18), text_color="#242424")

#Textos dos resultados (CTkLabel)
txt_N = CTkLabel(quadro_n, text="N", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")

txt_media = CTkLabel(quadro_media, text="Média", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")

txt_variacia = CTkLabel(quadro_variancia, text="Variância", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")

txt_desvio_padrao = CTkLabel(quadro_desvio_padrao, text="Desvio Padrão", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")

txt_coeficiente_padrao = CTkLabel(quadro_coeficiente_padrao, text="Coeficiênte Padrão", width=100, height=20, anchor=W, font=("Arial Bold", 22), text_color="white")

estatistica.mainloop()