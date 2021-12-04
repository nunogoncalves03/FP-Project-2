# Project 2 - The Meadow

################################# TAD posicao #################################
# Representação: R[(x, y)] = (x, y)
# cria_posicao: int X int -> posicao
# cria_copia_posicao: posicao -> posicao
# obter_pos_x: posicao -> int
# obter_pos_y: posicao -> int
# eh_posicao: universal -> booleano
# posicoes_iguais: posicao X posicao -> booleano
# posicao_para_str: posicao -> str

def cria_posicao(x, y):
    '''
    cria_posicao: int X int -> posicao
    Esta função recebe os valores correspondentes às coordenadas de uma posição
    e devolve a posição correspondente. Verifica a validade dos seus argumentos,
    gerando um ValueError caso os mesmos não sejam válidos.
    '''    
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError('Escreve essa merda bem. Caralho')    
    return (x, y)


def cria_copia_posicao(p):
    '''
    cria_copia_posicao: posicao -> posicao
    Esta função recebe uma posição e devolve uma cópia nova da posição. Verifica
    a validade do seu argumento, gerando um ValueError caso o mesmo não seja 
    válido.
    '''
    if not eh_posicao(p):
        raise ValueError('cria_copia_posicao: argumento invalido')
    return cria_posicao(p[0], p[1])


def obter_pos_x(p):
    '''
    obter_pos_x: posicao -> int
    Esta função devolve a componente x da posição p.
    '''
    return p[0]


def obter_pos_y(p):
    '''
    obter_pos_y: posicao -> int
    Esta função devolve a componente y da posição p.
    '''
    return p[1]


def eh_posicao(arg):
    '''
    eh_posicao: universal -> booleano
    Esta função devolve True caso o seu argumento seja um TAD posicao e False
    caso contrário.
    '''
    return type(arg) == tuple and len(arg) == 2 and type(arg[0]) == int and \
       type(arg[1]) == int and arg[0] >= 0 and arg[1] >= 0


def posicoes_iguais(p1, p2):
    '''
    posicoes_iguais: posicao X posicao -> booleano
    Esta função devolve True apenas se p1 e p2 são posições e são iguais.
    '''
    return eh_posicao(p1) and eh_posicao(p2) and p1[0] == p2[0] and \
        p1[1] == p2[1]


def posicao_para_str(p):
    '''
    posicao_para_str: posicao -> str
    Esta função devolve a cadeia de caracteres '(x, y)' que representa o seu
    argumento, sendo os valores x e y as coordenadas de p.
    '''
    return '({}, {})'.format(obter_pos_x(p), obter_pos_y(p))

############################ Funções de alto nível ############################
def obter_posicoes_adjacentes(p):
    '''
    obter_posicoes_adjacentes: posicao -> tuplo
    Esta função devolve um tuplo com as posições adjacentes à posição p,
    começando pela posição acima de p e seguindo no sentido horário.
    '''
    posicoes = ()
    if obter_pos_y(p) != 0:
        posicoes += (cria_posicao(obter_pos_x(p), obter_pos_y(p) - 1),)
    posicoes += (cria_posicao(obter_pos_x(p) + 1, obter_pos_y(p)), \
        cria_posicao(obter_pos_x(p), obter_pos_y(p) + 1))
    if obter_pos_x(p) != 0:
        posicoes += (cria_posicao(obter_pos_x(p) - 1, obter_pos_y(p)),)
    return posicoes


def ordenar_posicoes(t):
    '''
    ordenar_posicoes: tuplo -> tuplo
    Esta função devolve um tuplo contendo as mesmas posições do tuplo fornecido
    como argumento, ordenadas de acordo com a ordem de leitura do prado.
    '''
    return tuple(sorted(sorted(list(t), key=lambda x: obter_pos_x(x)), \
        key=lambda x: obter_pos_y(x)))

################################## TAD animal #################################
# Representação: R[animal] = {'especie': s, 'freq_reproducao': r, \
# 'freq_alimentacao': a, 'idade': idade, 'fome': fome}
# cria_animal: str X int X int -> animal
# cria_copia_animal: animal -> animal
# obter_especie: animal -> str
# obter_freq_reproducao: animal -> int
# obter_freq_alimentacao: animal -> int
# obter_idade: animal -> int
# obter_fome: animal -> int
# aumenta_idade: animal -> animal
# reset_idade: animal -> animal
# aumenta_fome: animal -> animal
# reset_fome: animal -> animal
# eh_animal: universal -> booleano
# eh_predador: universal -> booleano
# eh_presa: universal -> booleano
# animais_iguais: animal X animal -> booleano
# animal_para_char: animal -> str
# animal_para_str: animal -> str

