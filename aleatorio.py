# -*- coding:utf-8 -*-
import random

def gerarListaInteiro(tam, max):
    lista = []
    for i in range(0, tam):
        aleatorio = random.randint(1 , max)

        while lista.count(aleatorio) >= 1:
            aleatorio = random.randint(1 , max)
            
        lista.append(aleatorio)
        
    return sorted(lista)


