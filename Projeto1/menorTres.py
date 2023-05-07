a = int(input("Digite o primeiro valor "))
b = int(input("Digite o segundo valor "))
c = int(input("Digite o terceiro valor "))

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

print(f"O menor número é:  {menor}")