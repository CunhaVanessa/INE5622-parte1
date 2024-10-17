"""
- Gabriel Terra (21105570)
- Pedro Bressan (22100920)
- Vanessa Cunha (17100926)
"""

import os
import argparse

class AnalisadorLexicoParteA:
    def __init__(self):
        # Tabela de símbolos inicializada com palavras-chave
        self.tabela_simbolos = {
            'int': 'palavra-chave', 
            'float': 'palavra-chave', 
            'bool': 'palavra-chave', 
            'if': 'palavra-chave', 
            'else': 'palavra-chave'
        }
        self.tokens = []
        self.linha_atual = 1
        self.coluna_atual = 0

    def adicionar_token(self, tipo, valor):
        self.tokens.append((tipo, valor))

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
            
            # Verificar operadores relacionais
            if char == '=':
                if i + 1 < tamanho and entrada[i + 1] == '=':
                    self.adicionar_token('igual', '==')
                    i += 2
                else:
                    self.adicionar_token('igual', char)
                    i += 1
                continue
            
            if char == '!':
                if i + 1 < tamanho and entrada[i + 1] == '=':
                    self.adicionar_token('diferente', '!=')
                    i += 2
                else:
                    # Captura de erro léxico
                    print(f"Erro léxico na linha {self.linha_atual}, coluna {self.coluna_atual}: caractere inválido '{char}'")
                    i += 1
                continue

            if char in ('>', '<'):
                op = char
                if i + 1 < tamanho and entrada[i + 1] == '=':
                    op += '='
                    self.adicionar_token('operador_relacional', op)
                    i += 2
                else:
                    self.adicionar_token('operador_relacional', op)
                    i += 1
                continue
            
            # Captura de erro léxico
            print(f"Erro léxico na linha {self.linha_atual}, coluna {self.coluna_atual}: caractere inválido '{char}'")
            i += 1  # Continue para o próximo caractere

        return self.tokens

    def analisar_arquivo(self, caminho_arquivo: str):
        caminho_absoluto = os.path.abspath(caminho_arquivo)
        print(f"Tentando abrir o arquivo: {caminho_absoluto}")
        if not os.path.isfile(caminho_absoluto):
            print(f"O arquivo não foi encontrado: {caminho_absoluto}")
            return None 
        
        with open(caminho_absoluto, 'r') as file:
            conteudo = file.read()
        return self.analisar(conteudo)

def main():
    parser = argparse.ArgumentParser(description='Analisador Léxico - Parte A')
    parser.add_argument('caminho_arquivo', type=str, help='Caminho do arquivo a ser analisado')

    args = parser.parse_args()

    analisador = AnalisadorLexicoParteA()
    tokens = analisador.analisar_arquivo(args.caminho_arquivo)

    if tokens:
        print("Tokens reconhecidos:")
        for token in tokens:
            print(token)

if __name__ == '__main__':
    main()
