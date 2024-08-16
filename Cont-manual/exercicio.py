def conta_letra(string, letra):
    count = 0
    for carac in string:
        if letra == carac:
            count+=1
    return count

string = str(input("Digite um texto: "))
letra = str(input("Digite uma letra de parâmetro: "))

print(conta_letra(string, letra))