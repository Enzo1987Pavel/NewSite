from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html", name="index")


if __name__ == "__main__":
    app.run()
