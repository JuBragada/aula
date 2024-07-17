#Fazer importação específica de dados
#Biblioteca random gera valores aleatórios

from faker import Faker
import random



faker = Faker('pt_BR')

print(faker.name())

persona = {
"nome": faker.name(),
"cidade": faker.city(),
"data": faker.date_of_birth(),
"idade": faker.random_int(min=18,max=60) #pode ter número mínimo e máximo, é só colocar (x, x)
}

print(persona)