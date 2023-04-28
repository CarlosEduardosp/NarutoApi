from src.infra.config import DBConnectionHandler, Base
from src.infra.entities import users, Users

db_conn = DBConnectionHandler()
engine = db_conn.get_engine()
Base.metadata.create_all(engine)
