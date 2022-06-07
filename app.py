from flask import Flask, render_template

app = Flask(__name__)

@app.route("/adult")
def index():
    adult_books = ['A Walk in the Woods', 'The God of Small Things', 'The Starless Sea', 'The Parable of the Sower']
    return render_template('adult.html', adult_books=adult_books)

@app.route("/kid")
def other():    
    kid_books = [
        {'name': "It's a Book!", 'background':'bg-primary'},
        {'name': "In a Jar", 'background':'bg-white'},
        {'name': "I Talk Like a River", 'background':'bg-info'},
        {'name': "The Paper Bag Princess", 'background':'bg-secondary'},
        {'name': "The Van Gogh Cafe", 'background':'bg-warning'}
        ]
    return render_template('kid.html', kid_books=kid_books)