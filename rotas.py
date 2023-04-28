from fastapi import APIRouter
from functions import find
from src.infra.repo.user_Repository import UserRepository


router = APIRouter()
some = UserRepository()


@router.get("/")
def find_all():
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
            nivel = "Nada"
            vila = "Nada"
            tecnicas = "Nada"

            some.insert_user(
                personagem["Nome"],
                personagem["Resumo"],
                nivel,
                vila,
                tecnicas,
                personagem["Url_imagem"],
            )

    return result
