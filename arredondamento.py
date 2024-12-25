
# Função para ajustar o módulo round, para que ele  ##
# Arredonde inteiros a partir de 0.5 (em vez de 0.6)##
# O método sempre arredonda para duas casa decímais ##

def arredonde(num):
    mili = int(((num - int(num)) * 10000) % 10)
    cent = int(((num - int(num)) * 1000) % 10)

    if cent > 4 and mili < 8:
        num = num + 0.0011
    elif cent > 4:
        num = num + 0.001
    num = round(num, 2)

    return num
