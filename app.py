from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'blue'


@app.route('/')
def index():
   session['usuario_logado'] = None
   return render_template('index.html')

@app.route('/catalog')
def catalog():
   session['usuario_logado'] = None
   return render_template('catalog.html')

@app.route('/about')
def about():
   session['usuario_logado'] = None
   return render_template('about.html')

@app.route('/login')
def login():
   session['usuario_logado'] = None
   return render_template('login.html')

@app.route('/adm')
def adm():
   if 'usuario_logado' not in session or session['usuario_logado'] == None:
      flash('Faça login!')
   return redirect('/login')
   
@app.route('/auth', methods=['GET', 'POST'])
def auth():
   if request.form['user'] == 'admin' and request.form['senha'] == '1234':
      session['usuario_logado'] = 'admin'
      flash('Login feito com sucesso!')
      return redirect('/adm')
   else:
      flash('Erro no login, tente novamente!')
      return redirect('/login')

if __name__ == '__main__':
   app.run(debug=True)