
# Etapa 1 

#  If / If-else / elif 


# o que é uma estrutura condicional ? 

# Permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.




# IF 

#-Para criar uma ESTRUTURA CONDICIONAL SIMPLES, é composto por um único desvio, 
# sendo possível utilizar a palavra reservada  IF. 

#Este comando irá testar a expressão lógica, e em caso de retorno verdadeiro as
# ações presentes no bloco de código do IF serão executadas. 

#EXEMPLO : 




saldo = 2000.0
saque = float(input ("Informe o valor do saque"))


if saldo >= saque: 
    print("Realizando saque!")


if saldo < saque:
    print("Saldo insuficiente!")   




# IF / ELSE 

# Para criar uma ESTRUTURA CONDICIONAL, é composto por dois devios. 
# Como sabemos, se a expressão logica testada no IF for True, então 
# o bloco de código do if será executado. Caso contrário o bloco de código
# ELSE será executado.


saldo = 2000.0
saque = float(input ("Informe o valor do saque"))


if saldo >= saque: 
    print("Realizando saque!")
    

else:
    print("Saldo insuficiente")




# ELIF
    
# Há alguns cenários que devemos utilizar mais de dois desvios, para isso podemos utilizar a
# palavra reservada ELIF. O elif é composto por uma nova expressão lógica, que será testada
# e caso retorne True o bloco de código do elif será executada 
# Não existe um número máximo de ELIFS que podemos utilizar, porém evite criar grandes
# estruturas condicionais, pois elas aumentam a complexidade do código.
    



opcao = int(input("Informe uma opção: [1]Sacar \n[2] Extrato:"))


if opcao == 1: 
    valor = float(input ("Informa a quantia para o saque"))
    #  ...
elif opcao ==2:
    print("Exibindo o extrato...")
else: 
    SystemExit("Opção inválida")



# ====================================================================================
    
