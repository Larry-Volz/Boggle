from flask import Flask, request, redirect, render_template, session
from unittest import TestCase 
from boggle import Boggle

app=Flask(__name__)
app.config['SECRET_KEY']='7271112'

boggle_game = Boggle()
points = 0
word=""
words=[]


@app.route('/')
def home_instructions():
    return render_template('index.html')

@app.route('/game-start')
def game_start(word=""):
    #make board
    board_cells = boggle_game.make_board()
    #store board in session
    session['board']=board_cells
    print(session['board'])
    #display board on page
    return render_template('game-start.html', board_cells=board_cells, points=points, word=word)

@app.route('/submit_word', methods=['POST'])
def get_word():
    global word
    global words
    global points
    word = request.form['word_input']
    print(f"word is: {word}")

    # TODO: take the form value and check if it is a valid word in the dictionary using the words variable in your app.py.
    board_cells = session['board']
    word_validity = boggle_game.check_valid_word(board_cells, word.lower())

    # TODO: Next, make sure that the word is valid on the board using the check_valid_word function from the boggle.py file.
    word_on_board = boggle_game.find(board_cells, word.upper())
    # TODO: Since you made an AJAX request to your server, you will need to respond with JSON using the jsonify function from Flask.  (N/A because I designed a unique user interface/jquery submitted form instead)
    if word_validity =="ok" and word_on_board == True and word not in words and len(word)>1:
        #DONE: update points
        points += 10**(len(word)-1)
        words.append(word)
        for wrd in words:
            print(f"{wrd}-")
        #TODO: reset the points on game re-start

        # DONE: Send a JSON response which contains either a dictionary of {“result”: “ok”}, {“result”: “not-on-board”}, or {“result”: “not-a-word”}, so the front-end can provide slightly different messages depending if the word is valid or not.
        #DONE: instead of messages I refactored the output field turn green for a correct response and increase the points and red for an incorrect response and not affect the points

        #TODO: make sure 
    else:
        word_validity="not-word"


    # return redirect('game-start')
    
    return render_template('game-start.html', board_cells=board_cells, points=points, word=word, word_validity=word_validity)

@app.route('/reset_board')
def reset_board():
    global points
    points=0
    return redirect('/game-start')
