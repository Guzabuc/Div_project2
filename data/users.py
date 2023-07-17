#     #  __tablename__ служебный атрибут , т.о мы создаем таблицу с имененм 'users'
#     # autoincrement Автоматическое приращение позволяет автоматически генерировать уникальное число при вставке новой записи в
#     # nullable - не может быть нулем

import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash

# роль пользователя юзер и админ
ACCESS = {
    'user': 1,
    'admin': 2
}

class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True,
                              unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # создаем уровни пользователей
    # level = sqlalchemy.Column(sqlalchemy.Integer, default=1)
    create_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                    default=datetime.datetime.now())
    news = orm.relationship('News', back_populates='user')

    # пишем функцию для отображения информации __repr__(спец метод)
    def __repr__(self):
        return f'{self.name} - {self.email}'
    # возвращает Mark - plumer_mark@yyy.ru

    # хеширование пароля
    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    # сверяем пароль с введеным паролем
    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


    # Проверяем, является ли пользователь админом
    def is_admin(self):
        return self.level == ACCESS['admin']

    # разрешение действий пользователю с текущем уровнем применяется если уровней больше 2х
    def allowed(self, access_level):
        return  self.level >= access_level