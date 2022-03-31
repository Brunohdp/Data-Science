def verifica_se_pode_dirigir_sem_parametros():
    idade = input('Qual a sua idade?\nR: ')
    idade = int(idade)
    if idade >= 18:
        return print(f'Você tem permissão dirigir!')
    else:
        raise ValueError('Você não tem idade para dirigir!')

verifica_se_pode_dirigir_sem_parametros()
