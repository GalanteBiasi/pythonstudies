nome = "Gabriel"
idade = 19
profissao = "Prograamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Gabriel", "idade": 19, "saldo": 45.435}


print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))


print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")