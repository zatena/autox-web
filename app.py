from flask import Flask,  url_for
from flask import render_template, render_template_string
from flask import request, redirect, jsonify
from autox import run
import os
import json
from shutil import copy
from flask_bootstrap import Bootstrap

app = Flask(__name__)


bootstrap = Bootstrap(app)


@app.route('/')
def homepage():
    return redirect(url_for('index'))


@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/result', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        print(type(request.form.get('data')))
        data = json.loads(str(request.form.get('data')))
        scenario = data['scenario ']
        result = run.run(scenario)
        if result is None:
            return render_template('empty.html')

        copy(os.getcwd()+'/report/测试报告.html', os.getcwd()+'/templates/')
        return render_template("测试报告.html")
    else:
        return "请求方法错误"


if __name__ == '__main__':
    app.run()
