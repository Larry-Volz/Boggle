from flask import Flask, request, redirect, render_template
from unittest import TestCase 
from boggle import Boggle

app=Flask(__name__)


boggle_game = Boggle()


@app.route('/')
def home_instructions():
    return render_template('index.html')

@app.route('/game-start')
def game_start():
    board_cells = boggle_game.make_board()
    return render_template('game-start.html', board_cells=board_cells)
