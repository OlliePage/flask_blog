from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
