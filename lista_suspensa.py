from tkinter import *
from tkinter import messagebox

def imprimirEsporte():
    ve = ve_esporte.get()
    if ve == "Futebol":
        print("Esporte Futebol")
    elif ve == "Volei":
        print("Esporte Volei")
    elif ve == "b":
        print("Esporte Basquete")
    else:
        print("Selecione um esporte")
    
def mostrarMsg():
    messagebox.showinfo(title="CBG Cursos", message="CFB Cursos")


estatistica = Tk() #nome do tk(aplicativo, aplicação, janela...)

estatistica.title("Estátistica") #titulo
estatistica.geometry("500x300") #tamanho da janela
estatistica.configure(background="#ADD8E6") #cor de fundo
# def mostrasMsg (tiposmg, msg):

vnum_cstexto = StringVar()

fr_quadro1=Frame(estatistica,borderwidth=1, relief="solid") #borderwidt -> espessura da borda, relief -> tipo da borda (solid, flat, raised, sunken)
fr_quadro1.place(x=0, y=10, width=300, height=100)

Label(estatistica,text="Tipo de cx(1, 2 ou 3)").pack()
tb_num=Entry(estatistica,textvariable = vnum_cstexto)
vnum_cstexto.set("1")
tb_num.pack()

btn_msg=Button(estatistica, text="Mostrar mensagem", command=mostrarMsg)
btn_msg.pack()
# vmsg = ""


listaEsportes = ["Futebol", "Volei", "Basquete"] # lista suspensa

ve_esporte = StringVar()
ve_esporte.set(listaEsportes[0]) #definir valor padrao

bl_esportes = Label(estatistica, text="Esportes")
bl_esportes.pack()

menu_esportes = OptionMenu(estatistica, ve_esporte, *listaEsportes) # o * indica que será utilizado todos os elementos da lista
menu_esportes.pack() #para aparecer

btn_esporte = Button(estatistica, text="Esporte selecionado", command=imprimirEsporte)
btn_esporte.pack()

# txtxi = Label(estatistica, text="Xi", background="#ADD8E6", foreground = "#000", anchor=W).place(x=15,y=10, width=100, height = 20)
# xi1 = Entry(estatistica).place(x=10, y=30, width=30, height=20)
# xi2 = Entry(estatistica).place(x=10, y=50, width=30, height=20)
# xi3 = Entry(estatistica).place(x=10, y=70, width=30, height=20)
# xi4 = Entry(estatistica).place(x=10, y=90, width=30, height=20)
# xi5 = Entry(estatistica).place(x=10, y=110, width=30, height=20)
# txtfi = Label(estatistica, text="fi", background="#ADD8E6", foreground = "#000", anchor=W).place(x=50,y=10, width=100, height = 20)
# fi1 = Entry(estatistica).place(x=45, y=30, width=30, height=20)
# fi2 = Entry(estatistica).place(x=45, y=50, width=30, height=20)
# fi3 = Entry(estatistica).place(x=45, y=70, width=30, height=20)
# fi4 = Entry(estatistica).place(x=45, y=90, width=30, height=20)
# fi5 = Entry(estatistica).place(x=45, y=110, width=30, height=20)



estatistica.mainloop()