def intercambia(a,b):
    aux = a
    a = b
    b = aux
    return a, b

def ordena(lista):
    for pivote in range(0, len(lista)-1):
        for buscador in range(pivote+1, len(lista)):
            if lista[pivote]<lista[buscador]:
                lista[pivote], lista[buscador] = intercambia(lista[pivote],lista[buscador])
            else:
                pass