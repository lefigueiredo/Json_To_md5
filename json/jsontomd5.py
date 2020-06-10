import json
import hashlib


def ler_json(file_name: str):
    """
    Ler json e armazenar na memoria
    :param file_name: Nome do arquivo json
    :return: Retorna um dict com os dados do json
    """
    with open(file_name+'.json', 'r') as f:
        data = json.load(f)
        f.close()
        return data


def cria_dict(linha: str):
    dicionario = {
        'ID': linha[linha.find("conn")+4: linha.find("]")],
        'DATA': linha[:10],
        'HORA': linha[11:19],
        'BANCO': "",
        'IP': "",
        'AMDHM': linha[:16].replace("-", "").replace(":", "").replace("T", "")
    }

    if "metadata from" in linha:
        dicionario['IP'] = linha[linha.find("metadata from")+14: linha.find(":")]

    # Tratamento dos itens da lista de acessos
    if dicionario['ID'] != "":
        # Se ID = None, significa que NETWORK não possuí [conn#####]
        return dicionario
    else:
        del dicionario


lista_md5 = []
lista_acessos = []
dados_json = ler_json('log')

for chave, valor in dados_json.items():
    if chave == 'log':
        while True:
            for i in range(50): # MUDA AQUIIII PRA TESTARRRR MULHEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR <------------
                string_md5 = (hashlib.md5(valor[i].encode())).hexdigest()
                '''Cria o md5 de todas as linha do JSON. ".encode()" cria o 
                md5 e o "hexdigest" converte para string hexadecimal'''
                if string_md5 in lista_md5:
                    continue
                else:
                    lista_md5.append(string_md5)
                    if "NETWORK" in valor[i]:
                        dict_network = cria_dict(valor[i])
                        if dict_network is not None:
                            lista_acessos.append(cria_dict(valor[i]))
            break


print(lista_md5)
for i in lista_acessos:
    print(i, end="\n")
