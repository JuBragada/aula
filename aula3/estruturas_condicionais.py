#Verifique a idade do usuário, se maior de 18 imprimir "indivíduo possui idade mínima para dirigir"

idade_usuario = int(input("Informe a sua idade: "))

if idade_usuario > 18:
    print("Indivíduo possui idade mínima para dirigir")
elif idade_usuario >= 17 and idade_usuario <= 18:
    print("Indivíduo está entre 17 e 18 anos e ainda NÃO está apto para dirigir")
else:
    print("Indivíduo NÃO possui idade mínima para dirigir")