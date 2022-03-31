# -*- coding: utf-8 -*-
"""Corretor

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13NQPcUsZ70fx-y7V5I5CJS7RDCZWSku0

# <font color = green>Aula 1 – Explorando Um Projeto De NLP

## <font color = blackpink>Importando Um Corpus Textual
"""

with open('artigos.txt', 'r') as f:
  artigos = f.read()

print(artigos[:500])

"""---

## <font color = blackpink>Tokenização
"""

len(artigos)

texto_exemplo = 'Olá, tudo bem?'
tokens = texto_exemplo.split()
print(tokens)

len(artigos.split())

"""---
---

# <font color = green>Aula 2 – Utilizando NLTK Para Tokenizar Um Texto

## <font color = blackpink>Refinando a Tokenização
"""

import nltk
nltk.download('punkt')

palavras_separadas = nltk.tokenize.word_tokenize(texto_exemplo)
palavras_separadas

"""---

## <font color = blackpink>Separando Palavras De Tokens
"""

'palavra'.isalpha()

def separa_palavras(lista_tokens: list):
  lista_palavras = []
  for token in lista_tokens:
    if token.isalpha():
      lista_palavras.append(token)
  return lista_palavras

separa_palavras(palavras_separadas)

"""---

## <font color=blackpink>Contando Palavras Do Corpus
"""

lista_tokens = nltk.tokenize.word_tokenize(artigos)
lista_palavras = separa_palavras(lista_tokens)
print(f'O número de palavras é: {len(lista_palavras)}')

"""---

## <font color = blackpink>Normalização
"""

print(lista_palavras[:5])

def normalizacao(lista_palavras: list):
  lista_normalizada = []
  for palavra in lista_palavras:
    lista_normalizada.append(palavra.lower())
  return lista_normalizada

lista_normalizada = normalizacao(lista_palavras)
lista_normalizada[:5]

"""---

## <font color=blackpink>Tipos De Palavras
"""

set([1,1,1,3,4,4,5,8,2,4,5,5,6,6])

len(set(lista_normalizada))

"""---
---

# <font color=green>Aula 3 – Desenvolvendo e Testando o Corretor

## <font color=blackpink>Fatiando Strings
"""

lista = 'lgica'
(lista[:1],lista[1:])

palavra_exemplo = 'lgica'

def gerador_palavras(palavra):
  fatias = []
  for i in range(len(palavra) + 1):
    fatias.append((lista[:i],lista[i:]))
  print(fatias)
  # palavras_geradas = insere_letras(fatias)
  # return palavras_geradas

gerador_palavras(palavra_exemplo)

"""---

## <font color=blackpink>Operação De Inserção
"""

palavra_exemplo = 'lgica'


def insere_letras(fatias):
  novas_palavras = []
  letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
  for E, D in fatias:
    for letra in letras:
      novas_palavras.append(E + letra + D)
  return novas_palavras


def gerador_palavras(palavra):
  fatias = []
  for i in range(len(palavra) + 1):
    fatias.append((palavra[:i],palavra[i:]))
  palavras_geradas = insere_letras(fatias)
  return palavras_geradas


palavras_geradas = gerador_palavras(palavra_exemplo)
palavras_geradas

"""---

## <font color=blackpink>Construindo a Função Corretor
"""

def corretor(palavra):
  palavras_geradas = gerador_palavras(palavra)
  palavra_correta = max(palavras_geradas, key = probabilidade)
  return palavra_correta

# Meu método kkk

for palavra in palavras_geradas:
  for pal in lista_unica:
    if palavra == pal:
      print(palavra)

"""---

## <font color=blackpink>Probabilidade Das Palavras Geradas
"""

frequencia = nltk.FreqDist(lista_normalizada)
total_palavras = len(lista_normalizada)
frequencia.most_common(10)

frequencia["lógica"]

def probabilidade(palavras_geradas):
  return frequencia[palavras_geradas]/total_palavras

probabilidade('logica')

corretor('lgica')

"""---
---

# <font color=green>Aula 4 – Avaliando a Qualidade do Corretor

## <font color=blackpink>Preparando Dados de Teste
"""

