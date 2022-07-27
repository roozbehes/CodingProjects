from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def results():
    with open("results.csv", "r") as file:
        data = [item.strip().split(',') for item in file.readlines()]
    data.sort(key=lambda x: int(x[1]), reverse=True)
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
