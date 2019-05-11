# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file, redirect,error,get,response

@route('/')
def inicio():
	return template('html/inicio.tpl')

@route('/servidores')
def servidores():
	return template('html/servidores.tpl')

@route('/registro')
def registro():
	return template('html/registro.tpl')

@route('/style/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='html/style')

run(host='0.0.0.0', port=8080)
