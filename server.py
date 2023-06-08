from flask import Flask
#, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/') 
def hello_world():
    return 'Hello World!'
#"render_template("index.html"")  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo_name():
    return 'Dojo!'

@app.route('/say/<string:name>')
def hi_name(name):
    return f'Hi {name.title()}!'

@app.route('/repeat/<int:num>/<string:word>')
def repeating_word(num, word):
    repeating_word = word * num
    return repeating_word

@app.errorhandler(404)
def error_found(e):
    return "Sorry! No response. Try again.",404

# @app.route('/say/flask')
# def hi_flask():
#     return f'Hi Flask!'

# @app.route('/say/michael')
# def hi_michael():
#     return f'Hi Michael!'

# @app.route('/say/john')
# def hi_john():
#     return f'Hi John!'


# @app.route()

# @app.route('/hello/<name>')
# def hello_name(name):
#     return f'Hello {name}'

# @app.route('/hello/<name>/<pet>')
# def hello_name_food(name, pet):
#     return f"Hello {name}, and my pet's name it {pet}!"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.

