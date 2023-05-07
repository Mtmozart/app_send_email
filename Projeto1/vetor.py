M: int
i: int
M = int(input("Quantos números vocÊ vai digitar: "))
vetor: [float] = [0 for x in range(M)]

for i in range(0, M):
    vetor[i] = float(input("Digite um numero: "))
print()
print("Valores = ", end="")
for i in range(0, M):
    print(f"{vetor[i]:.1f}", end=" ")

print()
soma: float
soma = 0
for i in range(0, M):
    soma = soma + vetor[i]

print(f"Soma = {soma:.2f}")

media: float
media = soma/M
print(f"Media = {media:.2f}")



