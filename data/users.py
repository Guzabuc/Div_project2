# import datetime
# import sqlalchemy
# from .db_session import SqlAlchemyBase
#
# class User(SqlAlchemyBase):
#
#     __tablename__ = 'users'
#
#     #  __tablename__ служебный атрибут , т.о мы создаем таблицу с имененм 'users'
#     # autoincrement Автоматическое приращение позволяет автоматически генерировать уникальное число при вставке новой записи в
#     # nullable - не может быть нулем



import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True,
                              unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    create_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                    default=datetime.datetime.now())
    news = orm.relationship('News', back_populates='user')

    # пишем функцию для отображения информации __repr__(спец метод)
    def __repr__(self):
        return f'{self.name} - {self.email}'
    # возвращает Mark - plumer_mark@yyy.ru

