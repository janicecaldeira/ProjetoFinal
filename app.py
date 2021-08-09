from flask import Flask, render_template, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'blue'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ldffxgvk:yoOt67_wPlM7TmXSk28a_BXiUXjI8S8e@kesavan.db.elephantsql.com/ldffxgvk'
db = SQLAlchemy(app)

class Funko(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    funkoName = db.Column(db.String(150), nullable=False)
    funkoImg = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    music = db.Column(db.String(500), nullable=True)
    
    def __init__(self, funkoName, funkoImg, description, music):
        self.funkoName = funkoName
        self.funkoImg = funkoImg
        self.description = description
        self.music = music

@app.route('/')
def index():
    session['usuario_logado'] = None
    return render_template('index.html')

@app.route('/catalog')
def catalog():
    session['usuario_logado'] = None
    funko = Funko.query.all()
    return render_template('catalog.html', funko=funko)

@app.route('/about')
def about():
    session['usuario_logado'] = None
    return render_template('about.html')

@app.route('/login')
def login():
    session['usuario_logado'] = None
    return render_template('login.html')

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.form['user'] == 'admin' and request.form['senha'] == '1234':
        session['usuario_logado'] = 'admin'
        flash('Login feito com sucesso!')
        return redirect('/adm')
    else:
        flash('Erro no login, tente novamente!')
        return redirect('/login')

@app.route('/adm')
def adm():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Faça login!')
        return redirect('/login')
    funko = Funko.query.all()
    return render_template('adm.html', funko=funko)
   
@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        funko = Funko(
            request.form['funkoName'],
            request.form['funkoImg'],
            request.form['description'],
            request.form['music']
        )
    db.session.add(funko)
    db.session.commit()
    flash('Funko adicionado com sucesso!')
    return redirect('/adm')

@app.route('/<id>')
def id(id):
    funko = Funko.query.get(id)
    return render_template('adm.html', funko=funko)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    funko = Funko.query.all()
    funkoEdit = Funko.query.get(id)
    if request.method == "POST":
        funkoEdit.funkoName = request.form['funkoName']
        funkoEdit.funkoImg = request.form['funkoImg']
        funkoEdit.description = request.form['description']
        funkoEdit.music = request.form['music']
        db.session.commit()
        return redirect('/adm')
    return render_template('adm.html', funkoEdit=funkoEdit, funko=funko) 

@app.route('/delete/<id>') 
def delete(id):
    funko = Funko.query.get(id)
    db.session.delete(funko)
    db.session.commit()
    return redirect('/adm')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)