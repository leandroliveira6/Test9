# coding=iso-8859-1

def carrega_arquivo():
    arq = open("medalhas.txt","r")
    quadro = []
    for linha in arq:
        tmp = []
        linha = linha.strip()
        virg1 = linha.find(",")
        virg2 = linha.find(",", virg1+1)
        tmp.append(linha[:virg1])
        if linha[virg2+1] == 'o':
            tmp.append([1,0,0])
        elif linha[virg2+1] == 'p':
            tmp.append([0,1,0])
        else:
            tmp.append([0,0,1])
        quadro.append(tmp)
    return quadro

def verifica_quadro(quadro, escola):
    for i in range(len(quadro)):
        if escola in quadro[i]:
            return i
    return -1

def soma_cada_medalha(quadro, escola):
    total_cada_medalha = [0,0,0]
    for linha in quadro:
        if escola in linha:
            for i in range(3):
                total_cada_medalha[i]+=linha[1][i]
    return total_cada_medalha

def remove_redundancias(quadro):
    novo_quadro = []
    for escola in quadro:
        idx = verifica_quadro(novo_quadro, escola[0])
        if idx<0:
            tmp = []
            tmp.append(escola[0])

            total_cada_medalha = soma_cada_medalha(quadro,escola[0])
            str_total_cada_medalha = "{} {} {}".format(total_cada_medalha[0],total_cada_medalha[1],total_cada_medalha[2])
            tmp.append(str_total_cada_medalha)
            
            total_pontuacao = 5*total_cada_medalha[0]+3*total_cada_medalha[1]+total_cada_medalha[2]
            tmp.append(total_pontuacao)
            novo_quadro.append(tmp)
        else:
            continue
            
    return novo_quadro

def busca_vencedor(quadro):
    maior_pontuacao = -1
    maior_indice = -1
    for i in range(len(quadro)):
        if quadro[i][2]>maior_pontuacao:
            maior_pontuacao = quadro[i][2]
            maior_indice = i
            
    return maior_indice

def gerar_arquivo(quadro):
    arq = open("quadro.txt","w")
    for linha in quadro:
        arq.write("{} \t {} \t {}\n".format(linha[0], linha[1], linha[2]))
    vencedor = busca_vencedor(quadro)
    arq.write("O vencedor é o {} com {} pontos.".format(quadro[vencedor][0], quadro[vencedor][2]))
    arq.close()

quadro = carrega_arquivo()
quadro = remove_redundancias(quadro)
gerar_arquivo(quadro)

import os
os.system("quadro.txt")