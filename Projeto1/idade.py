nome1: str
idade1: int
nome2: str
idade2: int
media: float


print("Dados da primeira pessoa: ")
nome1 = str(input("Nome:"))
idade1 = int(input("idade: "))
print("Dados da segunda pessoa: ")
nome2 = str(input("Nome:"))
idade2 = int(input("idade: "))

media = (idade1 + idade2)/2

print(f"A média de idade de {nome1} e {nome2} é de {media:.1f}")