print("Digite dois números: ")
a = int(input())
b = int(input())

while a != b:
    if a > b:
        print("Crescente")
    else:
        print("Descrecente")
    print("Digite outros dois números: ")
    a = int(input())
    b = int(input())

print("Fim da execução")

