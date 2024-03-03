import sys
import re

# Definição dos padrões de tokens
token_patterns = [
    (r'[ \t\n]+',               None),   # Espaços em branco
    (r'--.*',                   None),   # Comentários
    (r'SELECT|FROM|WHERE',      'KEYWORD'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
    (r'>=',                     'OPERATOR'),
    (r'\d+',                    'NUMBER'),
    (r',',                      'COMMA')
]

def lex(characters):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_pattern in token_patterns:
            pattern, tag = token_pattern
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = {'text': text, 'type': tag}
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write(f'Illegal character: {characters[pos]}\n')
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens

input_string = "select id, nome, salario from empregado where salario >= 820"
tokens = lex(input_string.upper())
print(tokens)
