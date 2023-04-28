# pylint: disable=E1101
from sqlalchemy import text
from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


class UserRepository:
    """Class to manage User Repository"""

    @classmethod
    def insert_user(
        cls, name: str, resumo: str, nivel: str, vila: str, tecnicas: str, url: str
    ) -> Users:
        """Insert data in user entity
        :param - name - person name
               - password
        :return - tuple with new user inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(
                    name=name,
                    resumo=resumo,
                    nivel=nivel,
                    vila=vila,
                    tecnicas=tecnicas,
                    url=url,
                )

                db_connection.session.add(new_user)
                db_connection.session.commit()
                return new_user
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_user(self):
        """Select in users"""
        try:
            with engine.connect() as connection:
                # select data in users
                query_user = connection.execute(text(f"SELECT * FROM users;"))

                lista = []
                for i in query_user:
                    dados = {"nome": i.name, "resumo": i.resumo, "nivel": i.nivel, "vila": i.vila, "tecnicas": i.tecnicas, "url": i.url}
                    lista.append(dados)

                return lista
        except:
            return "erro"

    @classmethod
    def delete_user(cls, id: int):
        """deleting data in users"""

        try:
            """ deleting data of select in users """
            with engine.connect() as connection:
                connection.execute(text(f"DELETE FROM users WHERE id={id} ;"))
                connection.commit()
        except:
            return "erro ao deletar"
