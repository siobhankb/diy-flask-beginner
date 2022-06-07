from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():
    adult_books = ['A Walk in the Woods', 'The God of Small Things', 'The Starless Sea', 'The Parable of the Sower']
    kid_books = ["It's a Book!", "In a Jar", "I Talk Like a River", "The Paper Bag Princess", "The Van Gogh Cafe"]
    return render_template('index.html', adult_books=adult_books, kid_books=kid_books)