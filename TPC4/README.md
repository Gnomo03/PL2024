## TPC4: Analisador Léxico

### Autor
- Nome: David da Silva Teixeira
- ID: A100554

### Requisitos
- Construit um analisador léxico para: SELECT id,nome,salario from empregado where salario >= 820

### Parágrafos
**Definição de Tokens**: Uma lista de padrões de tokens (token_patterns) é definida para capturar os diferentes elementos de uma consulta SQL. Cada padrão consiste numa expressão regular e um tipo de token associado. Os tipos incluem KEYWORD para palavras-chave SQL (SELECT, FROM, WHERE), IDENTIFIER para identificadores (como nomes de colunas e tabelas), OPERATOR para operadores (como >=), NUMBER para números e COMMA para vírgulas.

**Ignorar Espaços em Branco e Comentários**: Os padrões também incluem regras para ignorar espaços em branco e comentários (que começam com --), que não contribuem para a estrutura semântica da consulta.

**Processamento dos Tokens**: A função lex é o coração do analisador léxico. Ela recebe uma string de entrada (a consulta SQL), e itera sobre ela utilizando as expressões regulares definidas para identificar tokens. Quando um token é identificado, ele é adicionado a uma lista de tokens, incluindo o texto do token e seu tipo.

**Gestão de Erros**: Se um caractere não corresponde a nenhum dos padrões definidos, o programa considera isso um erro, exibe uma mensagem de erro indicando o caractere inválido e termina a execução.

**Teste com Consulta SQL**: O programa inclui uma consulta SQL de exemplo (input_string) que é convertida para maiúsculas (para garantir a correspondência com as palavras-chave definidas) e passada para a função lex. Isso demonstra como a string de entrada é analisada em tokens.