def cria_animal(s, r, a):
    '''
    cria_animal: str X int X int -> animal
    Esta função recebe uma cadeia de caracteres s correspondente à espécie do
    animal e dois valores inteiros correspondentes à frequência de reprodução r
    e à frequência de alimentação a; e devolve o animal. Verifica a validade dos
    seus argumentos, gerando um ValueError caso os mesmos não sejam válidos.
    '''    
    if type(s) != str or s == '' or type(r) != int or r <= 0 or type(a) != int \
       or a < 0:
        raise ValueError('cria_animal: argumentos invalidos')
    return {'especie': s, 'freq_reproducao': r, 'freq_alimentacao': a, \
        'idade': 0, 'fome': 0}


def cria_copia_animal(a):
    '''
    cria_copia_animal: animal -> animal
    Esta função recebe um animal a e devolve uma nova cópia do animal. Verifica
    a validade do seu argumento, gerando um ValueError caso o mesmo não seja
    válido.
    '''
    if not eh_animal(a):
        raise ValueError('cria_copia_animal: argumento invalido')
    return {'especie': a['especie'], 'freq_reproducao': a['freq_reproducao'], \
        'freq_alimentacao': a['freq_alimentacao'], 'idade': a['idade'], \
            'fome': a['fome']}


def obter_especie(a):
    '''
    obter_especie: animal -> str
    Esta função devolve a cadeia de caracteres correspondente à espécie do
    animal.
    '''
    return a['especie']


def obter_freq_reproducao(a):
    '''
    obter_freq_reproducao: animal -> int
    Esta função devolve a frequência de reprodução do animal a.
    '''
    return a['freq_reproducao']


def obter_freq_alimentacao(a):
    '''
    obter_freq_alimentacao: animal -> int
    Esta função devolve a frequência de alimentação do animal a.
    '''
    return a['freq_alimentacao']


def obter_idade(a):
    '''
    obter_idade: animal -> int
    Esta função devolve a idade do animal a.
    '''
    return a['idade']


def obter_fome(a):
    '''
    obter_fome: animal -> int
    Esta função devolve a fome do animal a.
    '''
    return a['fome']


def aumenta_idade(a):
    '''
    aumenta_idade: animal -> animal
    Esta função modifica destrutivamente o animal a incrementando o valor da sua
    idade em uma unidade, e devolve o próprio animal.
    '''
    a['idade'] += 1
    return a


def reset_idade(a):
    '''
    reset_idade: animal -> animal
    Esta função modifica destrutivamente o animal a definindo o valor da sua
    idade igual a 0, e devolve o próprio animal.
    '''
    a['idade'] = 0
    return a


def aumenta_fome(a):
    '''
    aumenta_fome: animal -> animal
    Esta função modifica destrutivamente o animal predador a incrementando o
    valor da sua fome em uma unidade, e devolve o próprio animal. Não modifica
    os animais presa.
    '''
    if obter_freq_alimentacao(a) == 0:
        return a
    a['fome'] += 1
    return a


def reset_fome(a):
    '''
    reset_fome: animal -> animal
    Esta função modifica destrutivamente o animal predador a definindo o valor
    da sua fome igual a 0, e devolve o próprio animal. Não modifica os animais
    presa.
    '''
    if a['freq_alimentacao'] == 0:
        return a
    a['fome'] = 0
    return a


def eh_animal(arg):
    '''
    eh_animal: universal -> booleano
    Esta função devolve True caso o seu argumento seja um TAD animal e False
    caso contrário.
    '''
    if type(arg) != dict or len(arg) != 5:
        return False    
    for caracteristica in arg:
        if caracteristica not in ('especie', 'freq_reproducao', 'idade', \
                                  'fome', 'freq_alimentacao'):
            return False
    if type(arg['especie']) != str or arg['especie'] == '' or \
       type(arg['freq_reproducao']) != int or arg['freq_reproducao'] <= 0 or \
       type(arg['freq_alimentacao']) != int or arg['freq_alimentacao'] < 0:
        return False 
    return True


