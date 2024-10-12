use logos::Logos;
use std::collections::HashMap;

// Enum que representa os tipos de tokens
#[derive(Logos, Debug, PartialEq)]
enum Token {
    #[regex("[a-zA-Z_][a-zA-Z0-9_]*")]
    Identificador,

    #[regex("[0-9]+")]
    NumeroInteiro,

    #[token(">")]
    Maior,

    #[token("<")]
    Menor,

    #[token("=")]
    Igual,

    #[token(">=")]
    MaiorOuIgual,

    #[token("<=")]
    MenorOuIgual,

    #[token("!=")]
    Diferente,

    #[error]
    #[regex(r"[ \t\n\f]+", logos::skip)] // Ignora espaços em branco
    Erro,
}

// Estrutura da Tabela de Símbolos
struct TabelaSimbolos {
    simbolos: HashMap<String, String>,
}

impl TabelaSimbolos {
    fn new() -> TabelaSimbolos {
        let mut tabela = TabelaSimbolos {
            simbolos: HashMap::new(),
        };
        // Inserir palavras-chave reservadas (palavras-chave da linguagem) na tabela de símbolos
        tabela.inserir_palavra_chave("if".to_string());
        tabela.inserir_palavra_chave("else".to_string());
        tabela.inserir_palavra_chave("int".to_string());
        tabela.inserir_palavra_chave("return".to_string());
        tabela
    }

    // Função para inserir um identificador na tabela de símbolos
    fn inserir_identificador(&mut self, identificador: String) {
        self.simbolos.insert(identificador, "Identificador".to_string());
    }

    // Função para inserir uma palavra-chave
    fn inserir_palavra_chave(&mut self, palavra: String) {
        self.simbolos.insert(palavra, "Palavra-chave".to_string());
    }

    // Função para verificar se um identificador é uma palavra-chave
    fn e_palavra_chave(&self, identificador: &str) -> bool {
        self.simbolos.get(identificador) == Some(&"Palavra-chave".to_string())
    }

    // Exibe a tabela de símbolos
    fn exibir(&self) {
        println!("Tabela de Símbolos:");
        for (k, v) in &self.simbolos {
            println!("{}: {}", k, v);
        }
    }
}

// Estrutura do Analisador Léxico
struct AnalisadorLexico {
    tabela_simbolos: TabelaSimbolos,
}

impl AnalisadorLexico {
    fn new() -> AnalisadorLexico {
        AnalisadorLexico {
            tabela_simbolos: TabelaSimbolos::new(),
        }
    }

    // Função principal que realiza a análise léxica
    fn analisar(&mut self, entrada: &str) {
        let mut lexer = Token::lexer(entrada);

        while let Some(token) = lexer.next() {
            match token {
                Token::Identificador => {
                    let lexema = lexer.slice().to_string();
                    if self.tabela_simbolos.e_palavra_chave(&lexema) {
                        println!("Token: Palavra-chave, Lexema: {}", lexema);
                    } else {
                        println!("Token: Identificador, Lexema: {}", lexema);
                        self.tabela_simbolos.inserir_identificador(lexema);
                    }
                }
                Token::NumeroInteiro => {
                    let lexema = lexer.slice();
                    println!("Token: Número Inteiro, Valor: {}", lexema);
                }
                Token::Maior | Token::Menor | Token::Igual | Token::MaiorOuIgual | Token::MenorOuIgual | Token::Diferente => {
                    println!("Token: Operador Relacional, Operador: {}", lexer.slice());
                }
                Token::Erro => {
                    println!("Erro léxico no token: {}", lexer.slice());
                }
            }
        }

        // Exibir a tabela de símbolos ao final da análise
        self.tabela_simbolos.exibir();
    }
}

fn main() {
    let mut analisador = AnalisadorLexico::new();

    // Exemplo de entrada
    let entrada = "int x = 10; if(x > 5) x = x + 1;";
    
    analisador.analisar(entrada);
}
