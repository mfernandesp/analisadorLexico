#Equipe: Mariane Fernandes, Michael Robets, Yuri Levi

#PS: Criar arquivo Tokens.txt na raiz contendo os tokens a serem analisados

import re

##Inicio

#Divide os tokens lidos, retorna uma pilha de tokens no formato [classe, valor]
def trataTokens(rtokens):
  tokens = Pilha()
  ptokens = Pilha()

  tokens_aux = rtokens.split("\n")

  for token in tokens_aux:
    token_aux = token.split(",")
    tokens.empilha([token_aux[0], token_aux[1]])
  
  #inverter a pilha
  while(not tokens.vazia()):
    ptokens.empilha(tokens.desempilha())

  return ptokens

#verifica no automato
def automato(item, token):
  global pilha
  global acoes

  if(item == "S"):
    if(token == "0"):      
      pilha.empilha("17")
      pilha.empilha("[corpo]")
      pilha.empilha("16")
      pilha.empilha("0")
      acoes.empilha("S: [0] [16] [corpo] [17]")      
      return True
    else:
      return False
  elif(item == "[corpo]"):
    if(token == "1"):
      pilha.empilha("[corpo_if]")
      pilha.empilha("[corpo]")
      pilha.empilha("16")
      pilha.empilha("15")
      pilha.empilha("[expressão booleana]")
      pilha.empilha("14")
      pilha.empilha("1")
      acoes.empilha("[corpo]: [1][14][expressão booleana][15][16][corpo][corpo_if]")      
      return True
    elif(token == "3"):
      pilha.empilha("14")
      pilha.empilha("[declaração]")
      pilha.empilha("18")
      pilha.empilha("[expressão booleana]")
      pilha.empilha("15")
      pilha.empilha("16")
      pilha.empilha("[corpo]")
      pilha.empilha("17")
      pilha.empilha("3")
      acoes.empilha("[corpo]: [3][14][declaração][18][expressão booleana][18][expressão aritmética][15][16][corpo][17]")      
      return True
    elif(token == "4"):
      pilha.empilha("14")
      pilha.empilha("[expressão booleana]")
      pilha.empilha("15")
      pilha.empilha("16")
      pilha.empilha("[corpo]")
      pilha.empilha("17")
      pilha.empilha("4")
      acoes.empilha("[corpo]: [4][14][expressão booleana][15][16][corpo][17]")      
      return True
    elif(token == "5"):
      pilha.empilha("18")
      pilha.empilha("[declaração]")
      acoes.empilha("[corpo]: [declaração][18]")      
      return True
    else:
      return False



class Pilha(object):
    def __init__(self):
        self.dados = []

    def empilha(self, elemento):
        self.dados.append(elemento)

    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def vazia(self):
        return len(self.dados) == 0

tokens = Pilha()
pilha = Pilha()
acoes = Pilha()
analiseOk = True

pilha.empilha("S")

#Arquivo contendo os Tokens de entrada
aTokens = open ('Tokens.txt', 'r')
#Arquivo criado para salvar as a arvore sintatica gerada
aSintatica = open ('AnaliseSintatica.txt', 'w')

print('Lendo Arquivo contendo os Tokens\n')
#tokens_aux = aTokens.read()
tokens = trataTokens(aTokens.read())

#for item in pilha:
while ((not pilha.vazia()) and analiseOk):
  #pega o topo da pilha de tokens
  token = tokens.desempilha()
  #coloca novamente o topo na pilha 
  tokens.empilha(token)

  item = pilha.desempilha()

  if(re.match(token[0], item)):
    print("Encontrou: ", token[1])
    #retira o token da lista
    tokens.desempilha()
  else:
      analiseOk = automato(item, token[0])


if(analiseOk):
  print("Codigo reconhecido. Pilha de Estados")  
  while(not acoes.vazia()):
    a = acoes.desempilha()
    print(a)  
else:
  print("Codigo NÃO reconhecido")



aSintatica.close()
aTokens.close()

#Fim