def eh_predador(arg):
    '''
    eh_predador: universal -> booleano
    Esta função devolve True caso o seu argumento seja um TAD animal do tipo
    predador e False caso contrário.
    '''
    return eh_animal(arg) and obter_freq_alimentacao(arg) > 0


def eh_presa(arg):
    '''
    eh_presa: universal -> booleano
    Esta função devolve True caso o seu argumento seja um TAD animal do tipo
    presa e False caso contrário.
    '''
    return eh_animal(arg) and obter_freq_alimentacao(arg) == 0


def animais_iguais(a1, a2):
    '''
    animais_iguais: animal X animal -> booleano
    Esta função devolve True apenas se a1 e a2 são animais e são iguais.
    '''
    return eh_animal(a1) and eh_animal(a2) and \
           obter_especie(a1) == obter_especie(a2) and \
           obter_freq_reproducao(a1) == obter_freq_reproducao(a2) and \
           obter_freq_alimentacao(a1) == obter_freq_alimentacao(a2) and \
           obter_idade(a1) == obter_idade(a2) and \
           obter_fome(a1) == obter_fome(a2)


def animal_para_char(a):
    '''
    animal_para_char: animal -> str
    Esta função devolve a cadeia de caracteres correspondente ao primeiro
    caracter da espécie do animal passada por argumento, em maiúscula para
    animais predador e em minúscula para animais presa.
    '''
    if eh_predador(a):
        return obter_especie(a)[0].upper()
    return obter_especie(a)[0].lower()


def animal_para_str(a):
    '''
    animal_para_str: animal -> str
    Esta função devolve a cadeia de caracteres que representa o animal.
    '''
    if eh_predador(a):
        return '{} [{}/{};{}/{}]'.format(obter_especie(a), obter_idade(a), \
        obter_freq_reproducao(a), obter_fome(a), obter_freq_alimentacao(a))
    return '{} [{}/{}]'.format(obter_especie(a), obter_idade(a), \
                               obter_freq_reproducao(a))

############################ Funções de alto nível ############################
def eh_animal_fertil(a):
    '''
    eh_animal_fertil: animal -> booleano
    Esta função devolve True caso o animal a tenha atingido a idade de
    reprodução e False caso contrário.
    '''
    return obter_idade(a) >= obter_freq_reproducao(a)


def eh_animal_faminto(a):
    '''
    eh_animal_faminto: animal -> booleano
    Esta função devolve True caso o animal a tenha atingindo um valor de fome
    igual ou superior à sua frequência de alimentação e False caso contrário. As
    presas devolvem sempre False.
    '''
    if eh_predador(a):
        return obter_fome(a) >= obter_freq_alimentacao(a)
    return False


def reproduz_animal(a):
    '''
    reproduz_animal: animal -> animal
    Esta função recebe um animal a e modifica destrutivamente o animal passado
    como argumento alterando a sua idade para 0; e devolve um novo animal da
    mesma espécie com idade e fome igual a 0.
    '''
    reset_idade(a)
    return cria_animal(obter_especie(a), obter_freq_reproducao(a), \
        obter_freq_alimentacao(a))

################################## TAD prado ##################################
# Representação: R[prado] = {'dimensao': (tamanho_x, tamanho_y), 'rochedos': r,\
# 'animais': [{'animal': a1, 'posicao': p1}, {'animal': a2, 'posicao': p2},...]}
# cria_prado: posicao X tuplo X tuplo X tuplo -> prado
# cria_copia_prado: prado -> prado
# obter_tamanho_x: prado -> int
# obter_tamanho_y: prado -> int
# obter_numero_predadores: prado -> int
# obter_numero_presas: prado -> int
# obter_posicao_animais: prado -> tuplo posicoes
# obter_animal: prado X posicao -> animal
# eliminar_animal: prado X posicao -> prado
# mover_animal: prado X posicao X posicao -> prado
# inserir_animal: prado X animal X posicao -> prado
# eh_prado: universal -> booleano
# eh_posicao_animal: prado X posicao -> booleano
# eh_posicao_obstaculo: prado X posicao -> booleano
# eh_posicao_livre: prado X posicao -> booleano
# prados_iguais: prado X prado -> booleano
# prado_para_str: prado -> str

