from flask import Flask, url_for, request, redirect
from flask import render_template
import json
import requests
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'too short key'
# секретный ключ - чтобы не украли наш сайт,
# чем длиннее и непонятней, тем лучше



# ошибка 404
@app.errorhandler(404)
def http_404_error(error):
    return redirect('/error404')


@app.route('/error404')
def well():   # колодец
    return render_template('well.html')






@app.route('/')  # Это главная страница сайта
@app.route('/index')
def index():
    #- старый метод
    #user = "Слушатель"
    # redirect('/load_photo')  безусловный редирект, перекидывает сразу на эту форму
   # return render_template('index.html', title='Работа с шаблонами',username=user)
    param= {}
    param['username'] = 'Ученик'
    param['title'] = 'Раширяем шаблоны'
    return render_template('index.html', **param)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)

@app.route('/news')
def news():
    with open('news.json', 'rt', encoding='utf-8') as f:
        news_list = json.loads(f.read())
    return render_template('news.html', title='Новости',
                            news=news_list )



@app.route('/var_test')
def var_test():
    return  render_template('var_test.html', title='Переменные в HTML')

@app.route('/slogan')
def slogan():
    return 'какая то цитата<br><a href ="/">Назад</a>'


@app.route('/countdown')
def countdown():
    lst = [str(x) for x in range(10, 0, -1)]
    lst.append('Start!!!')
    return '<br>'.join(lst)



@app.route('/variants/<int:var>')
def variants(var):
    if var == 1:
        return f"""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>{var}</title>
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
                    <link rel="stylesheet" type= "text/css" href="{url_for('static', filename='css/style.css')}">
                </head>
                <body>
                <h1 >Привет, {var}</h1>
                <dl>
                  <dt>Режиссер:</dt>
                    <dd>Петр Точилин</dd>
                  <dt>В ролях:</dt>
                    <dd>Андрей Гайдулян</dd>
                    <dd>Алексей Гаврилов</dd>
                    <dd>Виталий Гогунский</dd>
                    <dd>Мария Кожевникова</dd>
                </dl>
                
                <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
                </body>
                </html>
"""
    elif var == 2:
        return f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>{var}</title>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
                <link rel="stylesheet" type= "text/css" href="{url_for('static', filename='css/style.css')}">
            </head>
            <body>
            <h1 >Привет, {var}</h1>
            <ul>
             <li>Пункт 1.</li>
              <li>Пункт 2.
                <ul>
                  <li>Подпункт 2.1.</li>
                   <li>Подпункт 2.2.     
                    <ul>
                      <li>Подпункт 2.2.1.</li>
                      <li>Подпункт 2.2.2.</li>
                      </ul>
                   </li>          
                  <li>Подпункт 2.3.</li>
                </ul>
              </li>
             <li>Пункт 3.</li>
            </ul>
            
            <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
            </body>
            </html>
            """
    else:
        return " не знаю о чем вы"


@app.route('/slideshow')  # карусель
def slideshow():
    return f"""<!DOCTYPE html>

    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Постер</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
        <link rel="stylesheet" type= "text/css" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
    
    <div class="container">
  <div class="row">
    <div class="col">
     <div id="carouselExampleControlsNoTouching" class="carousel slide" data-touch="false" data-interval="false">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{url_for('static', filename='images/foni4.png')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/foni1.png')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/foni3.png')}" class="d-block w-100" alt="...">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControlsNoTouching" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControlsNoTouching" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
    </div>
    <div class="col-6">
 <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{url_for('static', filename='images/foni1.png')}" class="d-block w-100" alt="Здесь должна была быть картинка, но не нашлась">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/foni2.png')}" class="d-block w-100" alt="Здесь должна была быть картинка, но не нашлась">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/foni3.png')}" class="d-block w-100" alt="Здесь должна была быть картинка, но не нашлась">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Предыдущий</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Следующий</span>
  </a>
</div>
    </div>
    <div class="col">
<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{url_for('static', filename='images/foni3.png')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/foni4.png')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/foni2.png')}" class="d-block w-100" alt="...">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Предыдущий</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Следующий</span>
  </a>
</div>
    </div>
  </div>
  
    
    
    


    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
    </body>
    </html>
    """


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
        url ='http://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': key, 'q': town, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather =result.json()
        code = weather['cod']
        icon = weather['weather'][0]['icon']
        time = weather['sys']['sunset']
        time_true =datetime.utcfromtimestamp(time).strftime("%H:%M")

       # заполняем словарь
        data['time'] = time_true
        data['humidity']=weather['main']['humidity']
        data['code']= code
        data['icon'] = icon
        data['temp']= weather['main']['temp']
        return render_template('weather.html', title=f'Погода в городе {{town}}',

                               data = data)

# &deg; - значек градуса

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)




# GET - запрашивает данные, не меняя состояния сервера
# POST - отправляет данные на сервер
# PUT  - заменяет все текущие данные на сервере, данными запроса
# DELETE - удаляет указанные данные
# PATCH - частичная замена данных



