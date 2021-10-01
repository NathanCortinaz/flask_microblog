from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash(f'Entrada solicitada para usuário {form.username.data}, remember_me={form.remember_me.data}')
    return redirect(url_for('index'))
  return render_template('login.html', title='Entrar', form=form)