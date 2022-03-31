permissoes = []
idades = [18,14,22,15,47]

def verifica_se_pode_dirigir(idades, permissoes):
    for idade in idades:
        if idade >= 18:
            permissoes.append(True)
        else:
            permissoes.append(False)
    print(permissoes)

verifica_se_pode_dirigir(idades, permissoes)

for permissao in permissoes:
    if permissao:
        print('Tem permissão para dirigir')
    else:
        print('Não tem permissão para dirigir')
