from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    comic = [
        {"title": "Кадр 1", "text": "Вспыш летит над городом и понимает, что опаздывает."},
        {"title": "Кадр 2", "text": "Миша сидит на площадке с поломанной машинкой."},
        {"title": "Кадр 3", "text": "Вспыш торопится починить машинку и делает хуже."},
        {"title": "Кадр 4", "text": "В мастерской Вспыш чинит машинку аккуратно."},
        {"title": "Кадр 5", "text": "Машинка снова работает."},
        {"title": "Кадр 6", "text": "Вспыш помогает бабушке и понимает: всему своё время."}
    ]

    return render_template("index.html", comic=comic)

if __name__ == "__main__":
    app.run(debug=True)