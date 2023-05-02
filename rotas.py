from fastapi import APIRouter
from functions import incluir_no_banco
from src.infra.repo.user_Repository import UserRepository
from src.infra.config import DBConnectionHandler, Base
import random


router = APIRouter()

# criando o banco de dados.
db_conn = DBConnectionHandler()
engine = db_conn.get_engine()
Base.metadata.create_all(engine)

# incluindo dados do beautifulsoup no banco
incluir_no_banco()

""" instancia do repositório user"""
some = UserRepository()


@router.get("/")
def todos_os_personagens():
    """Todos os 70 ninjas disponíveis na Api Naruto.
    Realiza a consulta de dados no banco, ou se o banco estiver vazio,
    realiza a raspagem de dados no site original"""

    # consultando banco de dados
    query_user = some.select_user()

    # verificando se o banco está completo ou vazio
    if query_user:
        personagens = []
        for personagem in query_user:
            personagens.append(personagem)

        return {"Todos Os Personagens": personagens}

    # condição para caso o banco esteja vazio
    else:
        try:
            # incluindo dados no banco
            incluir_no_banco()

            # retornando os dados salvos.
            query_user = some.select_user()
            personagens = []
            for personagem in query_user:
                personagens.append(personagem)

            return {"Todos Os Personagens": personagens}

        # caso exista algum problema, o retorno será "Algo deu Errado, verifique com o Desenvolvedor da API."
        except:
            return "Algo deu Errado, verifique com o Desenvolvedor da API."


@router.get("/akatsuki")
def todos_da_akatsuki():
    """Todos os personagens da Akatsuki reunidos em um link."""

    membros_akatsuki = []
    lista = [19, 29, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 60]

    query_user = some.select_user()

    for personagem in query_user:
        for i in lista:
            if personagem["id"] == i:
                membros_akatsuki.append(personagem)

    return {"Todos os ninjas da Akatsuki": membros_akatsuki}


@router.get("/hokages")
def todos_os_hokages():
    """Todos os Hokages reunidos em um link."""

    hokages = []
    lista = [1, 4, 6, 20, 30, 32, 33]

    query_user = some.select_user()

    for personagem in query_user:
        for i in lista:
            if personagem["id"] == i:
                hokages.append(personagem)

    return {"Todos os Hokages": hokages}


@router.get("/classico")
def ninjas_do_classico():
    """Todos os ninjas crianças da série naruto classica."""

    criancas = []
    lista = [1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15, 16, 21, 25, 26, 27]

    query_user = some.select_user()

    for personagem in query_user:
        for i in lista:
            if personagem["id"] == i:
                criancas.append(personagem)

    return {"Crianças ninjas do clássico": criancas}


@router.get("/sortear")
def sortear_um_personagem():
    """Realiza o sorteio de um personagem dentre todos os personagens"""

    query_user = some.select_user()

    sorteio = random.randint(0, 70)

    for personagem in query_user:
        if sorteio == personagem["id"]:
            sorteado = personagem

    return sorteado
