

            # Objetivo Geral 


# Aprender como realizar uma identação do código para delimitar os blocos de comandos. 


# Oque é identar ? 


# Identar código é uma forma de manter o código fonte mais legível e manutenivel, entretanto em Python, ela exerce um segundo papel,
# atráves da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.


def sacar(valor): 
    saldo = 500 


    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")


    print("Obrigado por ser nosso cliente, tenha um bom dia!")    

    
def depositar(valor):
    saldo = 500
    saldo += valor



sacar(100)

#=====================================================================================================================================================================

