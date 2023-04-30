from fastapi import APIRouter
from functions import find
from src.infra.repo.user_Repository import UserRepository


router = APIRouter()
some = UserRepository()


@router.get("/")
def find_all():
    query_user = some.select_user()

    if query_user:
        personagens = []
        for personagem in query_user:
            personagens.append(personagem)

        return {"Todos Os Personagens": personagens}

    else:
        try:
            result = find()
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

            query_user = some.select_user()
            personagens = []
            for personagem in query_user:
                personagens.append(personagem)

            return {"Todos Os Personagens": personagens}

        except:
            return "Algo deu errado"
