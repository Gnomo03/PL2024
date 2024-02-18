import re
import sys

blockquote_pattern = r'(?:^> (.*(?:\n(?!^> ).*)*))'

def markdown_to_html(markdown):
    converted_lines = []
    current_list_type = None
    in_paragraph = False

    # Cabeçalhos
    markdown = re.sub(r'###### (.*)', r'<h6>\1</h6>', markdown)
    markdown = re.sub(r'##### (.*)', r'<h5>\1</h5>', markdown)
    markdown = re.sub(r'#### (.*)', r'<h4>\1</h4>', markdown)
    markdown = re.sub(r'### (.*)', r'<h3>\1</h3>', markdown)
    markdown = re.sub(r'## (.*)', r'<h2>\1</h2>', markdown)
    markdown = re.sub(r'# (.*)', r'<h1>\1</h1>', markdown)

    # Ênfases
    markdown = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', markdown)
    markdown = re.sub(r'__(.*)__', r'<strong>\1</strong>', markdown)
    markdown = re.sub(r'\*(.*)\*', r'<em>\1</em>', markdown)
    markdown = re.sub(r'_(.*)_', r'<em>\1</em>', markdown)

    # Links
    markdown = re.sub(r'\[([^\[]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', markdown)

    # Listas
    for line in markdown.split('\n'):
        if re.match(r'^\d+\.\s+(.+)', line): #Lista Ordenada
            if current_list_type != "ol":
                if current_list_type:
                    converted_lines.append(f'</{current_list_type}>')
                converted_lines.append('<ol>')
                current_list_type = "ol"
            converted_lines.append(re.sub(r'^\d+\.\s+(.+)', r'<li>\1</li>', line))
        elif re.match(r'^-\s+(.+)', line):  # Lista Não Ordenada
            if current_list_type != "ul":
                if current_list_type: 
                    converted_lines.append(f'</{current_list_type}>')
                converted_lines.append('<ul>') 
                current_list_type = "ul"
            converted_lines.append(re.sub(r'^-\s+(.+)', r'<li>\1</li>', line))
        else: 
            if current_list_type:
                converted_lines.append(f'</{current_list_type}>')
                current_list_type = None
            converted_lines.append(line)
    if current_list_type:
        converted_lines.append(f'</{current_list_type}>')
    markdown = '\n'.join(converted_lines)

    #Código
    markdown = re.sub(r'`(.*?)`', r'<code>\1</code>', markdown, flags=re.DOTALL)

    # Blockquotes
    markdown = re.sub(re.compile(r'(?<!.)>\s*(.+)'), r'<blockquote>\1</blockquote>', markdown)

    # Horizontal Rules
    markdown = re.sub(re.compile(r'---'), r'<hr>', markdown)

    #Paragrafo
    markdown = re.sub(r'^(?!<h[1-6]>|<ul>|<ol>|<li>|<blockquote>|<hr>|<code>)(.+)$', r'<p>\1</p>', markdown, flags=re.MULTILINE)

    return markdown

def main():
    # Verifica se o número de argumentos está correto
    if len(sys.argv) != 3:
        print("Uso: python3 md2html.py <arquivo_md> <arquivo_html>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    try:
        with open(input_filename, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()

        html_content = markdown_to_html(markdown_content)

        with open(output_filename, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        print(f"Conversão concluída com sucesso! O arquivo '{output_filename}' foi criado.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{input_filename}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
