from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired

#  FileField если из формы добавляем файл, то обращаться
#  к нему при обработке следует так: f.form.<название поля с файлом>.data

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    # file = FileField('Файл')
    submit = SubmitField('Войти')
