## TPC3: Somador on/off

### Autor
- Nome: David da Silva Teixeira
- ID: A100554

### Requisitos
- Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
- Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
- Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
- Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

### Parágrafos

**Inicialização de Variáveis**: A função começa com a inicialização de variáveis para a soma total e uma variável booleana continuar para controlar se a soma deve continuar ou ser pausada.

**Processamento de Segmentos**: A função utiliza expressões regulares para iterar por segmentos da string fornecida, identificando números e palavras.

**Controlo do Fluxo**: Dentro do loop, a função verifica se o segmento atual contém as palavras-chave 'on' ou 'off', ajustando a variável continuar para controlar se os números encontrados devem ser somados.

**Soma de Números**: Quando a variável continuar está definida como verdadeira e um segmento contém um número, esse número é adicionado à soma total.

**Finalização e Impressão**: Ao encontrar um sinal de igual ('='), a função imprime o total acumulado da soma e o processo pode ser reiniciado ou finalizado.
