#Equipe: Mariane Fernandes, Michael Robets, Yuri Levi

#PS: Criar arquivo CodigoFonte.txt na raiz contendo o texto do codigo fonte a ser analisado

import re

##Inicio

#ler mais de uma linha
def inputCodigo():
 lines = []
 while True:
   line = input()
   if line:
       lines.append(line)
   else:
       break
 text = ' '.join(lines)
 return text

#cria uma tabela com as palavras reservadas possiveis
def definirPalavrasReservadas():
  reservadas = []
  reservadas.append("main")
  reservadas.append("{")
  reservadas.append("}")
  reservadas.append("(")
  reservadas.append(")")
  reservadas.append("if")
  reservadas.append("else")  
  reservadas.append("for")
  reservadas.append("while")
  reservadas.append("int")
  reservadas.append("float")
  reservadas.append("string")
  reservadas.append("and")
  reservadas.append("or")
  reservadas.append("=")
  reservadas.append("+")
  reservadas.append("-")
  reservadas.append("*")
  reservadas.append("/")
  reservadas.append(";")

  return reservadas

#cria uma tabela com as classes léxicas
def definirClasses():
  classes = []
  #Codigo, Classe Léxica, Expressão Regular
  classes.append([0, "main", "^main$"])
  classes.append([1, "if", "^if$"])
  classes.append([2, "else", "^else$"])
  classes.append([3, "for", "^for$"])
  classes.append([4, "while", "^while$"])  
  classes.append([5, "tipo de identificador", "^int$|^float$|^string$"])
  classes.append([6, "atribuição", "^=$"])
  classes.append([7, "identificador", "^[a-zA-Z][a-zA-Z0-9]*$"])
  classes.append([8, "operador relacional", "^==$|^!=$|^<$|^<=$|^>$|^>=$"])
  classes.append([9, "operador aritmético", "^[+]$|^[-]$|^[/]$|^[*]$"])
  classes.append([10, "operador lógico", "^and$|^or$"])
  classes.append([11, "inteiro", "^[-]?[0-9]+$"])
  classes.append([12, "float", "^[-]?[0-9][.][0-9]([0-9]+)?$"])
  classes.append([13, "string", "^[\"](.*)[\"]$"])
  classes.append([14, "abrir parênteses", "[(]"])
  classes.append([15, "fechar parênteses", "[)]"])
  classes.append([16, "abrir chaves", "[{]"])
  classes.append([17, "fechar chaves", "[]}]"])
  classes.append([18, "delimitador de linha", "[;]"])

  return classes
  
#divide o código em lexemas
def trataTextoCodigo(codigo):
  #Alterar qualquer tipo de espaço em branco(\t\n\r\f\v) por ' '
  codigo = re.sub("\s", " ", codigo)
  
  #Remove os espaços seguidos
  codigo = re.sub("[ ]+", " ", codigo)

  #Divide o codigo pelo ' '
  lexemas = codigo.split(" ")

  return lexemas

lexemas = []
tokens = []
tabelaSimbolos = []
palavrasReservadas = definirPalavrasReservadas()

#Arquivo contendo codigo fonte
codigoFonte = open ('CodigoFonte.txt', 'r')
#Arquivo criado para salvar as Tokens geradas
aTokens = open ('Tokens.txt', 'w')

print('Lendo Arquivo contendo codigo fonte\n')
codigo = codigoFonte.read()
lexemas = trataTextoCodigo(codigo)



#Verifica se o lexema pertence a linguagem e depois cria o token
for lexema in lexemas :
  classes =  definirClasses()
  for classe in classes:  
    if re.match(classe[2], lexema):
      if classe[0] != 7:
        tokens.append([classe[0], lexema])
      #verifica se o indentificador não é uma palavra reservada
      elif lexema not in palavrasReservadas:        
        if(lexema not in tabelaSimbolos):
          tokens.append([classe[0], len(tabelaSimbolos)])
          tabelaSimbolos.append(lexema)
        else:
          tokens.append([classe[0], tabelaSimbolos.index(lexema)])




print('\nTokens gerados:\n')
print('O caractere "," foi escolhido para, dentro de cada token, separar o código do tipo de lexema do lexema propriamente dito.')
#aTokens.write('O caractere "," foi escolhido para, dentro de cada token, separar o código do tipo de lexema do lexema propriamente dito.')
print('Para mais fácil visualização, cada token será representado em uma diferente linha.\n')
#aTokens.write('Para mais fácil visualização, cada token será representado em uma diferente linha.\n' + '\n')

#Imprime tokens
for token in tokens:
  if(token[0] == 7):
    print(str(token[0]) + ',' + tabelaSimbolos[token[1]])
    aTokens.write(str(token[0]) + ',' + tabelaSimbolos[token[1]] + '\n')
  else:
    print(str(token[0]) + ',' + token[1])
    aTokens.write(str(token[0]) + ',' + token[1] + '\n')
  
print('\nTabelas de Simbolos gerada:\n')



#Imprime tokens
for simbolo in tabelaSimbolos:
    print(simbolo)

print('\nArquivo Tokens.txt gerado no diretório raiz.')

aTokens.close()
codigoFonte.close()

#Fim