def cria_prado(d, r, a, p):
    '''
    cria_prado: posicao X tuplo X tuplo X tuplo -> prado
    Esta função recebe uma posição d correspondente à posição que ocupa a
    montanha do canto inferior direito do prado, um tuplo r com as posições dos
    rochedos, um tuplo a com os animais, e um tuplo p com as posições ocupadas
    pelos animais; e devolve o prado que representa internamente o mapa e os
    animais presentes. Verifica a validade dos seus argumentos, gerando um
    ValueError caso os mesmos não sejam válidos.
    '''
    def posicao_invalida(posicao):
        '''
        posicao_invalida: posicao -> booleano
        Esta função recebe uma posição e devolve True se a mesma for inválida.
        '''
        return obter_pos_x(posicao) == 0 or obter_pos_y(posicao) == 0 or \
            obter_pos_x(posicao) >= obter_pos_x(d) or \
            obter_pos_y(posicao) >= obter_pos_y(d)


    if not eh_posicao(d) or type(r) != tuple or type(a) != tuple or len(a) == 0\
         or type(p) != tuple or len(p) != len(a):
        raise ValueError('cria_prado: argumentos invalidos')
    prado = {'dimensao': cria_posicao(obter_pos_x(d) + 1, obter_pos_y(d) + 1), \
        'rochedos': (), 'animais': []}
    for posicao in r:
        # Verificação da existência de dois ou mais rochedos na mesma posição
        if not eh_posicao(posicao) or posicao_invalida(posicao) or \
            len(tuple(filter(lambda x: posicoes_iguais(x, posicao), r))) > 1:
            raise ValueError('cria_prado: argumentos invalidos')
        prado['rochedos'] += (posicao,)
    for animal in a:
        if not eh_animal(animal):
            raise ValueError('cria_prado: argumentos invalidos')
    for posicao in p:
        # Verificação da existência de dois ou mais animais na mesma posição
        if not eh_posicao(posicao) or posicao_invalida(posicao) or \
            len(tuple(filter(lambda x: posicoes_iguais(x, posicao), p))) > 1:
            raise ValueError('cria_prado: argumentos invalidos')
        for posicao_rochedo in r:
            if posicoes_iguais(posicao, posicao_rochedo):
                raise ValueError('cria_prado: argumentos invalidos')
    for indice in range(0, len(a)):
        prado['animais'] += [{'animal': a[indice], 'posicao': p[indice]}]
    return prado


def cria_copia_prado(m):
    '''
    cria_copia_prado: prado -> prado
    Esta função recebe um prado e devolve uma nova cópia do prado. Verifica a
    validade do seu argumento, gerando um ValueError caso o mesmo não seja 
    válido.
    '''
    if not eh_prado(m):
        raise ValueError('cria_copia_prado: argumento invalido')
    dimensao = cria_copia_posicao(cria_posicao(obter_tamanho_x(m) - 1, \
                                               obter_tamanho_y(m) - 1))
    rochedos = ()
    for posicao in m['rochedos']:
        rochedos += (cria_copia_posicao(posicao),)
    animais = posicoes = ()
    for animal in m['animais']:
        animais += (cria_copia_animal(animal['animal']),)
        posicoes += (cria_copia_posicao(animal['posicao']),)               
    return cria_prado(dimensao, rochedos, animais, posicoes)


def obter_tamanho_x(m):
    '''
    obter_tamanho_x: prado -> int
    Esta função devolve o valor inteiro que corresponde à dimensão Nx do prado.
    '''
    return obter_pos_x(m['dimensao'])


def obter_tamanho_y(m):
    '''
    obter_tamanho_y: prado -> int
    Esta função devolve o valor inteiro que corresponde à dimensão Ny do prado.
    '''
    return obter_pos_y(m['dimensao'])


def obter_numero_predadores(m):
    '''
    obter_numero_predadores: prado -> int
    Esta função devolve o número de animais predadores no prado.
    '''
    numero_predadores = 0
    for animal in m['animais']:
        if eh_predador(animal['animal']):
            numero_predadores += 1
    return numero_predadores


def obter_numero_presas(m):
    '''
    obter_numero_presas: prado -> int
    Esta função devolve o número de animais presa no prado.
    '''
    numero_presas = 0
    for animal in m['animais']:
        if eh_presa(animal['animal']):
            numero_presas += 1
    return numero_presas


