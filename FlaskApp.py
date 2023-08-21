from flask import Flask, Response, request, url_for, redirect

app = Flask(__name__)

fruits = []


@app.route('/')
def hello_from_flask():
    return 'Hello from Flask!'


@app.route('/get/text')
def get_text():
    return Response('Hello from Flask using an explicit Response object',mimetype='text/plain')

@app.route('/post/text',methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response('You posted this data to the Flask app:' +data_sent,mimetype='text/plain')

@app.route('/dynamic/<word>')
def home(word):
    return word

@app.route('/square/<int:number>')
def square(number):
    square = number**2
    line = 'Your number squared is '+' '+str(square)
    return line

@app.route('/numbers/<int:num1>/<int:num2>')
def sum(num1,num2):
    sum = num1+num2
    return str(sum)

@app.route('/home/<name>')
def say_hello(name):
    return """
    
    <html>
    <head>
    <title> Sample - Flask Routes </title>
    </head>
    <body>
    <hi>Name page</h1>
    <p>Hello{}</p>
    </html>
    """.format(name)

@app.route('/calculator/<int:num1>/<int:num2>/<operator>')
def calculator(num1,num2,operator):
    if operator == 'add':
        return  str(num1+num2)
    if operator == 'minus':
        return  str(num1-num2)
    if operator == 'divide':
        return  str(num1 / num2)
    if operator == 'multiply':
        return  str(num1 * num2)

@app.route('/fruits/add/<fruit>')
def Addfruit(fruit):
    fruits.append(fruit)
    return fruits

@app.route('/fruits/remove/<fruit>')
def RemoveFruit(fruit):
    fruits.remove(fruit)
    return fruits

@app.route('/home/<username>')
def login(username):
    url = url_for('profile', username=username)

    return """
    
    <html>
    <head>
    <title> ProfilePage for {} </title>
    </head>
    <body>
    
    <h1> You are logged in as {}</h1>
    <p> Click the below link to access your profile</p>
    <a href='{}'>Access Profile</a>
    
    <body>
    </html>
    """.format(username.username.url)



@app.route('/home/userprofile/<username>')
def profile(username):
    return"""
        
    <html>
    <head>
    <title> Welcome to the profile page for {} </title>
    </head>
    <body>
    
    <p> My profile Page -{} </P>
    <p> Username is {} </P>
    </body>
    </html>
    """.format(username, username, username)

@app.route('/home/external')
def external():
    return redirect('https://www.sky.com')


ToDo = []


@app.route('/todo/show')
def todo_show():
    return ToDo


@app.route('/todo/add/<task>')
def todo_add(task):
    ToDo.append(task)
    return ToDo


@app.route('/todo/clear')
def todo_clear():
    ToDo.clear()
    return ToDo


@app.route('/todo/remove/<task>')
def todo_remove(task):
    ToDo.remove(task)
    return ToDo


@app.route('/text/wordcount/<words>')
def text_wordcount(words):
    wordlist = words.split()
    wordcount = str(len(wordlist))
    return wordcount


if __name__ == '__main__':
    app.run(debug=True)


