valor_compra = float(input("Informe o valor da sua compra para verificar elegibilidade para desconto: "))


if valor_compra >= 250 and valor_compra <= 500:
    desconto_10 = valor_compra*(10/100)
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")
    print(f"O SEU DESCONTO É DE {desconto_10:.2f} REAIS")
    print(f"A SUA COMPRA FICA NO VALOR DE {valor_compra - desconto_10} ")
elif valor_compra > 500:
    desconto_30 = valor_compra*(30/100)
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")
    print(f"O SEU DESCONTO É DE {desconto_30:.2f} REAIS")
    print(f"A SUA COMPRA FICA NO VALOR DE {valor_compra - desconto_30} ")
else:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")