def obter_posicao_animais(m):
    '''
    obter_posicao_animais: prado -> tuplo posicoes
    Esta função devolve um tuplo contendo as posições do prado ocupadas por
    animais, ordenadas em ordem de leitura do prado.
    '''
    lista_posicoes = []
    for animal in m['animais']:
        lista_posicoes += [animal['posicao']]
    return tuple(sorted(sorted(lista_posicoes, key=lambda x: obter_pos_x(x)), \
        key=lambda x: obter_pos_y(x)))


def obter_animal(m, p):
    '''
    obter_animal: prado X posicao -> animal
    Esta função devolve o animal do prado que se encontra na posição p.
    '''
    for animal in m['animais']:
        if posicoes_iguais(animal['posicao'], p):
            return animal['animal']


def eliminar_animal(m, p):
    '''
    eliminar_animal: prado X posicao -> prado
    Esta função modifica destrutivamente o prado m eliminando o animal da
    posição p; e devolve o próprio prado.
    '''
    m['animais'] = list(filter(lambda x: not posicoes_iguais(x['posicao'], p), \
        m['animais']))
    return m


def mover_animal(m, p1, p2):
    '''
    mover_animal: prado X posicao X posicao -> prado
    Esta função modifica destrutivamente o prado m movimentando o animal da
    posição p1 para a nova posição p2; e devolve o próprio prado.
    '''
    for animal in m['animais']:
        if posicoes_iguais(animal['posicao'], p1):
            animal['posicao'] = p2
    return m


def inserir_animal(m, a, p):
    '''
    inserir_animal: prado X animal X posicao -> prado
    Esta função modifica destrutivamente o prado m acrescentando na posição p
    do prado o animal a passado com argumento; e devolve o próprio prado.
    '''
    m['animais'] += [{'animal': a, 'posicao': p}]
    return m


def eh_prado(arg):
    '''
    eh_prado: universal -> booleano
    Esta função devolve True caso o seu argumento seja um TAD prado e False caso
    contrário.
    '''
    def posicao_invalida(posicao):
        '''
        posicao_invalida: posicao -> booleano
        Esta função recebe uma posição e devolve True se a mesma for inválida.
        '''
        return obter_pos_x(posicao) == 0 or obter_pos_y(posicao) == 0 or \
               obter_pos_x(posicao) >= obter_pos_x(arg['dimensao']) - 1 or \
               obter_pos_y(posicao) >= obter_pos_y(arg['dimensao']) - 1
    

    if type(arg) != dict or len(arg) != 3:
        return False
    for chave in arg:
        if chave not in ('dimensao', 'rochedos', 'animais'):
            return False
        if chave == 'dimensao' and not eh_posicao(arg['dimensao']):
            return False
        elif chave == 'rochedos':
            if type(arg['rochedos']) != tuple:
                return False
            for posicao in arg['rochedos']:
                if not eh_posicao(posicao) or posicao_invalida(posicao) or \
                    len(tuple(filter(lambda x: posicoes_iguais(x, posicao), \
                        arg['rochedos']))) > 1:
                    return False
        elif chave == 'animais':
            if type(arg['animais']) != list or len(arg['animais']) == 0:
                return False
            for animal in arg['animais']:
                if type(animal) != dict or len(animal) != 2 or not \
                    eh_animal(animal['animal']) or not \
                    eh_posicao(animal['posicao']) or posicao_invalida\
                    (animal['posicao']):
                    return False
                for posicao_rochedo in arg['rochedos']:
                    if posicoes_iguais(animal['posicao'], posicao_rochedo):
                        return False
    return True


def eh_posicao_animal(m, p):
    '''
    eh_posicao_animal: prado X posicao -> booleano
    Esta função devolve True apenas no caso da posição p do prado estar ocupada
    por um animal.
    '''
    for posicao in obter_posicao_animais(m):
        if posicoes_iguais(posicao, p):
            return True
    return False


def eh_posicao_obstaculo(m, p):
    '''
    eh_posicao_obstaculo: prado X posicao -> booleano
    Esta função devolve True apenas no caso da posição p do prado corresponder
    a uma montanha ou rochedo.
    '''
    for posicao in m['rochedos']:
        if posicoes_iguais(posicao, p):
            return True
    return obter_pos_x(p) == 0 or obter_pos_y(p) == 0 or \
           obter_pos_x(p) == obter_pos_x(m['dimensao']) - 1 or \
           obter_pos_y(p) == obter_pos_y(m['dimensao']) - 1


