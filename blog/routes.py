from flask import render_template, url_for, flash, redirect
from blog.forms import RegistrationForm, LoginForm
from blog import app

posts = [
    {
        'author': 'Ollie Page',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': '2020-11-30'
    },
    {
        'author': 'Jane Page',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': '2020-12-01'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your details', 'danger')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

