from flask import Flask

from FontFilter.add_filters import add_template_filters
from routes.fontRoutes import app_bp

app = Flask(__name__)


# 注册蓝图
app.register_blueprint(app_bp)

# 添加jinja2自定义过滤器
add_template_filters(app)


