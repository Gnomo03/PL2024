import re

def somar_numeros(texto):
    soma = 0
    continuar = True  # Inicia com a soma ativada

    # Processa cada segmento do texto
    for segmento in re.finditer(r'\d+|[a-zA-Z]+|=', texto):
        texto_segmento = segmento.group()

        # Verifica se o segmento contém 'on' ou 'off'
        if 'on' in texto_segmento.lower():
            continuar = True
        elif 'off' in texto_segmento.lower():
            continuar = False

        # Se estiver somando, adiciona qualquer número encontrado ao total
        if continuar and texto_segmento.isdigit():
            soma += int(texto_segmento)

        # Ao encontrar '=', imprime a soma atual e a reseta
        if texto_segmento == '=':
            print(soma)

# Exemplo de uso
texto = "Ontem fez um fr10 = á 12 an05 atroff ="
somar_numeros(texto)
