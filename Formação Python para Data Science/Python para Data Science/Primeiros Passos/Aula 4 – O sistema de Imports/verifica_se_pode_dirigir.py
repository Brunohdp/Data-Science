idade = 20

def verifica_se_pode_dirigir(idade_usuario):
    if idade_usuario >= 18:
        return print(f'Você tem permissão dirigir!')
    else:
        raise ValueError('Você não tem idade para dirigir!')

verifica_se_pode_dirigir(idade)

