#!/bin/bash

python3 -m venv virtual_env

virtual_env/bin/pip install flask
virtual_env/bin/pip install flask-login
virtual_env/bin/pip install flask-openid
virtual_env/bin/pip install flask-mail
virtual_env/bin/pip install flask-sqlalchemy
virtual_env/bin/pip install sqlalchemy-migrate
virtual_env/bin/pip install flask-whooshalchemy
virtual_env/bin/pip install flask-wtf
virtual_env/bin/pip install flask-babel
virtual_env/bin/pip install guess_language
virtual_env/bin/pip install flipflop
virtual_env/bin/pip install coverage