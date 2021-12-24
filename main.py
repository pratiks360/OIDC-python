#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_oidc import OpenIDConnect

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': '9iokok',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': './client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post',
    'OIDC_OPENID_REALM': 'ventilator',
    'OIDC_TOKEN_TYPE_HINT': 'access_token',
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_VALID_ISSUERS': ['http://localhost:8888/auth/realms/demo'],
    })

oidc = OpenIDConnect(app)


@app.route('/withouttoken')
def hello():
    return 'App  Started'


@app.route('/token', methods=['POST'])
@oidc.accept_token(require_token=True)
def process_image():

    return {'msg': 'authenticated'}

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
