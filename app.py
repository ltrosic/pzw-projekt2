from flask import Flask, render_template, url_for
from forms import SignUpForm
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lozinka'

@app.route('/')
def pocetna():
    return render_template('pocetna.html')

@app.route('/onama')
def onama():
    return render_template('onama.html')

@app.route('/galerija')
def galerija():
    return render_template('galerija.html')

@app.route('/rezervacije')
def rezervacije():
    form = SignUpForm()
    return render_template('rezervacije.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

