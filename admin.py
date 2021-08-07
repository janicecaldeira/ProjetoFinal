from flask import Flask, render_template, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy

admin = Flask(__name__)
admin.secret_key = "udzssq"

admin.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qovpiolx:ldA1GZtyHZpNnDs-OcjClFO6In5BhivJ@kesavan.db.elephantsql.com/qovpiolx'
db = SQLAlchemy(admin)

class Funko(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    funko_name = db.Column(db.String(150), nullable=False)
    funko_img = db.Column(db.String(700), nullable=False)
    description = db.Column(db.String(700), nullable=False)
    music = db.Column(db.String(700), nullable=True)
    
    def __init__(self, funkoName, funkoImg, description, music):
        self.funkoName = funkoName
        self.funkoImg = funkoImg
        self.description = description
        self.music = music
        
@admin.route('/')
def index():
    funko=Funko.query.all()
    return render_template('admin.html', funko=funko)

@admin.route('/new', methods=['GET', 'POST'])
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
    return redirect('/')

@admin.route('/<id>')
def id(id):
    funko = Funko.query.get(id)
    return render_template('admin.html', funko=funko)

@admin.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    funkoEdit = Funko.query.get(id)
    funko=Funko.query.all()
    if request.method == "POST":
        funkoEdit.funkoName = request.form['funkoName']
        funkoEdit.funkoImg = request.form['funkoImg']
        funkoEdit.description = request.form['description']
        funkoEdit.music = request.form['music']
        db.session.commit()
        return redirect('/')
    return render_template('admin.html', funkoEdit=funkoEdit, funko=funko) 

@admin.route('/delete/<id>') 
def delete(id):
    funko = Funko.query.get(id)
    db.session.delete(funko)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
