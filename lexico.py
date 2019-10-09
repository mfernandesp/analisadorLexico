import re

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
  reservadas = [];
  reservadas.append("main")
  reservadas.append("{")
  reservadas.append("}")
  reservadas.append("(")
  reservadas.append(")")
  reservadas.append("if")
  reservadas.append("else")  
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

  return reservadas;

def definirClasses():
  classes = [[]];
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
  classes.append([9, "operador aritmético", "^+$|^-$|^/$|^*$"])
  classes.append([10, "operador lógico", "^and$|^or$"])
  classes.append([11, "inteiro", "^[-]?[0-9]+$"])
  classes.append([12, "float", "^[-]?[0-9]+([.][0-9]+)?$"])
  #falta ler caracter especial
  classes.append([13, "string", "^[\"][0-9a-zA-Z\\t\\n\\r ]*[\"]$"])
  classes.append([14, "abrir parênteses", "("])
  classes.append([15, "fechar parênteses", ")"])
  classes.append([16, "abrir chaves", "{"])
  classes.append([17, "fechar chaves", "}"])
  classes.append([18, "delimitador de linha", ";"])

  return classes;
  

def trataTextoCodigo(codigo):
  #Remove os espaços seguidos
  #codigo = codigo.replace("  ", " ")  
  codigo = re.sub("\s", " ", codigo)
  codigo = re.sub("[ ]+", " ", codigo)

  #Divide o codigo pelo ' '
  lexemas = codigo.split(" ")

  return lexemas
#  for item in lexemas :
 #   item = '_' + item + '_'
  #  print('Codigo é:', item)
 
  #Remove as tabulações
 # for item in lexemas :
  #  item = item.replace("\t", "")
 
  #Remove os espaços
 # for item in lexemas :
  #  item = item.replace(" ", "")    
   # if item == "" or "\t" or "\n":
    #  del(lexemas[lexemas.index(item)])

  

def reconhecerExpressaoRegular(fragmentoTexto):
  result = true
  for classe in definirClasses():
    re.match fragmentoTexto

def criaToken(fragmentoTexto):
  s = 1
    

lexemas = []
tokens = []

palavrasReservadas = definirPalavrasReservadas();

print('Insira o codigo\n')
#codigo = trataTextoCodigo(inputCodigo())
codigo = inputCodigo()
lexemas = trataTextoCodigo(codigo)

#Verifica se o lexema pertence a linguagem e depois cria o token
for lexema in lexemas :
  if(reconhecerExpressaoRegular(lexema)):
    token.append(criaToken)

 
#Imprime
for item in lexemas :
 item = '_' + item + '_'
 print('Codigo é:', item)
