import re
import sys
import json
from ply import lex

tokens = ['MOEDA', 'LISTAR', 'SELECIONAR', 'SAIR']

saldo = 0
produtos = []

def t_MOEDA(t):
    r'MOEDA\s+((\d+)(e|c)(,\s*)?)+'
    global saldo
    moedas = re.findall(r'(\d+)(e|c)', t.value)
    for valor, tipo in moedas:
        valor = int(valor)
        if tipo == 'e':
            saldo += valor * 100
        elif tipo == 'c':
            saldo += valor
    print(f"Saldo = {saldo // 100}e{saldo % 100}c")

def t_LISTAR(t):
    r'LISTAR'
    for i, produto in enumerate(produtos, start=1):
        euros = produto['preco'] // 100
        centimos = produto['preco'] % 100
        print(f"{i} - {produto['nome']} - {euros}e{centimos:02d}c - Quantidade: {produto['quantidade']}")


def t_SELECIONAR(t):
    r'SELECIONAR\s+(\d+)'
    global saldo
    produto_id = int(t.value.split()[1]) - 1
    if 0 <= produto_id < len(produtos):
        produto = produtos[produto_id]
        if produto['quantidade'] > 0:
            if saldo >= produto['preco']:
                saldo -= produto['preco']
                produto['quantidade'] -= 1
                print(f"Selecionou {produto['nome']}, saldo = {saldo // 100}e{saldo % 100}c, Restam {produto['quantidade']} unidades.")
            else:
                print("Saldo insuficiente.")
        else:
            print(f"{produto['nome']} esgotado.")
    else:
        print("Produto inválido.")

def t_SAIR(t):
    r'SAIR'
    print(f"Troco = {saldo // 100}e{saldo % 100}c")
    sys.exit()

t_ANY_ignore = ' \t\n'

def t_ANY_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

with open('produtos.json', 'r') as file:
    produtos = json.load(file)

while True:
    try:
        data = input()
        lexer.input(data)
        for tok in lexer:
            pass
    except EOFError:
        break
