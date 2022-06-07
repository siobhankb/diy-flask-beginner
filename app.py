from flask import Flask, render_template

app = Flask(__name__)

@app.route("/adult")
def index():
    adult_books = ['A Walk in the Woods', 'The God of Small Things', 'The Starless Sea', 'The Parable of the Sower']
    return render_template('adult.html', adult_books=adult_books)

@app.route("/kid")
def other():    
    kid_books = ["It's a Book!", "In a Jar", "I Talk Like a River", "The Paper Bag Princess", "The Van Gogh Cafe"]
    return render_template('kid.html', kid_books=kid_books)