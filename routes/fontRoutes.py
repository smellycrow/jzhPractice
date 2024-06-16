from flask import render_template, Blueprint
from datetime import datetime

app_bp = Blueprint("font_bp", __name__)


@app_bp.route('/')
def hello_world():
    now_time = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    user_list = ['jzh', 'snow', 'yh', 'dz', 'pp']
    return render_template('helloWorld.html',
                           now_time=now_time,
                           user_list=user_list
                           )


@app_bp.route('/upload_file')
def block_test():
    return render_template('upload.html')
