from flask import render_template, flash, redirect, request
from app import app
from forms import RegistrationForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Evgeni'}
    posts = [
        {
            'author':{'nickname':'Petr'},
            'body': 'Day at the races'
        },
        {
            'author':{'nickname':'Sveta'},
            'body': 'Night at the opera'
        }
    ]

    return render_template("Index.html",
                           title = 'Blog',
                           user = user,
                           posts = posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)