import tkinter as tk

def on_spinbox_change():
    value = spinbox.get()
    print("Valor selecionado:", value)

root = tk.Tk()
root.title("Exemplo de Spinbox com Botões Personalizados")
root.geometry("300x200")

# Função para aumentar o valor do Spinbox
def increase_value():
    current_value = int(spinbox.get())
    spinbox.delete(0, "end")
    spinbox.insert(0, current_value + 1)
    on_spinbox_change()

# Função para diminuir o valor do Spinbox
def decrease_value():
    current_value = int(spinbox.get())
    spinbox.delete(0, "end")
    spinbox.insert(0, current_value - 1)
    on_spinbox_change()

spinbox = tk.Entry(root, width=5)  # Usamos Entry em vez de Spinbox
spinbox.pack(side="left", padx=10)

# Botões personalizados
button_increase = tk.Button(root, text="+", command=increase_value, width=2, height=1)
button_increase.pack(side="left", padx=2)

button_decrease = tk.Button(root, text="-", command=decrease_value, width=2, height=1)
button_decrease.pack(side="left", padx=2)

# Função chamada quando o valor do Spinbox é alterado
spinbox.bind("<FocusOut>", lambda event: on_spinbox_change())

root.mainloop()
