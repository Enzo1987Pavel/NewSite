from flask import Flask, render_template

app = Flask(__name__)

menu = ["Установка", "Первое приложение", "Обратная связь"]


@app.route("/")
def main_page():
    return render_template("index.html", name="index", title="Главная", menu=menu)


@app.route("/about")
def about_page():
    return render_template("about.html", name="about", title="О сайте")


@app.errorhandler(404)  # Форма для вывода ошибка при неправильном URL-адресе, если страница не будет найдена
def page_not_found(e):
    return render_template("error_404.html", e=e), 404


@app.errorhandler(500)  # Форма при проблемах с сервером, внутренней ошибке в программе
def page_not_found(e):
    return render_template("error_500.html", e=e), 500


if __name__ == "__main__":
    app.run()
