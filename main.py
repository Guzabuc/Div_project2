from flask import Flask, url_for, request, redirect
from flask import render_template, make_response, session
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_login import current_user
import json
import requests
import datetime
from loginform import LoginForm
from mail_sender import send_mail
from dotenv import load_dotenv
from data import db_session
from data.users import User
from data.news import News
# forms.user - путь к файлу, импортируем класс RegisterForm
from forms.user import RegisterForm
from forms.add_news import NewsForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'too short key'
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///db/news.sqlite'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)  # год


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return (redirect('/'))


# ошибка 404
@app.errorhandler(404)
def http_404_error(error):
    return redirect('/error404')


@app.route('/error404')
def well():  # колодец
    return render_template('well.html')


@app.errorhandler(401)
def http_401_handler(error):
    return redirect('/login')


@app.route('/')  # Это главная страница сайта
@app.route('/index')
def index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        news = db_sess.query(News).filter((News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template('index.html', title='Новости', news=news)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)


@app.route('/news', methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()  # ORM  модель NEWS  через базу данных подключаемся к
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        # .merge - слияние сессии с текущим пользователем
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('news.html', title='Добавление новости', form=form)


@app.route('/var_test')
def var_test():
    return render_template('var_test.html', title='Переменные в HTML')


@app.route('/slogan')
def slogan():
    return 'какая то цитата<br><a href ="/">Назад</a>'


# секретный ключ - чтобы не украли наш сайт,
# чем длиннее и непонятней, тем лучше

@app.route('/success')
def success():
    return 'Success'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        # form.password != form.password_again - проверяем введенные пароли в register.html
        # form.password.data - .data отсылка к данным, если ее не будет , то отылка идет к объекту
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Проблемы с регистрацией',
                                   message='Пароли не совпадают', form=form)
        db_sess = db_session.create_session()
        # User.email == form.email.data - роверка на повторную регистрацию
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html',
                                   title='Проблемы с регистрацией',
                                   message='Пользователь с такой почтой уже есть', form=form)
        # если все правильно , записываем в базу нового пользователя
        user = User(name=form.name.data,
                    email=form.email.data,
                    about=form.about.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html', title='Повторная авторизация',
                               message='Неверный логин или пароль', form=form)
    return render_template('login.html', title='Авторизация', form=form)


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
        # time_true = datetime.utcfromtimestamp(time).strftime("%H:%M")

        # заполняем словарь
        # data['time'] = time_true
        data['humidity'] = weather['main']['humidity']
        data['code'] = code
        data['icon'] = icon
        data['temp'] = weather['main']['temp']

        return render_template('weather.html',
                               title=f'Погода в городе {{town}}', data=data)


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


@app.route('/cookie_test')
def cookie_test():
    visit_count = int(request.cookies.get('visit_count', 0))
    if visit_count != 0 and visit_count <= 20:
        res = make_response(f'Были уже {visit_count + 1} раз')
        res.set_cookie('visit_count',
                       str(visit_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    elif visit_count > 20:
        print('Мы тут')
        res = make_response(f'Были уже {visit_count + 1} раз')
        res.set_cookie('visit_count', '1', max_age=0)
    else:
        res = make_response('Вы впервые здесь за 2 года')
        res.set_cookie('visit_count', '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res


@app.route('/session_test')
def session_test():
    visit_count = session.get('visit_count', 0)
    session['visit_count'] = visit_count + 1
    if session['visit_count'] > 3:
        session.pop('visit_count', None)
    session.permanent = True
    return make_response(f'Мы тут были уже {visit_count + 1} раз')


@app.route('/mail', methods=['GET'])
def get_form():
    return render_template('mail_send.html')


@app.route('/mail', methods=['POST'])
def post_form():
    email = request.values.get('email')
    if send_mail(email, 'Вам письмо', 'Текст письма'):
        return f'Письмо на адрес {email} отправлено успешно!'
    return 'Сбой при отправке'


if __name__ == '__main__':
    db_session.global_init('db/news.sqlite')
    db_sess = db_session.create_session()  # подключение к базе данных
    app.run(host='127.0.0.1', port=5000, debug=True)
