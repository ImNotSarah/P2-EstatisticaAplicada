dic = {}

for i in range(0,10):
    var_nome = f'var{i}'
    dic[var_nome] = f'{i+1}'
    print(dic[f'var{i}'])
print()
print(dic)