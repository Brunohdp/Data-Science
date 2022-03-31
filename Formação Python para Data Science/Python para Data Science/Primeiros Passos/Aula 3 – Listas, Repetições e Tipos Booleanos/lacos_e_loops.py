'''def verifica_se_pode_dirigir(idade_usuario):
    if idade_usuario >= 18:
        print(f'{idade_usuario} anos de idade, TEM permissão dirigir!')
    else:
        print(f'{idade_usuario} anos de idade, NÃO tem idade para dirigir!')

for idade in idades:
    verifica_se_pode_dirigir(idade)'''


def verifica_se_pode_dirigir_loop_(idades):
    for idade in idades:
        if idade >= 18:
            print(f'{idade} anos de idade, TEM permissão dirigir!')
        else:
            print(f'{idade} anos de idade, NÃO tem idade para dirigir!')

idades = [18,20,12,22,15,35,47,17]
verifica_se_pode_dirigir_loop_(idades)
