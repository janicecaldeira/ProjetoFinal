from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qovpiolx:ldA1GZtyHZpNnDs-OcjClFO6In5BhivJ@kesavan.db.elephantsql.com/qovpiolx'
db = SQLAlchemy(app)

class Funko(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    funko_name = db.Column(db.String(700), nullable=False)
    funko_img = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    music = db.Column(db.String(500), nullable=True)
    
    def __init__(self, funko_name, funko_img, description, music):
        self.funko_name = funko_name
        self.funko_img = funko_img
        self.description = description
        self.music = music

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        funkos = Funko(
            request.form['funko_name'],
            request.form['funko_img'],
            request.form['description'],
            request.form['music']
        )
    db.session.add(funko)
    db.session.commit()
    flash('Funko adicionado com sucesso!')
    return redirect('/admin')

@app.route('/<id>')
def id(id):
    funkos = Funko.query.get(id)
    return render_template('admin.html', funkos=funkos)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    funkoEdit = Funko.query.get(id)
    if request.method == "POST":
        funkoEdit.funko_name = request.form['funko_name']
        funkoEdit.funko_img = request.form['funko_img']
        funkoEdit.description = request.form['description']
        funkoEdit.music = request.form['music']
        db.session.commit()
        return redirect('/admin')
        return render_template('admin.html', funkoEdit=funkoEdit) 

@app.route('/delete/<id>') 
def delete(id):
    funkos = Funko.query.get(id)
    db.session.delete(funkos)
    db.session.commit()
    return redirect('/admin')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
