# INE5622 - Parte 1: Analisadores Léxicos 

### Alunos:
- Gabriel Terra (21105570)
- Pedro Bressan (22100920)
- Vanessa Cunha (17100926)

### Descrição
---------
Este projeto implementa dois analisadores léxicos em Python. O primeiro analisador (Parte A) identifica identificadores, números inteiros e operadores relacionais, utilizando uma tabela de símbolos que armazena palavras-chave e identificadores. O segundo analisador (Parte B) processa a entrada para identificar terminais e não terminais, registrando erros léxicos quando encontra tokens não reconhecidos. Ambos os analisadores foram desenvolvidos conforme as diretrizes da atividade solicitada pelo professor da disciplina INE5622.

### Requisitos
----------
- Python 3.10 ou superior

### Como rodar o projeto
--------------------
1. Clone o repositório:

        git clone https://github.com/CunhaVanessa/INE5622-parte1.git

        cd INE5622-parte1 

2. Execute a Parte A manualmente, o analisador léxico com um arquivo de entrada:

         python src/parte_a.py inputs_partea/input_partea_correta.txt
         
        OU

         python src/parte_a.py inputs_partea/input_partea_incorreta.txt

3. Execute a Parte B manualmente, o analisador léxico com um arquivo de entrada:

         python src/parte_b.py inputs_parteb/input_parteb_correta.txt
         
        OU

         python src/parte_b.py inputs_parteb/input_parteb_incorreta.txt


### Estrutura do repositório
------------------------
- `src/` contém o código-fonte dos analisadores léxicos.
- `inputs_partea/` contém os arquivos de teste de entrada para a Parte A.
- `inputs_parteb/` contém os arquivos de teste de entrada para a Parte B.

### Arquivos de entrada
-------------------
1. `input_partea_correta.txt` - Arquivo com tokens válidos para testar o analisador léxico da Parte A.
2. `input_partea_incorreta.txt` - Arquivo com erros para testar a captura de erros léxicos na Parte A.
3. `input_parteb_correta.txt` - Arquivo com tokens válidos para testar o analisador da Parte B.
4. `input_parteb_incorreta.txt` - Arquivo com erros para testar a captura de erros léxicos na Parte B.

### Entrada e saída esperada
------------------------
1. Para entradas corretas, o programa gera uma lista de tokens e exibe a tabela de símbolos na Parte A, e contabiliza terminais e não terminais na Parte B.
2. Para entradas com erros léxicos, o programa informa o erro e a posição (linha e coluna).

### Instruções adicionais
---------------------
1. O projeto foi desenvolvido e testado em ambiente Linux e macOS. 
2. As instruções de execução são compatíveis com distribuições Linux e macOS com suporte a Python.
