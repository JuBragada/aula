import requests as res

integrantes = {
    "integrante_1" : {
        "nome" : "Julia",
        "cep" : "05835003"
    },
    "integrante_2" : {
        "nome" : "Raphael",
        "cep" : "06335300"
    },
    "integrante_3" : {
        "nome" : "Laura",
        "cep" : "06709300"

    }

}

def consuta_cep (cep):
    response  = res.get(f"https://viacep.com.br/ws/{cep}/json/")
    if (response.status_code == 200):
        data = response.json()
        return data["localidade"]
    else:
       return {
          "erro": f"Erro na execução: {response.status_code}",
             "status_codes": {
                    "1xx": "Informativo: Informação recebida e processamento continua.",
                    "3xx": "Redirecionamento: Ação adicional necessária para completar a requisição.",
                    "4xx": "Erro do Cliente: Requisição possui erro ou não pode ser completada.",
                    "5xx": "Erro do Servidor: Servidor encontrou um erro ao tentar completar a requisição."
                }
            }

def exibir(integrantes):
    for chave, valor in integrantes.items():
        nome = valor["nome"]
        cidade = consuta_cep(valor["cep"])
        print(f"Nome: {nome}, cidade: {cidade}")
        