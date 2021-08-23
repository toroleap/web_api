import json

from flask import Flask, Response, make_response, request, render_template, redirect, url_for
import config

app = Flask(__name__)
app.config.from_object(config)

users = []


@app.route('/', endpoint= 'index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        if password == re_password:
            user = {'username': username, 'password': password}
            users.append(user)
            return redirect(url_for('index'))
        else:
            return "password doesn't match"
    return render_template('register.html')


@app.route('/show', methods=['GET'])
def show():
    json_str = json.dumps(users)
    return json_str


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
