import pandas

data = pandas.read_excel("tabelanormal1.xlsx")
df = pandas.DataFrame(data)
df = df.reset_index()

def pegavalor(coordenada1):

    final = coordenada1[-1]
    if coordenada1[0] == '-':
        coordenada1 = 'b' + coordenada1[0:4]
    else:
        coordenada1 = 'b' + coordenada1[0:3]
    final = 'a0,0' + final

    for index, row in df.iterrows():
        if row['z'] == coordenada1:
            return row[final]


def pegacoordenada(valor):
    valor = valor.replace(',','.')
    valor = float(valor)
    contador = 0

    while contador <10:
        coluna = 'a0,0' + str(contador)
        for index, row in df.iterrows():
            if row[coluna] == valor:
                coordenada2 = row['z'][1:] + coluna[-1]
                coordenada2 = coordenada2.replace(',','.')
                coordenada2 = float(coordenada2)
        contador += 1

    return coordenada2