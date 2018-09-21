from flask import Flask, request
from caesar import encrypt
import cgi

app = Flask(__name__)
app.config['DEBUG']=True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            .error {{ color: red; }}
            </style>
        </head>
        <body>
          <!-- create your form here -->
            <form method="post">
                <label id="rot">
                    Rotate by
                </label>
                <input id="rot" type="text" name="rot" value="0"/>
                <p class="error">{1}</p>
                <textarea name="text">{0}</textarea>
                <br>
                <input type="submit" />
            </form>
        </body>
    </html>
    """
    #form = form.format()

@app.route("/")
def index():
    return form.format('', '')

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/", methods=['post'])
def encrypt_input():
    error = ''
    rotation = None

    if is_integer(request.form["rot"]):
        rotation = request.form["rot"]
        rotation = int(rotation)
    else:
        #set value of rotation to 0 and flag an error
        rotation = 0
        error = 'Please enter an integer.'

    #user_text = cgi.escape(request.form["text"])
    user_text = request.form["text"]

    #return "<h1>" + encrypt(user_text, rotation) + "</h1>"
    #return "<h1>" + str(rotation) + "</h1>"
    return form.format(encrypt(user_text, rotation), error)

app.run()
