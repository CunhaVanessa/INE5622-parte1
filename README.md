# INE5622 - Parte 1: Analisadores Léxicos 

### Alunos
- Gabriel Terra (21105570)
- Pedro Bressan (22100920)
- Vanessa Cunha (17100926)

### Descrição
---------
Este projeto implementa dois analisadores léxicos em Python. O primeiro analisador (Parte A) identifica os tokens mapeados, números inteiros e operadores relacionais, utilizando uma tabela de símbolos que armazena palavras-chave e identificadores. O segundo analisador (Parte B) processa a entrada para identificar terminais e não terminais da linguagem LSI-2024-2, registrando erros léxicos quando encontra tokens não reconhecidos. Ambos os analisadores foram desenvolvidos conforme as diretrizes da atividade solicitada pelo professor da disciplina INE5622.


### Requisitos
----------
- Python 3.12.3 ou superior
- Bibliotecas Python necessárias:
  - `argparse`
  - `os`
  - `collections`
  - `re`

Para instalar as dependências necessárias:

`pip install argparse collections re`

### Como rodar o projeto
--------------------
1. Clone o repositório:

`git clone https://github.com/CunhaVanessa/INE5622-parte1.git`

`cd INE5622-parte1`

2. Execute a Parte A manualmente, o analisador léxico com um arquivo de entrada, idealmente dentro da pasta src:

`python src/parte_a.py inputs_partea/input_partea_correta.txt`
         
OU

`python3 src/parte_a.py inputs_partea/input_partea_incorreta.txt`

3. Execute a Parte B manualmente, o analisador léxico com um arquivo de entrada:

`python src/parte_b.py inputs_parteb/input_parteb_correta.txt`
         
OU

`python3 src/parte_b.py inputs_parteb/input_parteb_incorreta.txt`

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
**Parte A:**
- Entradas corretas: Neste caso o programa gera uma lista de tokens e exibe a tabela de símbolos, diferenciando entre identificadores, palavras-chave e operadores.
- Entradas com erros: Já aqui a classe informa a linha e coluna onde o erro léxico ocorreu.

**Parte B:**
- Entradas corretas: A classe gera uma lista de tokens reconhecidos da linguagem LSI-2024-2, exibindo contagem de terminais e não terminais.
- Entradas com erros: Nesse exemplo a classe identifica a linha e coluna onde ocorreu o erro léxico e emite uma mensagem apropriada.

### Gramática LSI-2024-2
---------------------
A linguagem descrita pela gramática LSI-2024-2 possui tokens que são explicitamente reconhecidos pelo analisador léxico. Os tokens incluem:

- Palavras-chave: `int, if, else, def, print, return`
- Operadores: `<, >, <=, >=, =, <>, +, -, *, /, :=`
- Delimitadores: `(, ), {, }, ,, ;`
- Outros: identificadores e números inteiros

### Informações adicionais
---------------------
1. O projeto foi desenvolvido e testado em ambiente Linux e macOS.
2. As instruções de execução são compatíveis com distribuições Linux e macOS com suporte a Python.
3. Os scripts devem ser executados a partir do diretório base do projeto para que os caminhos dos arquivos de entrada sejam reconhecidos corretamente.

### Decisões de desenvolvimento
---------------------
Durante o desenvolvimento experimentamos um bocado com C++ e o FLEX, com o Rust e , também utilizando o Python com o PLY, por fim após a última aula tomamos a decisão de seguir com uma implementa manual da tabela de símbolos para ter mais flexibilidade no futuro, nas outras partes do trabalho. Embora o FLEX com C++ tenha se mostrado bastante eficiente, ficamos receosos em relação a desenvolvimentos mais complexo então por fim ficamos com python que é a linguagem comum para todos no grupo.
Em nossa percepção implementar o lexer manualmente em Python nos permitiu explorar e aplicar conceitos fundamentais de análise léxica que vimos em aula, como o uso de diagramas de transição e técnicas de resolução de ambiguidades como o "maximal munch". Acreditamos que facilitou a personalização de regras e o tratamento explícito de erros, garantindo que o projeto fosse didático para todos, além de cumprir os requisitos sem dependências externas complicadas.