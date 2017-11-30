def carregar_medalhas():
    arquivo = open("medalhas.txt", "r")
    medalhas = []
    for l in arquivo:
        l = l.strip()
        v1 = l.find(',')
        v2 = l.find(',',v1+1)
        quantidades = []
        if l[v2+1] == 'o':
            quantidades = [1,0,0]
        elif l[v2+1] == 'p':
            quantidades = [0,1,0]
        else:
            quantidades = [0,0,1]
        medalhas.append([l[:v1], quantidades])
    return medalhas

def busca(lista, elemento, inicio):
    for i in range(inicio, len(lista)):
        if lista[i][0] == elemento:
            return i
    return -1

def calcula_pontos(quantidades):
    pontos = 5
    total = 0
    for i in range(3):
        total += pontos*quantidades[i]
        pontos -= 2
    return total

def mesclar_redundancias(medalhas):
    quadro = []
    for i in range(len(medalhas)):
        if busca(quadro, medalhas[i][0], 0)>0:
            continue
        else:
            escola = medalhas[i][:]
            idx = busca(medalhas, medalhas[i][0], i+1)
            while idx>=0:
                escola[1][0] += medalhas[idx][1][0]
                escola[1][1] += medalhas[idx][1][1]
                escola[1][2] += medalhas[idx][1][2]
                idx = busca(medalhas, medalhas[i][0], idx+1)
            pontos = calcula_pontos(escola[1])
            escola.append(pontos)
            quadro.append(escola)
    return quadro

def atualiza_vencedor(quadro):
    maior_pontuacao = -1
    maior_indice_po = -1
    for i in range(len(quadro)):
        if quadro[i][2]>maior_pontuacao:
            maior_pontuacao = quadro[i][2]
            maior_indice_po = i
    return maior_indice_po

def ordena_quadro(quadro):
    for i in range(len(quadro)):
        for j in range(i,len(quadro)):
            if quadro[j][2]>quadro[i][2]:
                tmp = quadro[i]
                quadro[i] = quadro[j]
                quadro[j] = tmp

def gera_saida_arquivo(quadro):
    arquivo = open("quadro.txt", "w")
    for l in quadro:
        arquivo.write("%-25s %d \t %d \t %d \t %d\n"%(l[0], l[1][0], l[1][1], l[1][2], l[2]))

    v = atualiza_vencedor(quadro)
    arquivo.write("E o vencedor com %d pontos eh %s.\n"%(quadro[v][2], quadro[v][0]))
    arquivo.close()

medalhas = carregar_medalhas()
quadro = mesclar_redundancias(medalhas)
ordena_quadro(quadro)
gera_saida_arquivo(quadro)
import os
os.system("quadro.txt")
