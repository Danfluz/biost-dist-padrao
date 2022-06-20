from valorestabela import pegavalor, pegacoordenada
media = '0'
variancia = '1'
descobrir = False


entre = False
desprobabilidade = input('Descobrir termo? ').upper()
if desprobabilidade.startswith('S'):
    descobrir = True
    probabilidade = float(input('Digite o valor da probabilidade dado pela questão: ').replace(',', '.'))

sinal = input('Calcular maior (>), menor (<) ou "entre posições"?\nResposta: ').upper()
if sinal.startswith(('MAI', '>')):
    sinal = '>'
if sinal.startswith(('MEN', '<')):
    sinal = '<'
if sinal.startswith('ENT') and descobrir == False:
    entre = True
    termo1 = float(input('Digite o numero à esquerda de Z: ').replace(',', '.'))
    termo2 = float(input('Digite o numero à direita de Z: ').replace(',', '.'))
    if termo2 > termo1:
        sinal = '<'
    elif termo1 > termo2:
        sinal = '>'

if sinal.startswith('ENT') and descobrir == True:
    entre = True
    termo1 = input('Digite o numero à esquerda de Z: ').replace(',', '.')
    termo2 = input('Digite o numero à direita de Z: ').replace(',', '.')
    try:
        termo1 = float(termo1)
    except:
        pass
    try:
        termo2 = float(termo2)
    except:
        pass
    # sinal = input('Digite o sinal da questão (<) ou (>): ')
    sinal = '<'
    if type(termo1) == str and type(termo2) == str:
        try:
            endcresp = pegacoordenada(f'{(1-probabilidade)/2:.4f}'.replace('.', ','))
        except:
            endcresp = input(f'Digite a COORDENADA que contém o valor mais próximo de {1-(1-probabilidade)/2:.4f}: ')

        print('')
        print(f'P({termo1} {sinal} Z {sinal} {termo2}) = {probabilidade}')
        print(f'1 - {probabilidade} = {1-probabilidade:.4f}')
        print(f'A curva é simétrica, logo, z = ({1-probabilidade:.4f} / 2) = {(1-probabilidade)/2:.4f}')
        print(f'Resposta: P(Z < {(1-probabilidade)/2:.4f}) = {endcresp}')

    if type(termo1) == float:
        try:
            areatermo1 = pegavalor(f'{termo1:.2f}'.replace('.', ','))
        except:
            areatermo1 = float(input(f'Digite o valor mais próximo na tabela para {termo1}: ').replace(',','.'))
        z = probabilidade + areatermo1
        try:
            zresp = pegacoordenada(f'{z:.4f}'.replace('.', ','))
        except:
            zresp = input(f'Digite as coordenadas para o valor mais próximo de {z:.4f}: ')

        print('')
        print(f'Resposta: z = {zresp}, pois:')
        print(f'P(Z {sinal} z) = {areatermo1} + {probabilidade} = {areatermo1+probabilidade} (pela tabela, z = {zresp})')
        print(f'P({termo1} {sinal} Z {sinal} {zresp}) = {probabilidade}')



if descobrir == False and entre == False:
    z = input('Digite o valor (z) que deseja encontrar: ')
    z = float(z.replace(',','.'))
if descobrir == True and entre == False:
    if sinal == '<':
        try:
            z = pegacoordenada(f'{probabilidade:.4f}')
        except:
            z = input(f'Digite a COORDENADA na tabela que contém o valor mais próximo de {probabilidade:.4f}: ')
            z = float(z.replace(',', '.'))
    if sinal == '>':
        try:
            z = pegacoordenada(f'{1-probabilidade:.4f}')
        except:
            z = input(f'Digite a COORDENADA na tabela que contém o valor mais próximo de {1-probabilidade:.4f}: ')
            z = float(z.replace(',', '.'))

if descobrir == False and entre == False:
    if sinal == '>':
        try:
            z = f'{z:.2f}'.replace('.', ',')
            if float(z.replace(',','.')) > 0:
                area = pegavalor(f'-{z}')
            elif float(z.replace(',','.')) < 0:
                area = pegavalor(f'{z}')
        except:
            if float(z.replace(',','.')) > 0:
                area = float(input(f'Digite a área encontrada na tabela para -{z}: ').replace(',', '.'))
            elif float(z.replace(',','.')) < 0:
                area = float(input(f'Digite a área encontrada na tabela para {z}: ').replace(',', '.'))
    elif sinal == '<':
        try:
            z=f'{z:.2f}'.replace('.',',')
            area = pegavalor(z)
        except:
            area = float(input(f'Digite a área encontrada na tabela para {z}: ').replace(',', '.'))

    print('')
    if sinal == '<':
        print(f'Resposta: P(Z {sinal} {z}) = 1 - {area:.4f} = {1-area:.4f}')
    elif sinal == '>':
        print(f'Resposta: P(Z {sinal} {z}) = {area:.4f}')

if entre == True and descobrir == False:
    try:
        areatermo1 = pegavalor(f'{termo1:.2f}'.replace('.',','))
    except:
        areatermo1 = float(input(f'Digite a área encontrada para {termo1}: ').replace(',', '.'))
    try:
        areatermo2 = pegavalor(f'{termo2:.2f}'.replace('.',','))
    except:
        areatermo2 = float(input(f'Digite a área encontrada para {termo2}: ').replace(',', '.'))
    print('')

    if sinal == '<':
        print('Cálculo:')
        print(f'P({termo1} {sinal} Z {sinal} {termo2}) = P(Z < {termo2}) - P(Z < {termo1})')
        print(f'P({termo1} {sinal} Z {sinal} {termo2}) = {areatermo2} - {areatermo1} = {areatermo2-areatermo1:.4f}')


if entre == False and descobrir == True:
    print('')
    print(f'Resposta: z = {z}, pois:')
    print(f'P(Z {sinal} {z}) = {probabilidade}')

