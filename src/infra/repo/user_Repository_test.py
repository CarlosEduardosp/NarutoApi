from sqlalchemy import text
from src.infra.config import DBConnectionHandler, Base
from src.infra.entities import users, Users
from src.infra.repo import UserRepository
from faker import Faker

faker = Faker()
db_connection_handler = DBConnectionHandler()


def test_insert():
    name = faker.name()
    resumo = faker.word()
    vila = faker.word()
    ninja = faker.word()
    tecnicas = faker.word()
    url = faker.word()

    some = UserRepository()
    result = some.insert_user(name, resumo, ninja, vila, tecnicas, url)


def test_select_user():
    """Select in users"""

    engine = db_connection_handler.get_engine()

    with engine.connect() as connection:
        # select data in users
        query_user = connection.execute(text(f"SELECT * FROM users;"))

    for i in query_user:
        print(i.name, i.tecnicas)


def test_delete_user():
    """deleting data in users"""

    engine = db_connection_handler.get_engine()

    """ deleting data of select in users """
    with engine.connect() as connection:
        connection.execute(text(f"DELETE FROM users WHERE id={1} ;"))
        connection.commit()
