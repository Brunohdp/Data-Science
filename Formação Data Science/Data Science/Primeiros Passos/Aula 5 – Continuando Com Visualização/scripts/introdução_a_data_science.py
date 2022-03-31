# -*- coding: utf-8 -*-
"""Introdução a Data Science

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkNPoLRZv-Ik_pPCwxUqAiMuGdARh8QB

# Aula 1 - Data Science: Dados e Visualização

## Conhecendo nossos dados
"""

import pandas as pd

notas = pd.read_csv('ratings.csv')

notas.head()

notas.shape

notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento']
notas.head()

notas['nota']

notas['nota'].unique()

notas['nota'].value_counts()

notas['nota'].mean()

"""## Visualizando dados com histograma e boxplot"""

notas.nota.plot(kind='hist')

notas.nota.median()

notas.nota.describe()

import seaborn as sns

sns.boxplot(notas.nota)

"""# Aula 2 - Análise Exploratória

## Análise exploratória de dados e mais gráficos
"""

filmes = pd.read_csv('movies.csv')
filmes. columns = ['filmeId', 'titulo', 'generos']
filmes.head()

notas.head()

notas.query('filmeId == 2').nota.mean()

notas.groupby('filmeId')

notas.groupby('filmeId').mean()

notas.groupby('filmeId').nota.mean()

notas.groupby('filmeId').nota.mean().to_frame()

medias_por_filme = notas.groupby('filmeId').nota.mean()

medias_por_filme.head()

medias_por_filme.plot(kind='hist')

sns.boxplot(medias_por_filme)

medias_por_filme.describe()

sns.distplot(medias_por_filme)

sns.distplot(medias_por_filme, bins=10)

import matplotlib.pyplot as plt

plt.hist(medias_por_filme)

plt.figure(figsize=(5,8))
sns.boxplot(y=medias_por_filme)

"""# Aula 3 – Variáveis

## Tipos de Variáveis
"""

tmdb = pd.read_csv('tmdb_5000_movies.csv')
tmdb.head()

# Categórica Nominal:

tmdb['original_language'].unique()

# Categórica Ordinal

# escolaridade: 1°, 2° e 3° graus
# 1 grau < 2 grau < 3 grau

# budget => orçamento => quantitativo contínuo

# Quantidade de votos => 1, 2, 3, 4, não tem 2.5 votos.
# notas do movielens => 0.5, 1, 1.5, ... ,5 não tem 2.7

"""# Aula 4 – Data Visualization

## Visualizando gráficos por categoria
"""

tmdb['original_language'].value_counts()

tmdb['original_language'].value_counts().index

tmdb['original_language'].value_counts().values

tmdb['original_language'].value_counts().to_frame()

contagem_de_lingua = tmdb['original_language'].value_counts().to_frame().reset_index()
contagem_de_lingua.columns = ['original_language', 'total']
contagem_de_lingua.head()

sns.barplot(x = 'original_language', y = 'total', data = contagem_de_lingua)

print(sns.__version__)

!pip install seaborn=0.9.0

sns.catplot(x = 'original_language', kind='count', data = tmdb)

"""## Passando uma mensagem através de visualização"""

plt.pie(contagem_de_lingua['total'], labels = contagem_de_lingua['original_language'])
plt.show()

total_por_lingua = tmdb['original_language'].value_counts()
total_geral = sum(total_por_lingua)
total_de_ingles = total_por_lingua.loc['en']
total_do_resto = total_geral - total_de_ingles
print(total_de_ingles, total_do_resto)

dados = {
    'lingua': ['ingles', 'outros'],
    'total': [total_de_ingles, total_do_resto]
}
dados = pd.DataFrame(dados)
dados

sns.barplot(x = 'lingua', y = 'total', data = dados)

"""## Visualizando as outras categorias"""

plt.pie(dados['total'], labels = dados['lingua'])

total_por_lingua_de_outros_filmes = tmdb.query("original_language != 'en'").original_language.value_counts()
total_por_lingua_de_outros_filmes

filmes_sem_lingua_original_em_ingles = tmdb.query("original_language != 'en'")
sns.catplot(x = 'original_language', kind = 'count', data = filmes_sem_lingua_original_em_ingles)

"""# Aula 5 – Continuando Com Visualização

## Refinando Visualizações
"""

plt.figure(figsize=(5, 10))
sns.catplot(x = 'original_language', kind = 'count', data = filmes_sem_lingua_original_em_ingles)

sns.catplot(x = 'original_language', kind = 'count', data = filmes_sem_lingua_original_em_ingles, aspect=2)

total_por_lingua_de_outros_filmes = tmdb.query("original_language != 'en'").original_language.value_counts()
sns.catplot(x = 'original_language', kind = 'count', data = filmes_sem_lingua_original_em_ingles, aspect=2, order=total_por_lingua_de_outros_filmes.index)

sns.catplot(x = 'original_language', kind = 'count', data = filmes_sem_lingua_original_em_ingles, aspect=2, palette='mako', order=total_por_lingua_de_outros_filmes.index)

