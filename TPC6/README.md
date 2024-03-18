## TPC6: Calculadora LL(1)

### Autor
- Nome: David da Silva Teixeira
- ID: A100554

### Requisitos
- Criar uma calculadora que suporte operações básicas de aritmética. 
- O parser deve ser inplementado seguindo a abordagem LL(1).

### Parágrafos
**Armazenamento de Variáveis**: Utiliza um dicionário `vars` para armazenar os valores das variáveis, permitindo que expressões futuras façam referência a esses valores.

**Definição e Uso de Variáveis**:
   - O código permite definir variáveis através de expressões de atribuição (e.g., `a = 1 + 2`).
   - Variáveis não definidas são tratadas como tendo valor 0 por padrão.
   - Implementa a funcionalidade de solicitar ao utilizador o valor de uma variável não inicializada através do símbolo `?`.

**Avaliação de Expressões**: Expressões são avaliadas assim que são analisadas, o que permite a execução de cálculos em tempo real durante o parsing.

**Exibição de Resultados**: Utiliza o símbolo `!` para indicar que o resultado da expressão seguinte deve ser exibido na tela.
