# -*- coding:utf-8 -*-
import aleatorio 
import arquivos as arquivo

seisDezenas = aleatorio.gerarListaInteiro(6, 60)
seisDezenasStr = ''
count = 0

for i in seisDezenas:
    if len(seisDezenas) == count or count == 0:
        seisDezenasStr += str(i)
    else :
        seisDezenasStr += ',' + str(i)

    count += 1

print(seisDezenas)
print(seisDezenasStr)

arquivo.appendDadosArquivo('./sorteados.csv', seisDezenasStr)