def cria_dados_teste(nome_arquivo):
  lista_palavras_teste = []
  f = open(nome_arquivo, 'r')
  for linha in f:
    correta, errada = linha.split()
    lista_palavras_teste.append((correta, errada))
  f.close()
  return lista_palavras_teste

lista_teste = cria_dados_teste('palavras.txt')

"""---

## <font color=blackpink>Avaliando o Corretor
"""

def avaliador(testes):
  numero_palavras = len(testes)
  acertou = 0
  for correta, errada in testes:
    palavra_corrigida = corretor(errada)
    if palavra_corrigida == correta:
      acertou += 1
  taxa_acerto = acertou/numero_palavras
  print(f'Taxa de acerto: {taxa_acerto*100:.2f}% de {numero_palavras} palavras')

avaliador(lista_teste)

"""---
---

# <font color=green>Aula 5 – Incrementando o Corretor

## <font color=blackpink>Implementando o Delete de Caracteres
"""

def deletando_caracter(fatias):
  novas_palavras = []
  for E, D in fatias:
    novas_palavras.append(E + D[1:])
  return novas_palavras

"""---

## <font color=blackpink>Avaliando o Novo Corretor
"""

gerador_palavras('lóigica')

corretor('lóigica')

def gerador_palavras(palavra):
  fatias = []
  for i in range(len(palavra) + 1):
    fatias.append((palavra[:i],palavra[i:]))
  palavras_geradas = insere_letras(fatias)
  palavras_geradas += deletando_caracter(fatias)
  return palavras_geradas


palavras_geradas = gerador_palavras('lóigica')
palavras_geradas

avaliador(lista_teste)

corretor('lgica')

"""---
---

# <font color=green>Aula 6 – Corrigindo os Principais Erros de Digitação

## <font color=blackpink>Implementando a Troca de Letras
"""

def insere_letras(fatias):
  novas_palavras = []
  letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
  for E, D in fatias:
    for letra in letras:
      novas_palavras.append(E + letra + D)
  return novas_palavras


def deletando_caracter(fatias):
  novas_palavras = []
  for E, D in fatias:
    novas_palavras.append(E + D[1:])
  return novas_palavras


def troca_letra(fatias):
  novas_palavras = []
  letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
  for E, D in fatias:
    for letra in letras:
      novas_palavras.append(E + letra + D[1:])
  return novas_palavras


def gerador_palavras(palavra):
  fatias = []
  for i in range(len(palavra) + 1):
    fatias.append((palavra[:i],palavra[i:]))
  palavras_geradas = insere_letras(fatias)
  palavras_geradas += deletando_caracter(fatias)
  palavras_geradas += troca_letra(fatias)
  return palavras_geradas

corretor('lóhica')

"""---

## <font color=blackpink>Implementando a Inversão de Letras
"""

def inverte_letra(fatias):
  novas_palavras = []
  for E, D in fatias:
    if len(D) > 1:
      novas_palavras.append(E + D[1] + D[0] + D[2:])
  return novas_palavras

def gerador_palavras(palavra):
  fatias = []
  for i in range(len(palavra) + 1):
    fatias.append((palavra[:i],palavra[i:]))
  palavras_geradas = insere_letras(fatias)
  palavras_geradas += deletando_caracter(fatias)
  palavras_geradas += troca_letra(fatias)
  palavras_geradas += inverte_letra(fatias)
  return palavras_geradas

def insere_letras(fatias):
  novas_palavras = []
  letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
  for E, D in fatias:
    for letra in letras:
      novas_palavras.append(E + letra + D)
  return novas_palavras


def deletando_caracter(fatias):
  novas_palavras = []
  for E, D in fatias:
    novas_palavras.append(E + D[1:])
  return novas_palavras


def troca_letra(fatias):
  novas_palavras = []
  letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
  for E, D in fatias:
    for letra in letras:
      novas_palavras.append(E + letra + D[1:])
  return novas_palavras


def inverte_letra(fatias):
  novas_palavras = []
  for E, D in fatias:
    if len(D) > 1:
      novas_palavras.append(E + D[1] + D[0] + D[2:])
  return novas_palavras


