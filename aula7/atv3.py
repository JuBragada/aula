from faker import Faker
import pandas as pd



faker = Faker('pt_BR')

#SOLID (S - Princípio da responsabilidade única: a função só cria uma pessoa)

def create_persona(number_of_personas) -> list:
    personas_list = []

    for i in range(number_of_personas):
        data = {
        "nome": faker.name(),
        "cidade": faker.city(),
        "idade": faker.random_int(18, 90)
        }
        personas_list.append(data)
    return personas_list

lista_de_personas = create_persona(20)

df_lista_de_personas = pd.DataFrame(lista_de_personas)

df_lista_de_personas.to_csv('lista_de_personas.csv', index=False)



