nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade < 16:
    print(f"{nome} voce não está apto a votar")
else:
    print(f"{nome} voce está apto a votar")