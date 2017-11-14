from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

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
            <form action="/hello" method="post">
                <label for="rot">Rotate by:</label>
                <input type="number" name="rot" value="0"/>

                <textarea type="text" name="phrase"></textarea>
                <input type="submit"/>
            </form>

        </body>
    </html>
"""



@app.route("/")
def index():
    #form = form.format()
    return form

@app.route("/hello", methods=['POST'])
def hello():
    text = request.form['phrase']
    num = request.form['rot']
    num = int(num)

    code = rotate_string(text, num)
    #form = form.format('<h1>' + code + '</h1>')

    return '<h1>' + code + '</h1>'






app.run()
