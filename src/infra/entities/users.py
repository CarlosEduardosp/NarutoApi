from sqlalchemy import Column, String, Integer
from src.infra.config import Base
from sqlalchemy.orm import relationship


class Users(Base):
    """Users Entity"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    resumo = Column(String, nullable=False)
    nivel = Column(String, nullable=False)
    vila = Column(String, nullable=False)
    tecnicas = Column(String, nullable=False)
    url = Column(String, nullable=False)

    def __rep__(self):
        return f"Usr [name={self.name}]"
