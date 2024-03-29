from datetime import datetime
from collections import Counter

class Pessoa:
    def __init__(self, id, index, dataEMD, primeiro_nome, ultimo_nome, idade, genero, morada, modalidade, clube, email, federado, resultado):
        self.id = id
        self.index = index
        self.dataEMD = datetime.strptime(dataEMD, '%Y-%m-%d')
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = int(idade)
        self.genero = genero
        self.morada = morada
        self.modalidade = modalidade
        self.clube = clube
        self.email = email
        self.federado = federado.lower() in ['sim', 'true', '1']
        self.resultado = resultado.lower() in ['true', 'sim', '1']

    def __repr__(self):
        return f"Pessoa({self.id}, {self.index}, {self.dataEMD}, {self.primeiro_nome}, {self.ultimo_nome}, {self.idade}, {self.genero}, {self.morada}, {self.modalidade}, {self.clube}, {self.email}, {self.federado}, {self.resultado})"

#lista as modalidades por ordem alfabética
def listar_modalidades(pessoas):
    modalidades = sorted({pessoa.modalidade for pessoa in pessoas})
    print("Modalidades desportivas ordenadas alfabeticamente:")
    for modalidade in modalidades:
        print(modalidade)

#mostra as percentagens dos atletas aptos ou não aptos (resultado = true ou false)
def percentagem_aptidao(pessoas):
    total = len(pessoas)
    aptos = sum(pessoa.resultado for pessoa in pessoas)
    percent_aptos = (aptos / total) * 100
    percent_inaptos = 100 - percent_aptos
    print(f"Percentagem de atletas aptos: {percent_aptos:.2f}%")
    print(f"Percentagem de atletas inaptos: {percent_inaptos:.2f}%")

#mostra quantos atletas estão entre os intrevalos de idades (intrevalos de 5 a 5)
def distribuicao_por_idade(pessoas):
    escaloes = Counter(((pessoa.idade // 5) * 5 for pessoa in pessoas))
    print("Distribuição de atletas por escalão etário:")
    for escalao, count in sorted(escaloes.items()):
        print(f"[{escalao}-{escalao + 4}]: {count} atletas")

# Caminho para o arquivo
archive = 'emd.csv'

pessoas = []

with open(archive, 'r', encoding='utf-8') as file:
    next(file)  # Ignora a primeira linha (cabeçalho)
    for line in file:
        row = line.strip().split(',')  # Remove espaços em branco e quebra a linha por vírgula
        if row:  # Verifica se a linha não está vazia
            pessoa = Pessoa(*row)
            pessoas.append(pessoa)

while True:
    print("\nMenu:")
    print("1. Lista ordenada alfabeticamente das modalidades desportivas")
    print("2. Percentagens de atletas aptos e inaptos para a prática desportiva")
    print("3. Distribuição de atletas por escalão etário")
    print("4. Sair")
    
    escolha = input("Escolhe uma opção: ")

    if escolha == '1':
        listar_modalidades(pessoas)
    elif escolha == '2':
        percentagem_aptidao(pessoas)
    elif escolha == '3':
        distribuicao_por_idade(pessoas)
    elif escolha == '4':
        print("Adeus...")
        break
    else:
        print("Opção inválida. Tenta novamente.")

