from flask import Flask, url_for, request, redirect
from flask import render_template
import json
import requests
from datetime import datetime
from loginform import LoginForm
from mail_sender import send_mail
from dotenv import load_dotenv
from data import db_session
from data.users import User
from data.news import News


app = Flask(__name__)

app.config['SECRET_KEY'] = 'too short key'

app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///db/news.sqlite'

# секретный ключ - чтобы не украли наш сайт,
# чем длиннее и непонятней, тем лучше

@app.route('/success')
def success():
    return 'Success'
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


# ошибка 404
@app.errorhandler(404)
def http_404_error(error):
    return redirect('/error404')

@app.route('/error404')
def well():  # колодец
    return render_template('well.html')


@app.route('/')  # Это главная страница сайта
@app.route('/index')
def index():
    # - старый метод
    # user = "Слушатель"
    # redirect('/load_photo')  безусловный редирект, перекидывает сразу на эту форму
    # return render_template('index.html', title='Работа с шаблонами',username=user)
    param = {}
    param['username'] = 'Ученик'
    param['title'] = 'Раширяем шаблоны'
    return render_template('index.html', **param)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf-8") as f:
        news_list = json.loads(f.read())
    return render_template('news.html',
                           title='Новости',
                           news=news_list)
    # lst = ['ANN', 'TOM', 'BOB']
    # return render_template('news.html', title="FOR", news=lst)


@app.route('/var_test')
def var_test():
    return render_template('var_test.html', title='Переменные в HTML')


@app.route('/slogan')
def slogan():
    return 'какая то цитата<br><a href ="/">Назад</a>'




@app.route('/form_sample', methods=['GET', 'POST'])
def form_sample():
    if request.method == 'GET':
        return render_template('user_form.html', title='Форма')
    elif request.method == 'POST':
        f = request.files['file']  # request.form.get('file')
        f.save('./static/images/loaded.png')
        myform = request.form.to_dict()

        return render_template('filled_form.html',
                               title='Ваша форма',
                               data=myform)


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'GET':
        return render_template('user_form.html', title='Форма')


    elif request.method == 'POST':
        f = request.files['file']
        # request.files['file'] используем этот метод , но он только если есть ключ,  request.form.get('file') если его нет
        f.save('./static/images/loaded.png')
        myform = request.form.to_dict()
        return render_template('filled_form.html', title='Ваши данные', data=myform)


@app.route('/weather_form', methods=['GET', 'POST'])
def weather_form():
    if request.method == 'GET':
        return render_template('weather_form.html', title='Выбор города')
    elif request.method == 'POST':
        town = request.form.get('town')
        data = {}
        key = '06d3cdd940dbee91c85e8dedf7a91f78'
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': key, 'q': town, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()
        code = weather['cod']
        icon = weather['weather'][0]['icon']
        time = weather['sys']['sunset']
        time_true = datetime.utcfromtimestamp(time).strftime("%H:%M")

        # заполняем словарь
        data['time'] = time_true
        data['humidity'] = weather['main']['humidity']
        data['code'] = code
        data['icon'] = icon
        data['temp'] = weather['main']['temp']
        return render_template('weather.html', title=f'Погода в городе {{town}}', data=data)




if __name__ == '__main__':
    # подключаемся к бд
    db_session.global_init('db/news.sqlite')

    # app.run(host='127.0.0.1', port=5000, debug=True)

    db_sess = db_session.create_session()   # подключение к базе данных

    #  user = db_sess.query(User).first() # одключаюсь к классу User к первому .first пользователю
    # users = db_sess.query(User).all()  #  ыводит всех

    # в сложных запросах  &- и  |- или
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
