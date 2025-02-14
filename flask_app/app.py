from flask import Flask, render_template, request
import random

app = Flask(__name__)

gamers = [
    {'name': 'Alex', 'game': 'Valorant', 'availability': '6 PM - 10 PM'},
    {'name': 'Chris', 'game': 'League of Legends', 'availability': '3 PM - 8 PM'},
    {'name': 'Jordan', 'game': 'CS2', 'availability': '7 PM - 12 AM'},
    {'name': 'Sam', 'game': 'Valorant', 'availability': '5 PM - 9 PM'}
]

@app.route('/')
def home():
    random_gamer = random.choice(gamers)  # Pick a random gamer for suggestion
    return render_template('home.html', random_gamer=random_gamer)

@app.route('/gamers', methods=['GET'])
def gamers_list():
    selected_game = request.args.get('game')  # Get filter from URL parameter
    filtered_gamers = [g for g in gamers if g['game'] == selected_game] if selected_game else gamers
    return render_template('gamers.html', gamers=filtered_gamers, selected_game=selected_game)

if __name__ == '__main__':
    app.run(debug=True)