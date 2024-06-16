from flask import Flask

from FontFilter.add_filters import add_template_filters
from routes.serverApiRoutes import register_route

app = Flask(__name__)

# 添加jinja2自定义过滤器
add_template_filters(app)

# 注册路由
register_route(app)
