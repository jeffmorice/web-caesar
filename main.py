from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG']=True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            </style>
        </head>
        <body>
          <!-- create your form here -->
            <form method="post">
                <label id="rot">
                    Rotate by
                </label>
                <input id="rot" type="text" name="rot" value="0"/>
                <br>
                <textarea name="text"></textarea>
                <br>
                <input type="submit" />
            </form>
        </body>
    </html>
    """

@app.route("/")
def index():
    return form

@app.route("/", methods=['post'])
def encrypt_input():
    rotation = request.form["rot"]
    rotation = int(rotation)
    user_text = request.form["text"]

    return "<h1>" + encrypt(user_text, rotation) + "</h1>"
    #return "<h1>" + str(rotation) + "</h1>"

app.run()
