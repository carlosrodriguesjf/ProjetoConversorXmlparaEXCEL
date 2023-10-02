# PROJETO MANIPULADOR DE NOTAS FISCAIS


import xmltodict
import os
import json


def pegar_infos(nome_arquivo):
    with open(f'nfs\\{nome_arquivo}', 'rb') as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        
        # print(json.dumps(dic_arquivo, indent=5))
        # print(10*'-')
        try:
            if 'Nfse' in dic_arquivo:
                infos_nf = dic_arquivo['Nfse']['InfNfse']
            else: 
                infos_nf = dic_arquivo['CompNfse']['Nfse']['InfNfse']
            numero_nota = infos_nf['Numero']
            print(f'Número da nota: {numero_nota}')
            emissor_nota = infos_nf['PrestadorServico']['RazaoSocial']
            print(f'Emissor da nota: {emissor_nota}')
            endereço_empresa = infos_nf['PrestadorServico']['Endereco']
            logradouro = endereço_empresa['Endereco']
            numero = endereço_empresa['Numero']  
            complemento = endereço_empresa['Complemento']
            bairro = endereço_empresa['Bairro']
            estado = endereço_empresa['Uf']
            print(f'Endereço: {logradouro}, {numero} - {complemento} - {bairro} - {estado}')

            nome_cliente = infos_nf['TomadorServico']['RazaoSocial']
            print(f'Nome cliente: {nome_cliente}')
        
        except Exception as erro:
            
            print(erro)
            print(json.dumps(dic_arquivo, indent=5))


lista_arquivos = os.listdir('nfs')

for arquivo in lista_arquivos:
    pegar_infos(arquivo)
    print('')
    print('*-----------------*')
    print('')

