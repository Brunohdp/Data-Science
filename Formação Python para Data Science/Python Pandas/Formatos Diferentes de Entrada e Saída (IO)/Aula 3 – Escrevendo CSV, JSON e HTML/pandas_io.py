# -*- coding: utf-8 -*-
"""Pandas IO

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hwaixKU5O01xSJsiKxtGdY8S6b6-pmwV

# Criando os nomes
"""

import pandas as pd

nomes_f = pd.read_json("https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking?qtd=200&sexo=f")
nomes_m = pd.read_json("https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking?qtd=200&sexo=m")

print(f'Quantidade de nomes: {len(nomes_f) + len(nomes_m)}')

frames = [nomes_f, nomes_m]

type(frames)

nomes = pd.concat(frames)['nome'].to_frame()

nomes.sample(5)

nomes.columns.name = ''

nomes.head()

"""# Incluindo ID dos Alunos"""

import numpy as np
np.random.seed(123)

total_alunos = len(nomes)
total_alunos

nomes['id_aluno'] = np.random.permutation(total_alunos) + 1

nomes.sample(5)

dominios = ['@dominiodoemail.com.br', '@servicodoemail.com']
nomes['dominio'] = np.random.choice(dominios, total_alunos)

nomes

nomes['email'] = nomes.nome.str.cat(nomes.dominio).str.lower()

nomes.sample(5)

"""# Criando a Tabela Cursos"""

!pip3 install html5lib
!pip3 install lxml

import html5lib

url = 'http://tabela-cursos.herokuapp.com/index.html'
cursos = pd.read_html(url)

cursos

type(cursos)

cursos = cursos[0]

type(cursos)

"""# Alterando o Index de cursos"""

cursos.head()

cursos.rename(columns={'Nome do curso' : 'Nome_do_curso'}, inplace=True)
cursos.head()

cursos['id_curso'] = cursos.index + 1

cursos.head()

cursos = cursos.set_index('id_curso')
cursos.head()

"""# Matriculando os Alunos nos cursos"""

nomes.sample(5)

nomes['matriculas'] = np.ceil(np.random.exponential(size=total_alunos) * 1.5).astype(int)

nomes.sample(5)

nomes.matriculas.describe()

import seaborn as sns

sns.distplot(nomes.matriculas)

nomes.matriculas.value_counts()

nomes.sample(5)

"""# Selecionando cursos"""

todas_matriculas = []
x = np.random.rand(20)
prob = x / sum(x)

for index, row in nomes.iterrows():
  id = row.id_aluno
  matriculas = row.matriculas
  for i in range(matriculas):
    mat = [id, np.random.choice(cursos.index, p = prob)]
    todas_matriculas.append(mat)

matriculas = pd.DataFrame(todas_matriculas, columns = ['id_aluno', 'id_curso'])

matriculas.head()

matriculas.groupby('id_curso').count().join(cursos['Nome_do_curso']).rename(columns={'id_aluno': 'quantidade_de_alunos'})

matriculas_por_curso = matriculas.groupby('id_curso').count().join(cursos['Nome_do_curso']).rename(columns={'id_aluno': 'quantidade_de_alunos'})

matriculas_por_curso

"""# Saída em diferentes formatos"""

matriculas_por_curso.head(3)

matriculas_por_curso.to_csv('matriculas_por_curso.csv', index= False)

matriculas_json = matriculas_por_curso.to_json()
matriculas_json

matriculas_html = matriculas_por_curso.to_html()
print(matriculas_html)

