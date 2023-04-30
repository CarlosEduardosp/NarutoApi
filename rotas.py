from fastapi import APIRouter
from functions import find
from src.infra.repo.user_Repository import UserRepository
from src.infra.config import DBConnectionHandler, Base


db_conn = DBConnectionHandler()
engine = db_conn.get_engine()
Base.metadata.create_all(engine)

router = APIRouter()

""" instancia do repositório user"""
some = UserRepository()


@router.get("/")
def find_all():
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
            # realizando a raspagem de dados no site original, com as funções de functions.py
            result = find()

            # adicionando os dados da raspagem no banco de dados
            for personagem in result:
                if personagem["id"] != 28 and personagem["id"] < 32:
                    nivel = personagem["Detalhes"]["Nível Ninja"]
                    vila = personagem["Detalhes"]["Vila Ninja"]
                    tecnicas = personagem["Detalhes"]["Pincipais Técnicas"]

                    some.insert_user(
                        personagem["Nome"],
                        personagem["Resumo"],
                        nivel,
                        vila,
                        tecnicas,
                        personagem["Url_imagem"],
                    )
                else:
                    nivel = "Não disponível !!"
                    vila = "Não disponível !!"
                    tecnicas = "Não disponível !!"

                    some.insert_user(
                        personagem["Nome"],
                        personagem["Resumo"],
                        nivel,
                        vila,
                        tecnicas,
                        personagem["Url_imagem"],
                    )

            # retornando os dados salvos.
            query_user = some.select_user()
            personagens = []
            for personagem in query_user:
                personagens.append(personagem)

            return {"Todos Os Personagens": personagens}

        # caso exista algum problema, o retorno será "Algo deu Errado, verifique com o Desenvolvedor da API."
        except:
            return "Algo deu Errado, verifique com o Desenvolvedor da API."


@router.get("/konoha")
def todos_de_konoha():
    return {"Todos os ninjas de Konoha": "Disponível em Breve..."}


@router.get("/akatsuki")
def todos_da_akatsuki():
    return {"Todos os ninjas da Akatsuki": "Disponível em Breve..."}
