# idade = 26
# idade_str = '26'
#
# nome = input("Digite o seu nome: ")
#
# print(nome)

# lista_compras = ["maça", "chocolate", "carne"]
#
# lista_compras.append("doce de leite")

# print(lista_compras)

#
# lista_doces = []
#
# lista_doces.append(input("Insira o doce para a sua lista:"))
# lista_doces.append(input("Insira o doce para a sua lista:"))
# lista_doces.append(input("Insira o doce para a sua lista:"))
# lista_doces.append(input("Insira o doce para a sua lista:"))
# lista_doces.append(input("Insira o doce para a sua lista:"))

# print(lista_doces)

# Dicionários
#
# ficha_cadastral = {
#     'Nome':'Maça',
#     'Tipo': 'Fruta',
#     'Endereço': 'km18'
# }

# print(ficha_cadastral)
#
# ficha_cadastral.update(
#     {
#     'Telefone':input("Insira o telefone")
#     }
# )
#
# print(ficha_cadastral.get('Nome'))

cadastro_gato = [{
    'Nome':input("Insira o nome do gatinho: "),
    'Idade':input("insira a idade do gatinho: "),
    'Raça': input("Insita a raça do gatinho: ")
    }
    ]

cadastro_gato.append(  {
    'Nome':input("Insira o nome do gatinho: "),
    'Idade':input("insira a idade do gatinho: "),
    'Raça': input("Insita a raça do gatinho: ")
}
)
print(cadastro_gato)

gato_search = input('Procure um gato na base de dados: ')


gato_encontrado = False

for item in cadastro_gato:
    if item.get('Nome') == gato_search:
        gato_encontrado = True
        print(item)

if not gato_encontrado:
    print('Gato não encontrado')
#olá
