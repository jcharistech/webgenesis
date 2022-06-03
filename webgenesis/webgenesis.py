#!/usr/bin/python
import click

import datetime
import time
import os

timestr = time.strftime("%Y%m%d-%H%M%S")
from click_help_colors import HelpColorsGroup, HelpColorsCommand


FLASK_TEMPLATE = """
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello Flask'


if __name__ == '__main__':
	app.run(debug=True)


"""



STREAMLIT_TEMPLATE = """
import streamlit as st  

def main():
	st.title("Streamlit App")
	st.subheader("Hello Streamlit")


if __name__ == '__main__':
	main()


"""

STREAMLIT_MULTIPAGE_TEMPLATE = """
import streamlit as st  

def main():
	st.title("Streamlit App")
	st.subheader("Hello Streamlit")

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
	else:
		st.subheader("About")


if __name__ == '__main__':
	main()


"""



BOTTLE_TEMPLATE = """
from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello Bottle!"

run(app, host='localhost', port=8080)

"""

EXPRESS_TEMPLATE = """
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello Express!')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

"""

KOAJS_TEMPLATE = """
const Koa = require('koa');
const app = new Koa();

app.use(async ctx => {
  ctx.body = 'Hello Koa';
});

app.listen(3000);

"""

TORNADO_TEMPLATE = """
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


"""

FASTAPI_TEMPLATE = """
from fastapi import FastAPI
from typing import Optional
import uvicorn

# Init app
app = FastAPI()


@app.get("/")
def read_root():
    return {"text": "Hello FastAPI"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}



if __name__ == '__main__':
	uvicorn.run(app,host='127.0.0.1',port=8000)


"""




# def create_project(frameworktype):
# 	DIR_PATH = 'hello-flask/template'
# 	os.makedirs(DIR_PATH)
# 	FILE_PATH = 'hello-flask/app.py'
# 	with open(FILE_PATH,"w+") as f:
# 		f.write(FLASK_TEMPLATE)
# 	print("Finished Creating Project") 


# DEFAULTS
DIR_PATH_FLASK = 'hello-flask/templates'
FILE_PATH_FLASK = 'hello-flask/app.py'

DIR_PATH_STREAMLIT = 'hello-streamlit'
FILE_PATH_STREAMLIT = 'hello-streamlit/app.py'

DIR_PATH_STREAMLIT_MULTIPAGE = 'hello-streamlit-multi/pages'
FILE_PATH_STREAMLIT_MULTIPAGE = 'hello-streamlit-multi/app.py'

DIR_PATH_BOTTLE = 'hello-bottle/templates'
FILE_PATH_BOTTLE = 'hello-bottle/app.py'

DIR_PATH_EXPRESS = 'hello-express/views'
FILE_PATH_EXPRESS = 'hello-express/app.js'

DIR_PATH_KOAJS = 'hello-koa/views'
FILE_PATH_KOAJS = 'hello-koa/app.js'

DIR_PATH_TORNADO = 'hello-tornado'
FILE_PATH_TORNADO = 'hello-tornado/app.py'

DIR_PATH_FASTAPI = 'hello-fastapi/templates'
FILE_PATH_FASTAPI = 'hello-fastapi/app.py'



def create_project(TEMPLATE_TYPE,DIR_PATH,FILE_PATH):
	"""Create A Project Per the Template,Path and File
using default project folder name
	"""
	try:
		os.makedirs(DIR_PATH)
	except:
		click.secho("A Similar Project Already Exist", fg="red")
	with open(FILE_PATH,"w+") as f:
		f.write(TEMPLATE_TYPE)
	print("Finished Creating Project")  

def create_project_per_folder(TEMPLATE_TYPE,folder_name,language='py'):
	"""Create A Project Per the Template,Path and File using the 
		specified directory/folder
	"""
	try:
		DIR_PATH_ALL = '{}/template'.format(folder_name)
		os.makedirs(DIR_PATH_ALL)
	except:
		click.secho("A Similar Project Already Exist", fg="red")
	FILE_PATH_ALL = "{}/app.{}".format(folder_name,language)
	print(FILE_PATH_ALL)
	with open(FILE_PATH_ALL,"w+") as f:
		f.write(TEMPLATE_TYPE)
	print("Finished Creating Project")  

