from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html", name="index")


@app.route("/<first_name>/")
def main_page_post():
    return render_template("index_post.html", name="index_post")


if __name__ == "__main__":
    app.run()
