from math import sqrt

quant_xi = input("Digite a quantidade de dados (Xi): ")
quant_xi = int(quant_xi)

N = 0
S2 = 0
Xi = []
fi = []
variancias = []
soma_Xi_vezes_fi = 0

print("Digite os valores correspondentes a cada dado: ")
for i in range(0, quant_xi): #coleta os valroes de Xi
    Xi.append(float(input(f"Xi {i+1}: " )))

print()
print("Digite os valores correspondentes a cada frequencia individual absoluta: ")
for i in range(0, quant_xi):
    fi.append(float(input(f"fi {i+1}: " )))

for i in range(0, quant_xi):
    N += fi[i]
    soma_Xi_vezes_fi += Xi[i] * fi[i]
    
for i in range(0, quant_xi):
    soma_Xi_vezes_fi = round(soma_Xi_vezes_fi, 2)
    N = round(N, 2)
    media = round(soma_Xi_vezes_fi / N, 2)
    variancias.append(round((Xi[i] - media) ** 2 * fi[i],2))

for i in variancias:
    S2 += i

S2 = round(S2/(N-1), 2)
s = round(sqrt(S2),2)
cv = round((100 * s) / media, 2)

print("-=" * 5 ,"Resultados", "=-" * 5)
print("ẋ = ", media)
print("S2 = ", S2)
print("s = ", s)
print("CV = ", cv)
