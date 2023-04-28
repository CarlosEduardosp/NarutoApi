# pylint: disable=E1101

from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


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
