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


lista_md5 = []
dados_json = ler_json('log')


for chave, valor in dados_json.items():
    if chave == 'log':
        while True:
            for i in range(len(chave)): # MUDA AQUIIII PRA TESTARRRR MULHEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR <------------
                string_md5 = (hashlib.md5(valor[i].encode())).hexdigest()
                '''Cria o md5 de todas as linha do JSON. ".encode()" cria o 
                md5 e o "hexdigest" converte para string hexadecimal'''
                if string_md5 in lista_md5:
                    continue
                else:
                    lista_md5.append(string_md5)
            break
