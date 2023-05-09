from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, BooleanField, SubmitField

import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class PasswordForm(FlaskForm):
    length = IntegerField('Length:', default=8)
    digits = BooleanField('Include digits?')
    symbols = BooleanField('Include symbols?')
    generate = SubmitField('Generate')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PasswordForm()
    password = None

    if form.validate_on_submit():
        length = form.length.data
        digits = form.digits.data
        symbols = form.symbols.data
        chars = string.ascii_letters
        if digits:
            chars += string.digits
        if symbols:
            chars += string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))

    return render_template('index.html', form=form, password=password)

if __name__ == '__main__':
    app.run(debug=True)
