import os
from flask import Flask, request, render_template, flash, url_for
from somelib.useless import reverse

DEBUG = bool(os.getenv('DEBUG', True))
PORT = int(os.getenv('PORT', 8080))

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

messages = []

@app.route('/api/v1/ping')
def ping():
    return 'pong'

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        title = reverse(request.form['title'])
        content = reverse(request.form['content'])

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})

    return render_template('index.html', messages = messages)





if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
