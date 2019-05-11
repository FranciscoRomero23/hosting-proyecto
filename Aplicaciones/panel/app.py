# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file, redirect,error,get,response

@route('/')
def inicio():
	return template('html/inicio.tpl')

@route('/software')
def software():
	return template('html/software.tpl')

@route('/logs')
def logs():
	return template('html/logs.tpl')

@route('/style/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='html/style')

run(host='0.0.0.0', port=8080)
