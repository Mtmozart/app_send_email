import math
area: float
base: float
altura: float
diagonal: float
perimentro: float

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = base * altura
perimetro = (base * 2 ) + (altura * 2)
diagonal = math.sqrt(math.pow(base, 2) + math.pow(altura, 2))

print(f"A area do retângulo é : {area:.4f}")
print(f"A diagonal do retângulo é : {diagonal:.4f}")
print(f"O perimetro do retângulo é : {perimetro:.4f}")