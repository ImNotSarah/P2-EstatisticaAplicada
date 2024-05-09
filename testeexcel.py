import openpyxl

print("O exercicio que você quer resolver se trata de Agrupamento Discreto ou Agrupamento em Classes?")

planilha = openpyxl.load_workbook('teste.xlsx')
dados = planilha['Planilha1']

for coluna in dados.iter_rows(min_row=2):
    nome = coluna[0].value
    idade = coluna[1].value
    cidade = coluna[2].value
    print(nome, ' ', idade, ' ', cidade)
    
