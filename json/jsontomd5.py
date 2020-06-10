import json
import hashlib


def ler_json(file_name: str):
    '''
    Ler json e armazenar na memoria
    :param file_name: Nome do arquivo json
    :return: Retorna um dict com os dados do json
    '''
    data = {}
    with open(file_name+'.json', 'r') as f:
        data = json.load(f)
        f.close()
        return data


def cria_dict(linha: str):
    dicionario = {}
    dicionario['ID'] = linha[linha.find("conn")+4:linha.find("]")]
    dicionario['DATA'] = linha[:10]
    dicionario['HORA'] = linha[11:19]
    dicionario['BANCO'] = ""
    dicionario['IP'] = ""
    dicionario['AMDHM'] = linha[:16].replace("-","").replace(":","").replace("T","")






    if dicionario['ID'] != "":
        # Se ID = Nulo, significa que NETWORK não possuí [conn#####]
        return dicionario
    else:
        del dicionario



lista_md5 = []
lista_acessos = []
dados_json = ler_json('log')


for chave, valor in dados_json.items():
    if chave == 'log':
        while True:
            for i in range(300): # MUDA AQUIIII PRA TESTARRRR MULHEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR <------------
                string_md5 = (hashlib.md5(valor[i].encode())).hexdigest()
                '''Cria o md5 de todas as linha do JSON. ".encode()" cria o 
                md5 e o "hexdigest" converte para string hexadecimal'''
                if string_md5 in lista_md5:
                    continue
                else:
                    lista_md5.append(string_md5)
                    if "NETWORK" in valor[i]:
                        dict_network = cria_dict(valor[i])
                        if dict_network!= None:
                            lista_acessos.append(cria_dict(valor[i]))
            break


print(lista_md5)
for i in lista_acessos:
    print(i, end="\n")