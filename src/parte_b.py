import os
import argparse
from collections import defaultdict

class AnalisadorLexicoParteB:
    def __init__(self):
        # Tabela de símbolos inicializada com palavras-chave
        self.tabela_simbolos = {
            'def': 'palavra-chave', 
            'int': 'palavra-chave', 
            'float': 'palavra-chave', 
            'bool': 'palavra-chave', 
            'return': 'palavra-chave', 
            'print': 'palavra-chave', 
            ':=': 'operador_atribuicao'
        }
        self.tokens = []
        self.linha_atual = 1
        self.coluna_atual = 0
        self.erros = []
        self.contagem_nao_terminais = defaultdict(int)
        self.contagem_terminais = defaultdict(int)

    def adicionar_token(self, tipo, valor):
        self.tokens.append((tipo, valor))
        if tipo == 'identificador' or tipo == 'palavra-chave':
            self.contagem_terminais[valor] += 1
        elif tipo == 'numero_inteiro':
            self.contagem_terminais['num'] += 1
        elif tipo in ('operador_atribuicao', 'operador_aritmetico', 'delimitador', 'virgula'):
            self.contagem_terminais[valor] += 1

    def adicionar_nao_terminal(self, nome):
        self.contagem_nao_terminais[nome] += 1

    def adicionar_erro(self, mensagem):
        self.erros.append(mensagem)

    def analisar(self, entrada: str):
        i = 0
        tamanho = len(entrada)

        while i < tamanho:
            char = entrada[i]
            self.coluna_atual += 1

            # Ignorar espaços em branco e quebras de linha
            if char.isspace():
                if char == '\n':
                    self.linha_atual += 1
                    self.coluna_atual = 0
                i += 1
                continue
            
            # Verificar se é um número inteiro
            if char.isdigit():
                valor = ''
                while i < tamanho and entrada[i].isdigit():
                    valor += entrada[i]
                    i += 1
                self.adicionar_token('numero_inteiro', valor)
                continue
            
            # Verificar se é um identificador
            if char.isalpha() or char == '_':
                valor = ''
                while i < tamanho and (entrada[i].isalnum() or entrada[i] == '_'):
                    valor += entrada[i]
                    i += 1
                if valor in self.tabela_simbolos:
                    self.adicionar_token('palavra-chave', valor)
                else:
                    self.adicionar_token('identificador', valor)
                continue
            
            # Verificar operadores
            if char == ':':
                if i + 1 < tamanho and entrada[i + 1] == '=':
                    self.adicionar_token('operador_atribuicao', ':=')
                    i += 2
                    continue
            
            # Verificar vírgula
            if char == ',':
                self.adicionar_token('virgula', char)
                i += 1
                continue

            # Verificar delimitadores
            if char in ('{', '}', '(', ')', ';'):
                self.adicionar_token('delimitador', char)
                i += 1
                continue
            
            # Verificar operadores aritméticos
            if char in ('+', '-', '*', '/'):
                self.adicionar_token('operador_aritmetico', char)
                i += 1
                continue

            # Captura de erro léxico
            self.adicionar_erro(f"Erro léxico na linha {self.linha_atual}, coluna {self.coluna_atual}: caractere inválido '{char}'")
            i += 1  # Continue para o próximo caractere

        return self.tokens, self.erros

    def analisar_arquivo(self, caminho_arquivo: str):
        caminho_absoluto = os.path.abspath(caminho_arquivo)
        if not os.path.isfile(caminho_absoluto):
            print(f"O arquivo não foi encontrado: {caminho_absoluto}")
            return None 
        
        with open(caminho_absoluto, 'r') as file:
            conteudo = file.read()
        return self.analisar(conteudo)

    def exibir_saida(self):
        # Exibir contagem de não terminais
        print(f"Total de não terminais = {len(self.contagem_nao_terminais)}:")
        for nao_terminal, contagem in self.contagem_nao_terminais.items():
            print(f"{nao_terminal} (1)")  # Exibe cada não terminal, assumindo que eles aparecem uma vez

        print("--------------------")
        
        # Exibir contagem de terminais
        print(f"Total de terminais = {sum(self.contagem_terminais.values())}:")
        for terminal, contagem in self.contagem_terminais.items():
            if contagem > 1:
                print(f"{terminal} ({contagem})")
            else:
                print(terminal)
        print("--------------------")

def main():
    parser = argparse.ArgumentParser(description='Analisador Léxico - Parte B')
    parser.add_argument('caminho_arquivo', type=str, help='Caminho do arquivo a ser analisado')

    args = parser.parse_args()

    analisador = AnalisadorLexicoParteB()
    tokens, erros = analisador.analisar_arquivo(args.caminho_arquivo)

    if erros:
        print("Erros léxicos encontrados:")
        for erro in erros:
            print(erro)
    else:
        print("Tokens reconhecidos:")
        for token in tokens:
            print(token)

    analisador.exibir_saida()

if __name__ == '__main__':
    main()
