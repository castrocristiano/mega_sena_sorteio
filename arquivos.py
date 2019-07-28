# -*- coding:utf-8 -*-

def lerArquivo(path):
    arquivo = open(path)
    return arquivo

def salvarNovoArquivo(path, dados):
    arquivo = open(path, 'w+')
    arquivo.write(dados)
    arquivo.write('\n')
    arquivo.close()

def appendDadosArquivo(path, dados):
    arquivo = open(path, 'a+')
    arquivo.write(dados)
    arquivo.write('\n')
    arquivo.close()