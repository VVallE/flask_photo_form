from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(30)


class MyForm(FlaskForm):

    photo = FileField('Photo')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        photo = form.photo.data

        photo.save('uploads/' + photo.filename)
        return 'File Uploaded Successfully'
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
