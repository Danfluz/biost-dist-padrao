import math
from valorestabela import pegacoordenada, pegavalor

#Finalizado!

media = 159.2
desviopadrao = 40.8 # se ao invés da variância, a questão der o desvio padrão, multiplique o valor por ele mesmo, ex: 8*8.
variancia = desviopadrao*desviopadrao # multiplicador. inutilize esta linha se usar a multiplicação acima
raizvariancia = math.sqrt(variancia)

print('Atenção. Usar esta versão apenas para média e variancia diferentes de 0 e 1!')
print('')
# media = float(input('Digite a média (µ): ').replace(',','.'))
# variancia = float(input('Digite a variancia (σ): ').replace(',','.'))

modelo = input('Escolha um modelo de questão\n\n'
               '1. P(6 < X < 12) = ?\n'
               '2. P(X > k) = 0,05\n'
               '3. P(X < k) = 0,05\n'
               '4. P(X > 55) = ?\n'
               '5. P(X < 55) = ?\n\n'
               'Resposta: ')
# modelo = '5'



if modelo == '2':
    probabilidade = float(input('Digite o valor da probabilidade dado pela questão: ').replace(',','.'))
    probabilidade = round(probabilidade, 4)
    complementar = 1-probabilidade
    if str(complementar).endswith('5'):
        if complementar > 0:
            complementar = complementar + 0.00001
            complementar = round(complementar, 4)
        elif complementar < 0:
            complementar = complementar - 0.00001
            complementar = round(complementar, 4)
    else:
        complementar = round(complementar, 4)

    try:
        coordtabela = pegacoordenada(f'{complementar:.4f}'.replace('.',','))
    except:
        coordtabela = float(input(f'Digite a COORDENADA na tabela para o valor mais próximo de {complementar:.4f}: ').replace(',', '.'))

    print('')
    print(f'P((X - {media} / {raizvariancia}) > (k - {media} / {raizvariancia}) = ')
    print(f'= P(X > (k - {media} / {raizvariancia})) = {probabilidade}')
    print('')
    print(f'Vamos chamar a expressão: (k - {media} / {raizvariancia}), de "z".')
    print('')
    print(f'Então se P(X > k) = {probabilidade}, seu complementar é 1 - {probabilidade} = {complementar}.')
    print(f'Pela tabela, z = {coordtabela}.')
    print(f'Logo, k = {coordtabela} * {raizvariancia} + {media} = {coordtabela*raizvariancia+media:.4f}')

if modelo == '1':
    print('')
    t1 = float(input('Digite o numero à esquerda de X: ').replace(',', '.'))
    t2 = float(input('Digite o numero à direita de X: ').replace(',', '.'))

    pt1 = (t1 - media) / raizvariancia
    pt2 = (t2 - media) / raizvariancia

    try:
        zt1 = f'{pt1:.2f}'.replace('.',',')
        zt1 = pegavalor(zt1)
        zt2 = f'{pt2:.2f}'.replace('.',',')
        zt2 = pegavalor(zt2)
    except:
        zt1 = float(input(f'Digite o VALOR na tabela da coordenada {pt1}: ').replace(',', '.'))
        zt2 = float(input(f'Digite o VALOR na tabela da coordenada {pt2}: ').replace(',', '.'))

    print('')
    print(f'P({t1} < X < {t2}) = P(({t1} - {media} / {raizvariancia}) < (X - {media} / {raizvariancia}) < ({t2} - {media} / {raizvariancia}))')
    print(f'= P({pt1} < X < {pt2}) = ')
    print(f'= P(X < {pt1}) - P(X < {pt2}) =')
    print(f'Resposta: {zt2} - {zt1} = {zt2 - zt1:.4f}')

if modelo == '3':
    probabilidade = float(input('Digite o valor da probabilidade dado pela questão: ').replace(',', '.'))
    try:
        coordtabela = pegacoordenada(f'{probabilidade:.4f}'.replace('.',','))
    except:
        coordtabela = float(input(f'Digite a COORDENADA na tabela para o valor mais próximo de {probabilidade:.4f}: ').replace(',', '.'))

    print('')
    print(f'P(X < k) = {probabilidade} = P((X - {media} / {raizvariancia}) < k - {media} / {raizvariancia}) = ')
    print(f'P(X < (k - {media} / {raizvariancia}) = {probabilidade}')
    print('')
    print(f'Vamos chamar a expressão: (k - {media} / {raizvariancia}), de "z".')
    print('')
    print(f'Pela tabela, z = {coordtabela}.')
    print(f'Logo, k = {coordtabela} * {raizvariancia} + {media} = {coordtabela*raizvariancia+media}')

if modelo == '4':

    t1 = float(input('Digite o numero à direita de X: ').replace(',', '.'))
    postabela = (t1 - media) / raizvariancia
    if str(postabela).endswith('5'):
        if postabela < 0:
            postabela = postabela - 0.0001
            postabela = round(postabela, 2)
        elif postabela > 0:
            postabela = postabela + 0.0001
            postabela = round(postabela, 2)
    try:
        coordtabela = pegavalor(f'{postabela:.2f}'.replace('.',','))
    except:
        coordtabela = float(input(f'Informe o VALOR da coordenada mais próxima a {postabela}: ').replace(',', '.'))
    complementar = 1-coordtabela
    print('')
    print(f'P(X > {t1}) = P(X > ({t1} - {media} / {raizvariancia})) = P(X > {postabela})')
    print(f'Resposta: 1 - {coordtabela:.4f} = {complementar:.4f}')

if modelo == '5':

    t1 = float(input('Digite o numero à direita de X: ').replace(',', '.'))
    postabela = (t1 - media) / raizvariancia
    print(postabela)
    if str(postabela).endswith('5'):
        if postabela < 0:
            postabela = postabela - 0.0001
            postabela = round(postabela, 2)
        elif postabela > 0:
            postabela = postabela + 0.0001
            postabela = round(postabela, 2)
    else:
        pass
    try:
        coordtabela = pegavalor(f'{postabela:.2f}'.replace('.',','))
    except:
        coordtabela = float(input(f'Informe o VALOR da coordenada mais próxima a {postabela}: ').replace(',', '.'))
    print('')
    print(f'P(X < {t1}) = P(X < ({t1} - {media} / {raizvariancia})) = P(X < {postabela:.2f})')
    print(f'Resposta: P(X < {postabela:.2f}) = {coordtabela}')