from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():
    user = {
        'username': 'siobhankb',
        'email': 'skb@coolio.org'
    }
    return render_template('index.html', user=user)

@app.route("/")

def fave_five():
    adult_books = ['A Walk in the Woods', 'The God of Small Things', 'The Starless Sea', 'The Parable of the Sower']
    kid_books = ["It's a Book!", "In a Jar", "I Talk Like a River", "The Paper Bag Princess", "The Van Gogh Cafe"]
    return render_template('fave_five.html', adult_books=adult_books, kid_books=kid_books)