import pytest
from jinja2 import Environment, FileSystemLoader
import yaml

def test_database_template_renders_sqlite():
    env = Environment(loader=FileSystemLoader('crud_generator/templates'))
    template = env.get_template('database.py.j2')
    config = {
        'type': 'sqlite',
        'url': 'sqlite:///./test.db',
        'connect_args': {'check_same_thread': False},
        'echo': False,
    }
    rendered = template.render(database=config)
    assert 'sqlite:///./test.db' in rendered
    assert 'check_same_thread' in rendered
    assert 'echo=False' in rendered

def test_database_template_renders_postgres():
    env = Environment(loader=FileSystemLoader('crud_generator/templates'))
    template = env.get_template('database.py.j2')
    config = {
        'type': 'postgresql',
        'url': 'postgresql://user:pass@localhost/db',
        'connect_args': {},
        'echo': True,
    }
    rendered = template.render(database=config)
    assert 'postgresql://user:pass@localhost/db' in rendered
    assert 'connect_args={}' in rendered
    assert 'echo=True' in rendered
