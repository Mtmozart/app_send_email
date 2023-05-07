M: int

M = int(input("Quantas linhas vai ter a matriz? "))


matriz: [[int]] = [[0 for x in range(M)] for x in range(M)]

for i in range(0, M):
    for j in range(0, M):
        matriz[i][j] = int(input(f"Elemento[ {i},{j}]:"))

print("Diagonal principal: ")

for i in range(0, M):
    print(f"{matriz[i][i]} ", end="")
print()
soma: int
soma = 0
for i in range(0, M):
    for j in range(0, M):
        if matriz[i][j] < 0:
            soma = soma + 1
print(f"Quantidade de negativo =: {soma}")