def eh_posicao_livre(m, p):
    '''
    eh_posicao_livre: prado X posicao -> booleano
    Esta função devolve True apenas no caso da posição p do prado corresponder
    a um espaço livre.
    '''
    return not eh_posicao_animal(m, p) and not eh_posicao_obstaculo(m, p)


def prados_iguais(p1, p2):
    '''
    prados_iguais: prado X prado -> booleano
    Esta função devolve True apenas se p1 e p2 forem prados e forem iguais.
    '''
    if not eh_prado(p1) or not eh_prado(p2) or not \
       posicoes_iguais(p1['dimensao'], p2['dimensao']) or \
       len(p1['rochedos']) != len(p2['rochedos']) or \
       len(p1['animais']) != len(p2['animais']):
        return False
    for indice in range(0, len(p1['rochedos'])):
        if not posicoes_iguais(p1['rochedos'][indice], p2['rochedos'][indice]):
            return False
    for indice in range(0, len(p1['animais'])):
        if not animais_iguais(p1['animais'][indice]['animal'], \
                              p2['animais'][indice]['animal']):
            return False
        if not posicoes_iguais(p1['animais'][indice]['posicao'], \
                               p2['animais'][indice]['posicao']):
            return False
    return True


def prado_para_str(m):
    '''
    prado_para_str: prado -> str
    Esta função devolve uma cadeia de caracteres que representa o prado.
    '''
    prado = '+' + '-' * (obter_tamanho_x(m) - 2)  + '+\n'
    for y in range(1, obter_tamanho_y(m) - 1):
        prado += '|'
        for x in range(1, obter_tamanho_x(m) - 1):
                if eh_posicao_livre(m, cria_posicao(x, y)):
                    prado += '.'
                elif eh_posicao_obstaculo(m, cria_posicao(x, y)):
                    prado += '@'
                elif eh_posicao_animal(m, cria_posicao(x, y)):
                    prado += '{}'.format(animal_para_char(obter_animal(m, \
                                                        cria_posicao(x, y))))
                if x == obter_tamanho_x(m) - 2:
                    prado += '|\n'
    return prado + '+' + '-' * (obter_tamanho_x(m) - 2)  + '+'

############################ Funções de alto nível ############################
def obter_valor_numerico(m, p):
    '''
    obter_valor_numerico: prado X posicao -> int
    Esta função devolve o valor numérico da posição p correspondente à ordem de
    leitura no prado m.
    '''
    return obter_pos_y(p) * obter_tamanho_x(m) + obter_pos_x(p)


def obter_movimento(m, p):
    '''
    obter_movimento: prado X posicao -> posicao
    Esta função devolve a posição seguinte do animal na posição p dentro do
    prado m de acordo com as regras de movimento dos animais no prado.
    '''    
    if eh_presa(obter_animal(m, p)):
        posicoes_disponiveis = tuple(filter(lambda x: eh_posicao_livre(m, x), \
                                            obter_posicoes_adjacentes(p)))
        return posicoes_disponiveis[obter_valor_numerico(m, p) % \
            len(posicoes_disponiveis)] if len(posicoes_disponiveis) != 0 else p
    else:
        # Verificação da existência de presas nas posições adjacentes
        if tuple(filter(lambda x: eh_posicao_animal(m, x) and \
            eh_presa(obter_animal(m, x)), obter_posicoes_adjacentes(p))) == ():
            posicoes_disponiveis = tuple(filter(lambda x: \
                        eh_posicao_livre(m, x), obter_posicoes_adjacentes(p)))
            return posicoes_disponiveis[obter_valor_numerico(m, p) % \
            len(posicoes_disponiveis)] if len(posicoes_disponiveis) != 0 else p
        posicoes_disponiveis = tuple(filter(lambda x: eh_posicao_animal(m, \
            x) and eh_presa(obter_animal(m, x)), obter_posicoes_adjacentes(p)))
        return posicoes_disponiveis[obter_valor_numerico(m, p) % \
            len(posicoes_disponiveis)] if len(posicoes_disponiveis) != 0 else p

