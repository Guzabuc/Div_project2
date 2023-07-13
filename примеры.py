это нужно вставить в файл main.py



if __name__ == '__main__':
    # подключаемся к бд
    db_session.global_init('db/news.sqlite')

    # app.run(host='127.0.0.1', port=5000, debug=True)

    db_sess = db_session.create_session()  # подключение к базе данных

    #  user = db_sess.query(User).first() # одключаюсь к классу User к первому .first пользователю
    # users = db_sess.query(User).all()  #  ыводит всех

"""в сложных запросах  &- и  |- или"""

# users = db_sess.query(User).filter(User.email.like('%v%'))
# аменяем волдемарта на володя
# users = db_sess.query(User).filter(User.id == 1).first()
# id == 1).first() -

# for user in users:
#     print(user.name)  # Voldemar
#     user.name = 'Volodia'
#     print(user.name)
#     db_sess.commit()  # - заменить содержание

# удаляем одного пользователя полностью
# user = db_sess.query(User).filter(User.name == 'имя').first()
# db_sess.delete(user)
# db_sess.commit()

# создание юзеров в таблицу юзер
# user = User()
# user.name = 'Mark'
# user.about = 'Plumer'
# user.email = 'plumer_mark@yyy.ru'
# db_sess = db_session.create_session()
# db_sess.add(user)
# db_sess.commit()
# присваиваем к новости второй от пользователя его ид  из базы
# удалить пользователей у кого ид больше 3
# db_sess.query(User).filter(User.id >3).delete()


# id = db_sess.query(User).filter(User.id == '1').first()
# print(id.id)
# news = News(title='Новости от Владимира #2', content='<Больше не опаздываю>', user_id=id.id, is_private=False)

# user = db_sess.query(User).filter(User.id == '1').first()
# subj = News(title='Новости от Владимира #4', content='пошел на обед',  is_private=False)
# user.news.append(subj)
# db_sess.commit()

user = db_sess.query(User).filter(User.id == 1).first()
for news in user.news:
    print(news)

# GET - запрашивает данные, не меняя состояния сервера
# POST - отправляет данные на сервер
# PUT - заменяет все текущие данные на сервере, данными запроса
# DELETE - удаляет указанные данные
# PATCH - частичная замена данных
