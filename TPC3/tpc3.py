import re

def somar_numeros(texto):
    soma = 0
    # num_read = 0
    continuar = False

    for palavra in texto.split():
        if palavra.lower() == "on":
            continuar = True
        elif palavra.lower() == "off":
            continuar = False
        elif palavra == "=":
            #if continuar or soma > 0: 
            print(soma)
            # print(str(num_read) + " Números lidos")
        elif continuar:
            numeros = re.findall(r'\b\d+\b', palavra)
            soma += sum(map(int, numeros))
            # num_read += 1

# Exemplo de uso
texto = "oN 1 + 2 = 3 oFf 45 99 ON 7 + 3 = OfF 10 = 16"
somar_numeros(texto)
 