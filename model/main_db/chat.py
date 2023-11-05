from sqlalchemy import Column, Integer, Boolean

from database.main_db.database import Base


class Admin(Base):
    __tablename__ = 'chat'

    chat_id = Column(Integer, primary_key=True)

    def __repr__(self) -> str:
        return f'Chat [ID: {self.chat_id}]'