def create_project_per_folder_st(TEMPLATE_TYPE,folder_name,language='py'):
	"""Create A Project Per the Template,Path and File using the 
		specified directory/folder
	"""
	try:
		DIR_PATH_ALL = '{}/data'.format(folder_name)
		os.makedirs(DIR_PATH_ALL)
		
	except:
		click.secho("A Similar Project Already Exist", fg="red")
	FILE_PATH_ALL = "{}/app.{}".format(folder_name,language)
	print(FILE_PATH_ALL)
	with open(FILE_PATH_ALL,"w+") as f:
		f.write(TEMPLATE_TYPE)
	print("Finished Creating Project")  



@click.group(
    cls=HelpColorsGroup, help_headers_color="yellow", help_options_color="cyan"
)
@click.version_option("0.0.3", prog_name="webgenesis")
def main():
    """Webgenesis : A simple CLI for creating basic starter templates for web frameworks """
    pass


@main.command()
@click.argument("frameworktype")
@click.option('--folder','-f',help='specify folder name')
def create(frameworktype,folder):
	""" Create A Basic Startup Project for the specified web framework

	frameworktype:: flask,express,streamlit,bottle,koa,tornado,fastapi,streamlit-multipage

	---Usage---

	webgenesis create flask

	webgenesis create flask -f newflaskapp

	webgenesis create streamlit
	

	"""
	click.secho("Creating a :: {} project".format(frameworktype), fg="blue")
	click.echo("Folder:{}".format(folder))
	if folder is None:
		if frameworktype == 'flask':
			create_project(FLASK_TEMPLATE,DIR_PATH_FLASK,FILE_PATH_FLASK)
		elif frameworktype == 'streamlit':
			create_project(STREAMLIT_TEMPLATE,DIR_PATH_STREAMLIT,FILE_PATH_STREAMLIT)
		elif frameworktype == 'streamlit-multipage':
			create_project(STREAMLIT_MULTIPAGE_TEMPLATE,DIR_PATH_STREAMLIT_MULTIPAGE,FILE_PATH_STREAMLIT_MULTIPAGE)
		elif frameworktype == 'express':
			create_project(EXPRESS_TEMPLATE,DIR_PATH_EXPRESS,FILE_PATH_EXPRESS)
		elif frameworktype == 'bottle':
			create_project(BOTTLE_TEMPLATE,DIR_PATH_BOTTLE,FILE_PATH_BOTTLE)
		elif frameworktype == 'koa':
			create_project(KOAJS_TEMPLATE,DIR_PATH_KOAJS,FILE_PATH_KOAJS)

		elif frameworktype == 'tornado':
			create_project(TORNADO_TEMPLATE,DIR_PATH_TORNADO,FILE_PATH_TORNADO)

		elif frameworktype == 'fastapi':
			create_project(FASTAPI_TEMPLATE,DIR_PATH_FASTAPI,FILE_PATH_FASTAPI)
	else:
		if frameworktype == 'flask':
			create_project_per_folder(FLASK_TEMPLATE,folder)
		elif frameworktype == 'streamlit':
			create_project_per_folder_st(STREAMLIT_TEMPLATE,folder)
		elif frameworktype == 'streamlit-multipage':
			create_project_per_folder_st(STREAMLIT_MULTIPAGE_TEMPLATE,folder)
		elif frameworktype == 'express':
			create_project_per_folder(EXPRESS_TEMPLATE,folder,"js")
		elif frameworktype == 'bottle':
			create_project_per_folder(BOTTLE_TEMPLATE,folder)
		elif frameworktype == 'koa':
			create_project_per_folder(KOAJS_TEMPLATE,folder,"js")
		elif frameworktype == 'tornado':
			create_project(TORNADO_TEMPLATE,folder)
		elif frameworktype == 'fastapi':
			create_project_per_folder(FASTAPI_TEMPLATE,folder)


@main.command()
def info():
	"""Info About CLI """
	version_info = '0.0.2'
	click.secho("webgenesis v.{}".format(version_info),fg='blue')
	click.echo("Jesus Saves @JCharisTech")



if __name__ == '__main__':
	main()