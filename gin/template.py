import jinja2
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(dir_path, 'templates')

loader = jinja2.FileSystemLoader(template_dir)

template_env = jinja2.Environment(loader=loader)