def gerador_palavras(palavra):
  fatias = []
  for i in range(len(palavra) + 1):
    fatias.append((palavra[:i],palavra[i:]))
  palavras_geradas = insere_letras(fatias)
  palavras_geradas += deletando_caracter(fatias)
  palavras_geradas += troca_letra(fatias)
  palavras_geradas += inverte_letra(fatias)
  return palavras_geradas

corretor('lógiac')

avaliador(lista_teste)

"""---
---

# <font color=green>Aula 7 – Criando um Corretor Turbinado

## <font color=blackpink>Palavras Desconhecidas Ao Vocabulário
"""

def avaliador(testes, vocabulario):
  numero_palavras = len(testes)
  acertou = 0
  desconhecida = 0
  
  for correta, errada in testes:
    palavra_corrigida = corretor(errada)
    if palavra_corrigida == correta:
      acertou += 1
    else:
      desconhecida += (correta not in vocabulario)
  
  taxa_acerto = acertou/numero_palavras
  taxa_desconhecida = desconhecida/numero_palavras
  
  print(f'Taxa de acerto: {taxa_acerto*100:.2f}% de {numero_palavras} palavras')
  print(f'Taxa de desconhecidas: {taxa_desconhecida*100:.2f}%')

vocabulario = set(lista_normalizada)
avaliador(lista_teste, vocabulario)

"""---

## <font color=blackpink>Turbinando O Gerador De Palavras
"""

palavra = 'lóiigica'

def gerador_turbinado(palavras_geradas):
  novas_palavras = []
  for palavra in palavras_geradas:
    novas_palavras += gerador_palavras(palavra)
  return novas_palavras

palavras_g = gerador_turbinado(gerador_palavras(palavra))
'lógica' in palavras_g

len(palavras_g)

"""---

## <font color=blackpink>Escolhendo Os Melhores Candidatos
"""

def novo_corretor(palavra):
  palavras_geradas = gerador_palavras(palavra)
  palavras_turbinado = gerador_turbinado(palavras_geradas)
  
  todas_palavras = set(palavras_geradas + palavras_turbinado)
  candidatos = [palavra]
  
  for palavra in todas_palavras:
    if palavra in vocabulario:
      candidatos.append(palavra)
  
  palavra_correta = max(candidatos, key = probabilidade)
  
  return palavra_correta

novo_corretor(palavra)

"""---
---

# <font color=green>Aula 8 – Avaliando e Interpretando o Erro do Corretor Turbinado

## <font color=blackpink>Avaliando O Resultado Dos Dois Corretores
"""

def avaliador(testes, vocabulario):
  numero_palavras = len(testes)
  acertou = 0
  desconhecida = 0
  
  for correta, errada in testes:
    palavra_corrigida = novo_corretor(errada)
    desconhecida += (correta not in vocabulario)
    if palavra_corrigida == correta:
      acertou += 1
    else:
      print(errada + '-' + corretor(errada) + '-' + palavra_corrigida)
  
  taxa_acerto = acertou/numero_palavras
  taxa_desconhecida = desconhecida/numero_palavras
  
  print(f'Taxa de acerto: {taxa_acerto*100:.2f}% de {numero_palavras} palavras')
  print(f'Taxa de desconhecidas: {taxa_desconhecida*100:.2f}%')

avaliador(lista_teste, vocabulario)

"""---

## <font color=blackpink>Avaliando o Resultado dos Dois Corretores Cont
"""

def avaliador(testes, vocabulario):
  numero_palavras = len(testes)
  acertou = 0
  desconhecida = 0
  
  for correta, errada in testes:
    palavra_corrigida = corretor(errada)
    desconhecida += (correta not in vocabulario)
    if palavra_corrigida == correta:
      acertou += 1
  
  taxa_acerto = acertou/numero_palavras
  taxa_desconhecida = desconhecida/numero_palavras
  
  print(f'Taxa de acerto: {taxa_acerto*100:.2f}% de {numero_palavras} palavras')
  print(f'Taxa de desconhecidas: {taxa_desconhecida*100:.2f}%')

avaliador(lista_teste, vocabulario)

palavra = 'ló gica'

print(novo_corretor(palavra))
print(corretor(palavra))

