from flask import Flask,  url_for
from flask import render_template
from flask import request, redirect
from autox import run
import os
from shutil import copy
from collections import OrderedDict

app = Flask(__name__)


# bootstrap = Bootstrap(app)

@app.route('/')
def homepage():
    return redirect(url_for('index'))


@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/envconfig', methods=['GET'])
def env_config():
    return render_template("envConfig.html")


@app.route('/addcase', methods=['GET', 'POST'])
def case_add():
    if request.method == 'GET':
        return render_template("addcase.html")
    else:
        caseName = request.form.get('caseName')
        runSystem = request.form.get('runSystem')
        runEnv = request.form.get('runEnv')
        caseSet = request.form.get('caseSet')
        method = request.form.get('method')
        url = request.form.get('url')
        assertResult = request.form.get('assertResult')
        body = request.form.get('body')


@app.route('/caselist', methods=['GET'])
def case_list():
    return render_template("caselist.html")


@app.route('/set', methods=['GET'])
def case_set():
    return render_template("set.html")


@app.route('/result', methods=['GET'])
def search():
    if request.method == 'GET':
        data = request.args.get("hidden")
        scenario = str(data).split(",")
        result = run.run(scenario)

        if result is None:
            return render_template('empty.html')
        copy(os.getcwd()+'/report/测试报告.html', os.getcwd()+'/templates/')
        return render_template("测试报告.html")
    else:
        return "请求方法错误"


if __name__ == '__main__':
    app.run()

