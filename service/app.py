import os

from flask import Flask, request, render_template

from somelib.useless import put_something

app = Flask(__name__)
DEBUG = bool(os.getenv('DEBUG', True))
PORT = int(os.getenv('PORT', 8080))


@app.route('/api/v1/ping')
def ping():
    return 'pong'


@app.route('/api/v1/put_something', methods=['POST'])
def put_something():
    content = request.json
    print(content)
    text = content['text']

    list = put_something(text)
    return {
        'code': 'OK',
        'message': '',
        'result': list
    }


@app.route('/page')
def page():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)