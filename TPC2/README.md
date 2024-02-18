## TPC2: Conversor de MD para HTML

### Autor
- Nome: David da Silva Teixeira
- ID: A100554

### Requisitos
- Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" de MarkDown

### Parágrafos
Uma peça chave na conversão de Markdown para HTML é o re.sub, uma técnica chave para realizar substituições de texto baseadas em padrões definidos por expressões regulares. Aqui está um resumo de como *re.sub* é utilizado:

**Cabeçalhos**: A função re.sub é usada para encontrar padrões de cabeçalhos Markdown (indicados por cardinais) e substituí-los pelas respectivas tags de cabeçalho HTML.

**Ênfases**: Transforma texto em negrito e itálico de Markdown para as suas tags HTML equivalentes utilizando re.sub.

**Links**: Converte links em Markdown para a forma HTML (<a href="url">texto</a>) utilizando re.sub.

**Listas**: Apesar do script usar um loop e re.match para identificar itens de lista, ele ainda usa re.sub dentro desse contexto para substituir a sintaxe de itens de lista por tags HTML.

**Código**: Usa re.sub para converter texto entre crases (indicando código inline em Markdown) para a tag "<code>" em HTML. A opção flags=re.DOTALL permite que o padrão corresponda a linhas múltiplas, se necessário.

**Blockquotes**: Substitui citações em Markdown (> citação) por "<blockquote>" em HTML, utilizando re.sub com uma expressão regular que identifica o padrão de citação.

**Regras Horizontais**: Converte linhas horizontais em Markdown (---) para a tag "<hr>" em HTML, utilizando re.sub.

**Parágrafos**: Identifica linhas que não correspondem a outros padrões Markdown e envolve-as em tags de parágrafo "<p>", utilizando re.sub com uma expressão regular negativa para excluir linhas que já foram convertidas em outros elementos HTML.
