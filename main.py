from flask import Flask, url_for, request, redirect
from flask import render_template
import json


app = Flask(__name__)


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





@app.route('/nekrasov')
def nekrasov():
    return f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Постер</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
    <link rel="stylesheet" type= "text/css" href="{url_for('static', filename='css/style.css')}">

    
</head>
<body>

<div class="container text-center">
  <div class="row">
    <div class="col">
  <h1>Постер к фильму</h1>
<img src="{url_for('static', filename='images/nekrasov.png')}"
alt="Здесь должна была быть картинка, но не нашлась">  
    </div>
    <div class="col">
<div class="p-3 mb-2 bg-primary text-white">.bg-primary</div>
<div class="p-3 mb-2 bg-secondary text-white">.bg-secondary</div>
<div class="p-3 mb-2 bg-success text-white">.bg-success</div>
<div class="p-3 mb-2 bg-danger text-white">.bg-danger</div>
<div class="p-3 mb-2 bg-warning text-dark">.bg-warning</div>    
    </div>
  </div>



<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>

</body>
</html>
"""


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
        myform = request.form.to_dict()

        print(myform)
        return render_template('filled_form.html',
                               title='Ваша форма',
                               data=myform)




@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'GET':
        return render_template('user_form.html', title= 'Форма')


    elif request.method == 'POST':
        f = request.files['file']
        # request.files['file'] используем этот метод , но он только если есть ключ,  request.form.get('file') если его нет
        f.save('./static/images/loaded.png')
        myform = request.form.to_dict()
        return render_template('filled_form.html', title='Ваши данные', data=myform)







if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)



# GET - запрашивает данные, не меняя состояния сервера
# POST - отправляет данные на сервер
# PUT  - заменяет все текущие данные на сервере, данными запроса
# DELETE - удаляет указанные данные
# PATCH - частичная замена данных



