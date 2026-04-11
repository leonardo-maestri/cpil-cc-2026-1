# Código-fonte em "calculator language"
# para análise léxica
source : str = """
read a
read b
read c
result := (a + b) * c
write result
"""

# Caracteres considerados "em branco"
BLANKS = {
    " ",    # Espaço em branco 
    "\t",   # Tabulação
    "\n",   # Quebra de linha
    "\r"    # Retorno de linha
}

# Funções auxiliares
def is_alpha(c: str) -> bool:
    # Letras maiúsculas e minúsculas sem acento
    return c.isascii() and c.isalpha()

def is_digit(c: str) -> bool:
    # 0 a 9
    return c.isascii() and c.isdigit()

def is_alphanum(c: str) -> bool:
    # Maiúsculas e minúsculas sem acento + dígitos
    return c.isascii() and c.isalnum()

# Função que efetua a análise propriamente dita
def analyze(source: str) -> None:

    # Variáveis de controle
    state = 0
    lexeme = ""
    row = 1
    col = 1
    symbols_table = []

    # Adiciona uma quebra de linha ao final do código-fonte para
    # possibilitar o processamento do último lexema
    source += "\n"

    # Função que opera a mudança de estado
    def go_to_state(ch: str, next_state: int) -> tuple[str, int]:
        # Adiciona o ch atual ao lexema e move para o próximo estado
        return lexeme + ch, next_state

    # Função que aceita um lexema válido e o insere na tabela de símbolos
    def accept(ch: str, terminal: int) -> tuple[str, int]:
        pass    # Vamos implementar isso depois

    # Função que exibe um erro caso a análise léxica falhe
    def display_error(ch: str) -> None:
        pass    # Também vamos implementar isso depois

    pos = 0     # Posição atual de leitura dentro do código-fonte
    while pos < len(source):
        ch = source[pos]        # Lê um caractere do código fonte

        # Se for uma quebra de linha, ajusta a contagem de linhas e colunas
        if ch == "\n":
            row += 1
            col = 0

        match state:
            case 0:         
                if ch == "r":           lexeme, state = go_to_state(ch, 10)
                elif ch == "w":         lexeme, state = go_to_state(ch, 60)
                elif is_alpha(ch):      lexeme, state = go_to_state(ch, 50)
                elif is_digit(ch):      lexeme, state = go_to_state(ch, 110)
                elif ch == ".":         lexeme, state = go_to_state(ch, 130)
                elif ch == ":":         lexeme, state = go_to_state(ch, 150)
                elif ch == "+":         lexeme, state = accept(ch, 1006)
                elif ch == "-":         lexeme, state = accept(ch, 1007)
                elif ch == "*":         lexeme, state = accept(ch, 1008)
                elif ch == "/":         lexeme, state = accept(ch, 1009)
                elif ch == "(":         lexeme, state = accept(ch, 1010)
                elif ch == ")":         lexeme, state = accept(ch, 1011)
                elif ch in BLANKS:      pass        # Ignora
                else:                   display_error(ch)

            case 10:
                if ch == "e":           lexeme, state = go_to_state(ch, 20)
                elif is_alphanum(ch):   lexeme, state = go_to_state(ch, 50)
                elif ch in BLANKS:      lexeme, state = accept(ch, 1001)
                else                    display_error(ch)

            case 20:
                if ch == "a":           lexeme, state = go_to_state(ch, 30)
                elif is_alphanum(ch):   lexeme, state = go_to_state(ch, 50)
                elif ch in BLANKS:      lexeme, state = accept(ch, 1001)
                else:                   display_error(ch)

            case 30:
                if ch == "d":           lexeme, state = go_to_state(ch, 40)
                elif is_alphanum(ch):   lexeme, state = go_to_state(ch, 50)
                elif ch in BLANKS:      lexeme, state = accept(ch, 1001)
                else:                   display_error(ch)

            case 40:
                if is_alphanum(ch):     lexeme, state = go_to_state(ch, 50)
                if ch in BLANKS:        lexeme, state = accept(ch, 1002)
                else:                   display_error(ch)
            case 50:
                if is_alphanum(ch):     lexeme, state = go_to_state(ch, 50)
                if ch in BLANKS:        lexeme, state = accept(ch, 1001)
                else:                   display_error(ch)     
            case 60:
                if ch == "r":           lexeme, state = go_to_state(ch, 70)
                elif is_alphanum(ch):   lexeme, state = go_to_state(ch, 50)
                elif ch in BLANKS:      lexeme, state = accept(ch, 1001)
                else:                    display_error(ch)
            case 70:
                if ch == "i":           lexeme, state = go_to_state(ch, 80)
                elif is_alphanum(ch):   lexeme, state = go_to_state(ch, 50)
                elif ch in BLANKS:      lexeme, state = accept(ch, 1001)
                else:                    display_error(ch)
            case 80:
                if ch == "t":           lexeme, state = go_to_state(ch, 90)
                elif is_alphanum(ch):   lexeme, state = go_to_state(ch, 50)
                elif ch in BLANKS:      lexeme, state = accept(ch, 1001)
                else:                    display_error(ch)
            case 90:
                if ch == "e":           lexeme, state = go_to_state(ch, 100)
                elif is_alphanum(ch):   lexeme, state = go_to_state(ch, 50)
                elif ch in BLANKS:      lexeme, state = accept(ch, 1001)
                else:                    display_error(ch)
            case 100:
                elif is_alphanum(ch):   lexeme, state = go_to_state(ch, 50)
                elif ch in BLANKS:      lexeme, state = accept(ch, 1003)
                else:                    display_error(ch)
            case 110:
                if is_digit(ch)         lexeme, state = go_to_state(ch, 110)
                elif ch == ".":         lexeme, state = go_to_state(ch, 120)
                elif ch in BLANKS:      lexeme, state = accept(ch, 1004)
                else:                   display_error(ch)
            case 120:
                if is_digit(ch)         lexeme, state = go_to_state(ch, 120)
                elif ch in BLANKS:      lexeme, state = accept(ch, 1004)
                else:                   display_error(ch)
            case 130:
                if is_digit(ch)         lexeme, state = go_to_state(ch, 140)
            case 140:
                if is_digit(ch)         lexeme, state = go_to_state(ch, 140)
                elif ch in BLANKS:      lexeme, state = accept(ch, 1004)
                else:                   display_error(ch)
            case 150:
                if ch == "=":         lexeme, state = go_to_state(ch, 1005)
                else:                   display_error(ch)
            
                       
        
