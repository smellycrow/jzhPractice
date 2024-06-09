from FontFilter.filter_funcs import *


def add_template_filters(app):
    app.add_template_filter(double_filter, name="double_step")
    app.jinja_env.add_extension('jinja2.ext.do')
