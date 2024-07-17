pergunta = print("Qual das operações você quer calcular?")
funcao = str(input("(+) (*) (-) (/) (√2) (^): "))
primeiro_numero = float(input("Qual o primeiro número do cálculo? "))
segundo_numero = float(input("Qual o segundo número do cálculo? "))

match funcao:
    case "+":
        print(primeiro_numero + segundo_numero)
    case "*":
        print(primeiro_numero * segundo_numero)
    case "-":
        print(primeiro_numero - segundo_numero)
    case "/":
        print(primeiro_numero / segundo_numero)
    case "√2":
        print(primeiro_numero  **(1/segundo_numero))
    case "^":
        print(primeiro_numero ** segundo_numero)
    case _:
        print("Essa operação não é válida")