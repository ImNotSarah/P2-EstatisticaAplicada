from customtkinter import CTk
from tkinter import Spinbox

app = CTk()
app.title("Exemplo de Spinbox")
app.geometry("300x200")

def on_spinbox_change(value):
    print("Valor selecionado:", value)


entrada_quant_xi = Spinbox(app, values=(0,1,2,3,4,5), command=on_spinbox_change, borderwidth= 2, background="#242424", highlightbackground="#565B5E", highlightcolor="#565B5E", highlightthickness=2, foreground="#FFFFFF") #aqui
entrada_quant_xi.pack(pady=20) #e aqui

app.mainloop()
