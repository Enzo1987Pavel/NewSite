import os

from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime, time


app = Flask(__name__)


# def format_datetime(value, format='%B %d, %Y %H:%M'):
#     """Custom filter for formatting datetime objects."""
#     if value is None:
#         return ""
#     return value.strftime(format)


@app.route("/")
def main_page():
    return render_template("index.html", name="index", title="Главная")  # , menu=menu)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            # Аутентификация успешна
            return redirect(url_for('dashboard'))
        else:
            # Аутентификация не удалась
            return render_template('login.html', error='Неверное имя пользователя или пароль')

    # Если это GET-запрос, просто отображаем страницу входа
    return render_template('login.html')


@app.route("/about")
def about_page():
    return render_template("about.html", name="about", title="О сайте")  # , menu=menu)


@app.route("/application")
def about_app_page():
    return render_template("application.html", name="application", title="О приложении")


@app.route("/contacts")
def contacts_page():
    return render_template("contacts.html", name="contacts", title="Контакты")


@app.errorhandler(404)  # Форма для вывода ошибка при неправильном URL-адресе, если страница не будет найдена
def page_404(e):
    return render_template("error_404.html", e=e), 404


# @app.route("/contacts/test")  # Форма для вывода ошибка при неправильном URL-адресе, если страница не будет найдена
# def test_page():
#     return render_template("test.html", title="Test page")


@app.errorhandler(500)  # Форма при проблемах с сервером, внутренней ошибке в программе
def error_500(e):
    return render_template("error_500.html", e=e), 500


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1")
