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
    """
    Cria o dicionário individual para cada acesso em NETWORK
    :param linha: Linha do Json que está sendo lido
    :return: Retorna o dicionário do acesso
    """
    dicionario = {
        'ID': linha[linha.find("conn") + 4: linha.find("]")],
        'DATA': linha[:10],
        'HORA': linha[11:19],
        'BANCO': [],
        'IP': "",
        'AMDHM': linha[:16].replace("-", "").replace(":", "").replace("T", "")
    }

    # =~=~= Identificação do IP
    if "metadata from" in linha:    # NETWORKs tipo 1
        dicionario['IP'] = linha[linha.find("from") + 5: linha.find(":", 20, 150)]
        # Procura o valor no intervalo que vai de "from" até o primeiro ":"

    elif "end connection" in linha:    # NETWORKs tipo 2
        dicionario['IP'] = linha[linha.find("connection") + 11: linha.find(":", 20, 100)]
        # Procura o valor no intervalo que vai de "connection" até o primeiro ":"

    # =~=~= Tratamento dos itens da lista de acessos
    if dicionario['ID'] != "":
        # Se ID = None, significa que NETWORK não possuí [conn#####]
        return dicionario
    else:
        del dicionario


def achar_bancos(bancos: list, linha: str):
    """
    Verifica se o banco está na linha do JSON e retorna a sigla do banco
    :param bancos: Lista com siglas dos bancos
    :param linha: Linha do JSON lida
    :return: Retorna a sigla do banco
    """
    for banco in bancos:
        banco += "."
        if banco in linha:
            return banco.replace(".", "")


bancos_existentes = ['AL', 'ANA', 'ANAC', 'ANATEL', 'ANEEL', 'ANP', 'ANS',
                     'BCB', 'BNDES', 'BRASILEIRA_UNILAB', 'CAGED', 'CAPES',
                     'DISTRITO_FEDERAL', 'FGV', 'IBAMA', 'IBGE_NACIONAL',
                     'IBGE', 'IFAL', 'IFC', 'IFFAR', 'IFMG', 'IFS', 'INEP',
                     'INPI', 'JBRJ', 'JOBS', 'MAPA', 'MCTIC', 'MDIC', 'MDM',
                     'MDS', 'ME', 'MEC', 'MF', 'MINISTERIO_DA_INFRAESTRUTURA',
                     'MIN_C', 'MJ', 'MS', 'PNUD', 'PREVIDENCIA_SOCIAL',
                     'RAIS', 'RECEITA_FEDERAL', 'TESOURO_NACIONAL', 'UFCA',
                     'UFOP', 'UFPI', 'UFRN', 'UFRR', 'UF_PEL']
lista_md5 = []
lista_acessos = []
dados_json = ler_json('log')
teste = []

# Manipulação do JSON para NETWORK
for chave, valor in dados_json.items():
    if chave == 'log':
        while True:
            for i in range(len(valor)):
                string_md5 = (hashlib.md5(valor[i].encode())).hexdigest()
                '''Cria o md5 de todas as linha do JSON. ".encode()" cria o 
                md5 e o "hexdigest" converte para string hexadecimal'''

                if string_md5 in lista_md5:
                    continue
                else:
                    lista_md5.append(string_md5)
                    if "NETWORK" in valor[i]:
                        dict_network = cria_dict(valor[i])
                        # Cria o dict de todos os NETWORKs

                        if dict_network is not None:
                            lista_acessos.append(cria_dict(valor[i]))
                            # Adiciona na lista somente os dict com dados
                            # TIRAR OS NETWORKS REPITIDOS
            break

# Manipulação do JSON para uso de ID
for chave, valor in dados_json.items():
    if chave == 'log':
        while True:
            for ids in lista_acessos:
                for i in range(len(valor)):
                    if ids["ID"] in valor[i]:
                        if valor[i] in lista_acessos:
                            teste.append(ids["ID"] )
            break


print(lista_md5)
for i in lista_acessos:
    print(i, end="\n")
print(len(lista_acessos))
print(teste)