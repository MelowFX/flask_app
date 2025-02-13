from flask import Flask, render_template

app = Flask(__name__)

walkers = [
    {'name': 'Anna', 'location': 'Viljandi', 'availability': '10 AM - 5 PM'},
    {'name': 'Mark', 'location': 'Tartu', 'availability': '8 AM - 2 PM'}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dog-walkers')
def dog_walkers():
    return render_template('dog_walkers.html', walkers=walkers)

if __name__ == '__main__':
    app.run(debug=True)