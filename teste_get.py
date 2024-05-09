from tkinter import *

def imprimir_dados():
    lista = [vnome.get(), vfone.get(), vmail.get(),vobs.get("1.0", END)]
    
    print(lista)
estatistica = Tk() #nome do tk(aplicativo, aplicação, janela...)

estatistica.title("Estátistica") #titulo
estatistica.geometry("500x300") #tamanho da janela
estatistica.configure(background="#ADD8E6") #cor de fundo

txt1 = Label(estatistica, text="Nome", background="#ADD8E6", foreground = "#000", anchor=W).place(x=10,y=10, width=100, height = 20) 
#anchor -> alinhamento do texto dentro do label

vnome = Entry(estatistica)
vnome.place(x=10, y=30, width=200, height=20)

txt2 = Label(estatistica, text="Telefone", background="#ADD8E6", foreground = "#000", anchor=W).place(x=10,y=60, width=100, height = 20) 
vfone = Entry(estatistica)
vfone.place(x=10, y=80, width=100, height=20)

txt3 = Label(estatistica, text="E-mail", background="#ADD8E6", foreground = "#000", anchor=W).place(x=10,y=110, width=100, height = 20) 
vmail = Entry(estatistica)
vmail.place(x=10, y=130, width=300, height=20)

txt3 = Label(estatistica, text="OBS", background="#ADD8E6", foreground = "#000", anchor=W).place(x=10,y=160, width=100, height = 20) 
vobs = Text(estatistica)
vobs.place(x=10, y=180, width=300, height=80)


#entry -> caixa de entrada de texto
#text -> caixa maior de entrada de texto (multilinha)

Button(estatistica, text="Imprimir", command=imprimir_dados).place(x=10, y=270, width=100, height=20)


estatistica.mainloop()