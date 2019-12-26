from flask import Flask
from flask import render_template, render_template_string
from flask import request, redirect, jsonify
from autox import run
import os
from shutil import copy
from flask_bootstrap import Bootstrap

app = Flask(__name__)


bootstrap = Bootstrap(app)


@app.route('/index', methods=['GET'])
def index():
    html = render_template("index.html")
    return html


@app.route('/result', methods=['GET'])
def search():
    scenario = request.args.get('scenario_name')
    result = run.run(scenario)
    if result is None:
        return render_template('empty.html')

    copy(os.getcwd()+'/report/测试报告.html', os.getcwd()+'/templates/')
    return render_template("测试报告.html")


if __name__ == '__main__':
    app.run()
