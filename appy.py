from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html',title = 'home')

@app.route('/index')
def index():
    return render_template('index.html',title = 'index')


@app.route('/fruits')
def fruits():
    fruits = ["apple","banana","pear"]
    return render_template('fruits.html',title="fruits",fruits=fruits)


@app.route('/favourites')
def favourites():
    favourites = ["eating","holidays","other stuff"]
    return render_template('favourites.html', title="favourites", favourites=favourites)



@app.route('/about')
def about():
    about = ['eating', 'Travel', 'other stuff']
    return render_template('about.html', title = 'about',about = 'about')


if __name__=="__main__":
    app.run(debug=True)









