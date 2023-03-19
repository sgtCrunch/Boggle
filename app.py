from boggle import Boggle
from flask import Flask, render_template, request, jsonify, session


boggle_game = ""

app = Flask(__name__)
app.secret_key = 'app_pass'


@app.route('/')
def home_page():
    global boggle_game
    boggle_game = Boggle()
    if session.get('high_score') == None:
        session['high_score'] = 0

    return render_template('home.html', board = boggle_game.board)

@app.route('/check-answer', methods = ["POST"])
def check_word():

    word = request.json['word']
    result = boggle_game.check_valid_word(word)
    session['score'] = boggle_game.score

    return jsonify({"result" : result, "score" : session['score']})

@app.route('/check-highscore')
def check_high_score():
    
    if session['score'] > session['high_score']:
        result = jsonify({"highscore" : "HIGH SCORE!"})
        session['high_score'] = session['score']
    else:
        result = jsonify({"highscore" : "Not a high score"})

    return result
