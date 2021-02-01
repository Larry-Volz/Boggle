from flask import Flask, request, redirect, render_template, session
from unittest import TestCase 
from boggle import Boggle

app=Flask(__name__)
app.config['SECRET_KEY']='7271112'

boggle_game = Boggle()


@app.route('/')
def home_instructions():
    return render_template('index.html')

@app.route('/game-start')
def game_start():
    #make board
    board_cells = boggle_game.make_board()
    #store board in session
    session['board']=board_cells
    print(session['board'])
    #display board on page
    return render_template('game-start.html', board_cells=board_cells)
