# Parte 1: Analisadores Léxicos


### Descrição
---------
Este projeto implementa um analisador léxico que identifica identificadores, números inteiros e operadores relacionais com base em diagramas de transição. Além disso, há uma tabela de símbolos que armazena os identificadores e palavras-chave da linguagem, conforme previsto na atividade solicitada pelo professor da disciplina INE5622.

### Requisitos
----------
- Rust 1.75.0+
- Cargo (gerenciador de pacotes do Rust)

### Como rodar o projeto
--------------------
1. Clone o repositório:

   `git clone https://github.com/CunhaVanessa/INE5622-parte1.git`

   `cd INE5622-parte1` 

2. Instale as dependências e compile o projeto:

   `cargo build` 

3. Execute o analisador léxico com um arquivo de entrada:

   `cargo run -- inputs/entrada_correta.txt`

### Estrutura do repositório
------------------------
- src/ contém o código-fonte do analisador léxico.
- inputs/ contém os arquivos de teste de entrada.
- outputs/contém saídas esperadas de teste.
- tests/ contém testes automatizados.

### Arquivos de entrada
-------------------
1. entrada_correta.txt - Arquivo com tokens válidos para testar o analisador léxico.
2. entrada_errada_A.txt - Arquivo com erros para testar a captura de erros léxicos na parte A.
3. entrada_errada_B.txt - Arquivo com erros para testar a captura de erros léxicos na parte B.

### Entrada e saída esperada
------------------------
1. Para entradas corretas, o programa gera uma lista de tokens e exibe a tabela de símbolos.
2. Para entradas com erros léxicos, o programa informa o erro e a posição (linha e coluna).

### Como rodar os testes
-------------------------------
Para rodar os testes basta executar o seguinte comando:

   `cargo test`

### Instruções adicionais
---------------------
1. O projeto foi desenvolvido e testado em ambiente Linux. 
2. As instruções de execução e compilação são compatíveis com distribuições Linux com suporte a Rust.
