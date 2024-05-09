from tkinter import *

estatistica = Tk() #nome do tk(aplicativo, aplicação, janela...)

estatistica.title("Estátistica") #titulo
estatistica.geometry("1920x1080") #tamanho da janela
estatistica.configure(background="#ADD8E6") #cor de fundo

def mostrar_agrupamento_discreto():
    quadro_btn_classes.destroy()
    txtxi = Label(quadro_dados, text="Xi", background="#ADD8E6", foreground = "#000", anchor=W).place(x=15,y=1, width=100, height = 20)
    xi1 = Entry(quadro_dados).place(x=10, y=20, width=30, height=20)
    xi2 = Entry(quadro_dados).place(x=10, y=40, width=30, height=20)
    xi3 = Entry(quadro_dados).place(x=10, y=60, width=30, height=20)
    xi4 = Entry(quadro_dados).place(x=10, y=80, width=30, height=20)
    xi5 = Entry(quadro_dados).place(x=10, y=100, width=30, height=20)
    txtfi = Label(quadro_dados, text="fi", background="#ADD8E6", foreground = "#000", anchor=W).place(x=50,y=1, width=100, height = 20)
    fi1 = Entry(quadro_dados).place(x=45, y=20, width=30, height=20)
    fi2 = Entry(quadro_dados).place(x=45, y=40, width=30, height=20)
    fi3 = Entry(quadro_dados).place(x=45, y=60, width=30, height=20)
    fi4 = Entry(quadro_dados).place(x=45, y=80, width=30, height=20)
    fi5 = Entry(quadro_dados).place(x=45, y=100, width=30, height=20)

    xi1 = xi1.get()
    xi2 = xi2.get()
    xi3 = xi3.get()
    xi4 = xi4.get()
    xi5 = xi5.get()


    lista_dados = [xi1, xi2, xi3, xi4, xi5]
    return lista_dados

def mostrar_agrupamento_classes():
    quadro_btn_discreto.destroy()
    instru_classe = Label(quadro_dados, text="Digite apenas uma classe: ", background="#ADD8E6", foreground = "#000", anchor=W).place(x=10, y= 1, width = 145, height = 20)
    txtclasse = Label(quadro_dados, text="Classes", background="#ADD8E6", foreground = "#000", anchor=W).place(x=10,y=20, width=100, height = 20)
    classe1 = Entry(quadro_dados).place(x=10, y=41, width=30, height=20)
    classe2 = Entry(quadro_dados).place(x=40, y=41, width=30, height=20)

    txtfi = Label(quadro_dados, text="fi", background = "#ADD8E6", foreground = "#000", anchor = W).place(x=80,y=20, width=50, height = 20)
    fi1 = Entry(quadro_dados).place(x=75, y=41, width=30, height=20)
    fi2 = Entry(quadro_dados).place(x=75, y=61, width=30, height=20)
    fi3 = Entry(quadro_dados).place(x=75, y=81, width=30, height=20)
    fi4 = Entry(quadro_dados).place(x=75, y=101, width=30, height=20)
    fi5 = Entry(quadro_dados).place(x=75, y=121, width=30, height=20)

quadro_btn_discreto = Frame(estatistica,borderwidth = 1, relief= "flat")
quadro_btn_discreto.configure(background="#ADD8E6")
quadro_btn_discreto.place(x=10, y=10, width=160, height=30)

quadro_btn_classes = Frame(estatistica,borderwidth = 1, relief= "flat")
quadro_btn_classes.configure(background="#ADD8E6")
quadro_btn_classes.place(x=220, y=10, width=160, height=30)

Button(quadro_btn_discreto, text="Agrupamento discreto", command=mostrar_agrupamento_discreto).place(x=1, y=1, width=150, height=25)

Button(quadro_btn_classes, text="Agrupamento em classes", command=mostrar_agrupamento_classes).place(x=1, y=1, width=150, height=25)

quadro_dados = Frame(estatistica,borderwidth = 1, relief= "flat")
quadro_dados.configure(background="#ADD8E6")
quadro_dados.place(x=10, y=50, width=160, height=200)

def listar():
    print(mostrar_agrupamento_discreto())

Button(estatistica, text="exibir", command=listar).place(x=50, y=230, width=150, height=25)


estatistica.mainloop()