from flask import Flask, request, redirect, render_template, session
from unittest import TestCase 
from boggle import Boggle
import time

app=Flask(__name__)
app.config['SECRET_KEY']='7271112'

boggle_game = Boggle()
points = 0
word=""
words=[]
begun=0
high_score=0


@app.route('/')
def home_instructions():
    global high_score
   
    high_score=session.get('high_score', 0)
    session['high_score'] = high_score

    return render_template('index.html')

@app.route('/start-timer')
def start_timer():
    global begun
    global points
    points=0
    begun = time.time()
    session['begun']=begun
    
    # print(f"game begun: {begun}")
    return redirect('/game-start')

@app.route('/game-start')
def game_start(word=""):
    #make board
    board_cells = boggle_game.make_board()
    #store board in session
    session['board']=board_cells
    #display board on page
    return render_template('game-start.html', board_cells=board_cells, points=points, word=word, high_score=session['high_score'])

@app.route('/submit_word', methods=['POST'])
def get_word():
    global word
    global words
    global points
    global high_score
    word = request.form['word_input']

    # TODO: take the form value and check if it is a valid word in the dictionary using the words variable in your app.py.
    board_cells = session['board']
    word_validity = boggle_game.check_valid_word(board_cells, word.lower())

    # DONE: esure word is valid on the board
    word_on_board = boggle_game.find(board_cells, word.upper())
    
    if word_validity =="ok" and word_on_board == True and word not in words and len(word)>1:
        #DONE: update points
        points += 10**(len(word)-1)
        words.append(word)

        if points > session['high_score'] :
            session['high_score'] = points

        #DONE: reset the points on game re-start

        #DONE: Send a JSON response which contains either a dictionary of {“result”: “ok”}, {“result”: “not-on-board”}, or {“result”: “not-a-word”}, so the front-end can provide slightly different messages depending if the word is valid or not.
        #DONE: instead of messages I refactored the output field turn green for a correct response and increase the points and red for an incorrect response and not affect the points

        #TODO: make sure 
    else:
        word_validity="not-word"
    high_score=session['high_score']

    #timer up?
    if time.time()-float(session['begun']) > 60:
        set_all_scores(points)
        return render_template('game-over.html', points=points, high_score=high_score)

    # return redirect('game-start')
    return render_template('game-start.html', board_cells=board_cells, points=points, word=word, word_validity=word_validity, high_score=session['high_score'])

@app.route('/reset_board')
def reset_board():
    global points
    points=0
    return redirect('/start-timer')

@app.route('/game-over')
def game_over():
    global points
    request.args.get(points,0)
    high_score=session['high_score']
   
    return render_template('game-over.html', points=points, high_score=high_score)


def set_all_scores(points):
    """for future development - sort, add game boards and allow others to play the same game with same letters later"""
    all_scores=[]
    all_scores= session.get('all_scores',[0])
    all_scores.append(points)
    session['all_scores'] = all_scores
    for ea in all_scores:
        print(f"score: {ea}")
    print(f"high_score from game_over: {high_score}")
    return all_scores