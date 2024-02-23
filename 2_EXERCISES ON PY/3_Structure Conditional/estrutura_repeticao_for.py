
#       COMANDO FOR 

#   É utilizado para percorrer um objeto iterável. Faz sentido usar "for" 
#   quando sabemos o número exato de vezes que nosso bloco de código deve ser executado,
#   ou quando queremos percorrer um objeto iterável.




#texto = input("Informe um texto:")
texto= " "
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável

for letra in texto:
    if letra.upper() in VOGAIS:
      print(letra, end=" ")
else:      
    print()  # adiciona uma quebra de linha     
    print("Executa no final do laço")



# exemplo utilizando a função built-in range

    for numero in range(0, 51, 5):
       print(numero, end=" ")



print()
print()

