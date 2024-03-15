## TPC5: Vending Machine

### Autor
- Nome: David da Silva Teixeira
- ID: A100554

### Requisitos
- Criar um analisador léxico de uma máquina de vendas que aceite os seguintes tokens: MOEDA, LISTAR, SELECIONAR, SAIR
- Ao detetar o token MOEDA, o programa lê os próximos argumentos e adiciona-os ao saldo do utilizador, por exemplo: "MOEDA 1e,20c" daria Saldo = 1e20c (1 euro e 20 cêntimos)
- Ao detetar o token LISTAR, o programa lista o id, nome e preço de todos os produtos associados á máquina
- Ao detetar o token SELECIONAR o programa lê o próximo argumento (que deve ser um número) e seleciona o produto com esse id, retirando o preço ao saldo do utilizador
- Ao detetar o token SAIR o programa termina, imprimindo o troco

### Parágrafos
**Definição de Tokens**: Os tokens MOEDA, LISTAR, SELECIONAR e SAIR representam as ações que o utilizador pode realizar. Estes são identificados por expressões regulares específicas, que permitem ao analisador léxico reconhecer os comandos de entrada.

**Manipulação do Saldo**: A função t_MOEDA atualiza o saldo global com base nas moedas inseridas. As moedas podem ser especificadas em euros (e) e centimos (c), e o saldo é mantido em centimos para simplificar os cálculos.

**Listagem de Produtos**: A função t_LISTAR itera sobre a lista global de produtos, exibindo cada um com seu preço e quantidade. Os produtos são carregados a partir de um arquivo JSON, o que facilita a modificação e adição de novos itens sem alterar o código.

**Seleção de Produtos**: t_SELECIONAR permite ao utilizador escolher um produto pelo seu índice na lista. Verifica se o saldo é suficiente e, em caso afirmativo, deduz o preço do saldo e informa o usuário da compra bem-sucedida e quantidades restantes.

**Saída e Troco**: t_SAIR exibe o troco devido ao utilizador e encerra o programa. O troco é calculado com base no saldo restante.

**Gestão de Erros**: A função t_ANY_error lida com caracteres inválidos, informando o usuário e ignorando o caractere problemático.

**Estrutura de Loop Principal**: O programa executa em um loop infinito, lendo comandos do utilizador até que o comando SAIR seja recebido.
