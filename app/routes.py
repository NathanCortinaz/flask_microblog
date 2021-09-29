from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'username': "Nathan"}
  posts= [
    {
      'author': {'username': 'Romeu'},
      'body': 'Au au!'
    },
    {
      'author': {'username': 'Fran'},
      'body': 'Eu sou a bileia!'
    },
    {
      'author': {'username': 'Leandro'},
      'body': 'Só por levantar um muro!'
    }
  ]
  return render_template('index.html', title='Página Inicial', user=user, posts=posts)