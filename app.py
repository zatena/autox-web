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
# def search_form():
# #     return '''
# #         <body bgcolor="#E6E6FA">
# #         <div style="text-align:center">
# #         <font></font><br/><font></font><br/><font></font><br/>
# #         <font face="宋体" size="+5" color="#B0C4DE">接口自动化测试平台</font><br/>
# #         <font></font><br/>
# #         <font></font><br/>
# #         <form action='/search' method='post'>
# #             <input type="text" rows="2" cols="60" placeholder="请输入测试场景或输入全部..."
# #             name='scenario_name' style="height:40px; width:500px;">
# #             <button type="submit" class="search-submit"
# #             style="height:38px; width:60px;">执行</button>
# #         </form>
# #         </div>
# #         </body>
# #     '''
def index():
    html = render_template("index.html")
    return html


@app.route('/result', methods=['GET'])
def search():
    scenario = request.args.get('scenario_name')
    result = run.run(scenario)
    # page = open(report_html, encoding='utf-8')
    # res = page.read()
    if result is None:
        return render_template('空html')

    copy(os.getcwd()+'/report/测试报告.html', os.getcwd()+'/templates/')
    return render_template("测试报告.html")


if __name__ == '__main__':
    app.run()
