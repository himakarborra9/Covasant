from flask import Flask, jsonify, request


app = Flask(__name__)

items = []

item1 = {"title": "mouse", "price": 1200, "country": "india"}
item2 = {"title": "keyboard", "price": 1600, "country": "russia"}
item3 = {"title": "ssd", "price": 3000, "country": "usa"}

items.append(item1)
items.append(item2)
items.append(item3)

@app.route("/")
def index():
    return """
    <html>
        <body>
            <h1>Welcome to the home page :)</h1>
        </body>
    </html>
    """


@app.route("/create")
def create():
    pass


@app.route("/all")
def all():
    return resp.jsonify(items)



if __name__ == '__main__':
    app.run()