############################# Funções adicionais ##############################
def geracao(m):
    '''
    geracao: prado -> prado
    É a função auxiliar que modifica o prado m fornecido como argumento de
    acordo com a evolução correspondente a uma geração completa, e devolve o
    próprio prado.
    '''
    animais_movidos = ()
    for y in range(0, obter_tamanho_y(m)):
        for x in range(0, obter_tamanho_x(m)):
            p = cria_posicao(x, y)
            # Verifica se o animal da posição p já foi movido durante a geração
            if eh_posicao_animal(m, p) and tuple(filter(lambda x: \
                                posicoes_iguais(x, p), animais_movidos)) == ():
                animal = aumenta_fome(aumenta_idade(obter_animal(m, p)))
                if eh_animal_fertil(animal) and not \
                   posicoes_iguais(obter_movimento(m, p), p):
                    posicao_final = obter_movimento(m, p)
                    reset_idade(animal)
                    if eh_predador(animal) and eh_posicao_animal(m, \
                    posicao_final) and eh_presa(obter_animal(m, posicao_final)):
                        reset_fome(animal)
                        eliminar_animal(m, posicao_final)                    
                    animais_movidos += (posicao_final,)
                    mover_animal(m, p, posicao_final)
                    inserir_animal(m, reproduz_animal(animal), p)
                elif posicoes_iguais(obter_movimento(m, p), p):
                    pass
                else:
                    posicao_final = obter_movimento(m, p)
                    if eh_predador(animal) and eh_posicao_animal(m, \
                    posicao_final) and eh_presa(obter_animal(m, posicao_final)):
                        reset_fome(animal)
                        eliminar_animal(m, posicao_final)                    
                    animais_movidos += (posicao_final,)
                    mover_animal(m, p, posicao_final)
                if eh_animal_faminto(animal):
                    eliminar_animal(m, posicao_final)
                    # Remove a posição do animal no tuplo dos animais movidos
                    animais_movidos = tuple(filter(lambda x: not \
                            posicoes_iguais(x, posicao_final), animais_movidos))
    return m


def simula_ecossistema(f, g, v):
    '''
    simula_ecossistema: str X int X booleano -> tuplo
    É a função principal que permite simular o ecossistema de um prado. A função
    recebe uma cadeia de caracteres f correspondente ao nome do ficheiro de 
    configuração da simulação, um valor inteiro g correspondente ao número de
    gerações a simular e um valor booleano v que ativa o modo verboso (True) ou
    o modo quiet (False); e devolve um tuplo de dois elementos correspondentes
    ao número de predadores e presas no prado no fim da simulação.
    '''
    def saida_standard(m, gen):
        '''
        saida_standard: prado X int ->
        Esta função recebe um prado m e um inteiro gen correspondente ao número
        da geração; e mostra o prado, o número de animais e o número da geração
        pela saída standard.
        '''
        print('Predadores: {} vs Presas: {} (Gen. {})'.format\
            (obter_numero_predadores(m), obter_numero_presas(m), gen))
        print(prado_para_str(m))


    ficheiro = open(f, 'r')
    linhas = list(map(lambda x: eval(x[:len(x) - 1]), ficheiro.readlines()))
    ficheiro.close()
    rochedos = animais = posicoes = ()
    for posicao in linhas[1]:
        rochedos += (cria_posicao(posicao[0], posicao[1]),)
    for linha in linhas[2:]:
        animais += (cria_animal(linha[0], linha[1], linha[2]),)
        posicoes += (cria_posicao(linha[3][0], linha[3][1]),)
    prado = cria_prado(cria_posicao(linhas[0][0], linhas[0][1]), rochedos, \
                       animais, posicoes)
    saida_standard(prado, 0)
    tuplo = (obter_numero_predadores(prado), obter_numero_presas(prado))
    if v:
        for gen in range(1, g + 1):
            prado = geracao(prado)
            if obter_numero_predadores(prado) != tuplo[0] or \
               obter_numero_presas(prado) != tuplo[1]:
                saida_standard(prado, gen)
                tuplo = (obter_numero_predadores(prado), obter_numero_presas(prado))         
    else:
        for gen in range(1, g + 1):
            prado = geracao(prado)
        saida_standard(prado, gen)
        tuplo = (obter_numero_predadores(prado), obter_numero_presas(prado))
    return tuplo
