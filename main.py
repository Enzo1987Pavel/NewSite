import os

from flask import Flask, render_template
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


@app.route("/about")
def about_page():
    return render_template("about.html", name="about", title="О сайте")  # , menu=menu)


@app.route("/application")
def about_app_page():
    return render_template("application.html", name="application", title="О приложении")


@app.errorhandler(404)  # Форма для вывода ошибка при неправильном URL-адресе, если страница не будет найдена
def page_404(e):
    return render_template("error_404.html", e=e), 404


# @app.route("/test")  # Форма для вывода ошибка при неправильном URL-адресе, если страница не будет найдена
# def test_page():
#     return render_template("test.html", title="Test page")


@app.errorhandler(500)  # Форма при проблемах с сервером, внутренней ошибке в программе
def error_500(e):
    return render_template("error_500.html", e=e), 500


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1")
