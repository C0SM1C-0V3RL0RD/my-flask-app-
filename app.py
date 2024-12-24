from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    menu_items = [
        {"name": "İskender Kebap", "price": 290, "image": "iskender.jpg"},
        {"name": "Adana Kebap", "price": 260, "image": "adana.jpg"},
        {"name": "Urfa Kebap", "price": 260, "image": "urfa.jpg"},
        {"name": "Beyti Kebap", "price": 275, "image": "beyti.jpg"},
        {"name": "Güveç", "price": 290, "image": "guvec.jpg"},
        {"name": "Tandır", "price": 580, "image": "tandir.jpg"},
    ]
    return render_template("index.html", menu_items=menu_items)

if __name__ == "__main__":
    app.run(debug=True)
