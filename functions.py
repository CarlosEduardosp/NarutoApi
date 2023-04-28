import requests
from bs4 import BeautifulSoup


def get_soup():
    """faz a requisição e retorna a variável soup"""

    page = requests.get(
        "https://criticalhits.com.br/anime/naruto-shippuden-os-70-personagens-principais-da-historia/"
    )

    soup = BeautifulSoup(page.content, "html.parser")

    return soup


def nomes_personagens():
    """Envia uma lista com todos os nomes dos personagens."""

    soup = get_soup()

    nome_personagem = soup.find_all("h3")
    nome_personagem.pop(71)
    nome_personagem.pop(70)

    return nome_personagem


def lista_imagens():
    """envia uma lista com todas as url de imagens dos personagens."""

    soup = get_soup()

    imagem = soup.find_all("amp-img")
    list_imagens = []
    for link in imagem:
        data = link.get("src")
        list_imagens.append(data)

    imagens = []
    cont = 2
    for i in range(len(list_imagens)):
        if cont < 158:
            imagens.append(list_imagens[cont])
            cont += 2

    for i in range(8):
        imagens.pop(-1)

    return imagens


def acertando_dados(list_descricao):
    """concatenando descrição do mesmo personagem, depois deletando as separadas,
    e inserindo novamente na lista a mensagem concatenada."""

    num_lista = [14, 32, 36, 45, 46, 48]

    for i in num_lista:
        x = i + 1
        num_lista_editar = list_descricao[i] + list_descricao[x]
        list_descricao.pop(i)
        list_descricao.pop(i)
        list_descricao.insert(i, num_lista_editar)

    return list_descricao


def lista_descricao():
    soup = get_soup()
    descricao = soup.find_all("p")

    list_descricao = []
    cont = 0
    for i in descricao:
        if 3 <= cont <= 78:
            dados = i.text
            list_descricao.append(dados)
        cont += 1

    """concatenando descrição do mesmo personagem, depois deletando as separadas,
     e inserindo novamente na lista a mensagem concatenada."""

    list_descricao = acertando_dados(list_descricao)

    return list_descricao


def information():
    soup = get_soup()

    information = soup.find_all("li")

    list_info = []
    cont = 21
    for i in range(len(information)):
        if 112 > i > 21:
            if i > cont:
                dic = {
                    "Nível Ninja": information[i].text,
                    "Vila Ninja": information[i + 1].text,
                    "Pincipais Técnicas": information[i + 2].text,
                }
                list_info.append(dic)
                cont = i + 2

    return list_info


def find():
    nome_personagem = nomes_personagens()
    list_descricao = lista_descricao()
    imagens = lista_imagens()
    list_info = information()

    list_nomes = []
    cont = id = contador = 0
    for nome in nome_personagem:
        if nome.text != "Kurama":
            if "Post" not in nome.text:
                if cont <= 29:
                    dados = {
                        "id": id + 1,
                        "Nome": nome.text,
                        "Resumo": list_descricao[id],
                        "Detalhes": list_info[cont],
                        "Url_imagem": imagens[contador],
                    }
                    list_nomes.append(dados)
                    cont += 1
                    id += 1
                    contador += 1
                else:
                    dados = {
                        "id": id + 1,
                        "Nome": nome.text,
                        "Resumo": list_descricao[id],
                        "Url_imagem": imagens[contador],
                    }
                    list_nomes.append(dados)
                    cont += 1
                    id += 1
                    contador += 1

        elif nome.text == "Kurama":
            dados = {
                "id": id + 1,
                "Nome": nome.text,
                "Resumo": list_descricao[id],
                "Url_imagem": imagens[contador],
            }
            list_nomes.append(dados)
            id += 1
            contador += 1

    return list_nomes
