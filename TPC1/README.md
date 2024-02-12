## TPC1: Análise de um dataset

### Autor
- Nome: David da Silva Teixeira
- ID: A100554

### Regras
- Proibido usar o módulo CSV;

### Requisitos
- Ler o dataset, processá-lo e criar os seguintes resultados:
    - Lista ordenada alfabeticamente das modalidades desportivas;
    - Percentagens de atletas aptos e inaptos para a prática desportiva;
    - Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...

### Parágrafos
- #### Leitura e Processamento do Dataset:
	- O código lê o arquivo 'emd.csv' linha por linha, ignorando a primeira linha que é assumida ser o cabeçalho.
	- Cada linha é dividida em campos separados por vírgulas, e esses campos são passados para o construtor da classe Pessoa, criando um objeto Pessoa para cada linha do arquivo.
	- Todos os objetos Pessoa são armazenados numa lista chamada pessoas, facilitando o acesso e a manipulação dos dados.
- #### Listagem das Modalidades Desportivas:
    - A função "listar_modalidades" extrai todas as modalidades distintas dos objetos Pessoa, ordena-as alfabeticamente utilizando o método sorted e imprime-as. Isto é feito ao criar um conjunto para garantir a unicidade e em seguida, converter esse conjunto numa lista ordenada.
- #### Cálculo das Percentagens de Atletas Aptos e Inaptos:
    - A função "percentagem_aptidao" calcula a percentagem de atletas aptos e inaptos usando uma compreensão de lista para somar todos os atletas com resultado igual a "apto". A percentagem de inaptos é calculada subtraindo a porcentagem de aptos de 100%.
- #### Distribuição de Atletas por Escalão Etário:
    - Utiliza a função "distribuicao_por_idade" e a classe "Counter" para contar quantos atletas caem em cada escalão etário, definido em intervalos de 5 anos. Isto é feito calculando a idade base do escalão (arredondando para baixo para o múltiplo de 5 mais próximo) para cada atleta e, em seguida, contando quantas vezes cada escalão ocorre.
- #### Interface de Menu Interativa:
    -  O código implementa um menu de texto interativo que permite ao utilizador escolher entre listar as modalidades desportivas, mostrar as percentagens de atletas aptos e inaptos, e visualizar a distribuição de atletas por escalão etário, melhorando a interatividade e usabilidade do programa.
