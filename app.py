# PROJETO MANIPULADOR DE NOTAS FISCAIS


import xmltodict
import os


def pegar_infos(nome_arquivo):
    with open(f'nfs/{nome_arquivo}', 'r') as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        print(dic_arquivo)


lista_arquivos = os.listdir('nfs')


for arquivo in lista_arquivos:
    pegar_infos(arquivo)
