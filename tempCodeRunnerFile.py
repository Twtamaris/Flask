def hello_world():
    return 'This is Awesomeaap!!!'

@app.route('/hello/<name>')
def hehaha(name):
    return f'<h1>This is hello mode {name}</h1>'