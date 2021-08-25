from .base import Base
from sqlalchemy import Column, BigInteger, String, Boolean, ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship

association_table = Table('association', Base.metadata,
                          Column('user_id', ForeignKey('user.user_id')),
                          Column('chat_id', ForeignKey('chat.chat_id'))
                          )


class Chat(Base):
    __tablename__ = 'chat'

    chat_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    type = Column(String, nullable=True)
    title = Column(String, nullable=True)

    user = relationship('User', back_populates='chat')


class User(Base):
    __tablename__ = 'user'

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    is_bot = Column(Boolean)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    username = Column(String, nullable=True)
    language_code = Column(String, nullable=True)
    chat_id = Column(BigInteger, ForeignKey('chat.chat_id'))

    chat = relationship('Chat', back_populates='user')
