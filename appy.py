from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/home1')
def home1():
    return render_template('home1.html', title='home1')


@app.route('/index')
def index1():
    return render_template('index1.html', title='index1')


@app.route('/fruits')
def fruits():
    fruits = ["apple", "banana", "pear"]
    return render_template('fruits.html', title="fruits", fruits=fruits)


@app.route('/favourites')
def favourites():
    favourites = ["eating", "holidays", "other stuff"]
    return render_template('favourites.html', title="favourites", favourites=favourites)


@app.route('/about')
def about1():
    about1 = ['eating', 'Travel', 'other stuff']
    return render_template('about1.html', title='about1', about='about1')


if __name__ == "__main__":
    app.run(debug=True)
