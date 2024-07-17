print("Bem vindo a calculadora de vogais da Squad 4!")
palavra = str(input("Qual a palavra que você quer contar as vogais: "))

contador = 0 
vogais = "AEIOUaeiou"
for caracter in palavra:
    if caracter in vogais:
        contador += 1

print(f"O número de vogais na palavra é {contador}")