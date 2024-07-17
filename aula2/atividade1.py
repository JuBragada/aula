"""
Fazer um programa que some 4 notas e, no final, tenha a média aritmética dessas notas
"""
nome_usuario = str(input("Informe seu nome: "))
n1 = float(input("Informe a sua n1: "))
n2 = float(input("Informe sua n2: "))
n3 = float(input("Informe sua n3: "))
n4 = float(input("Informe sua n4: "))
media = (n1 + n2 + n3 + n4) / 4

print(f"Olá, {nome_usuario}, sua média é de {media:.2f}")
