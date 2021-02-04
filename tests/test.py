from unittest import TestCase
from app import app
from flask import session, jsonify
from boggle import Boggle
import time

app.config['TESTING']=True
app.config['DEBUG_TB_HOSTS']=['dont-show-debug-toolbar']

b_board = Boggle()

class FlaskTests(TestCase):

    """Tests for view functions / features!"""
    def test_make_board(self):
        self.assertIsInstance(b_board.make_board(),list,"not a list")

    def test_root_route(self):
        with app.test_client() as test_server:
            resp=test_server.get('/')
            html=resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Drag your pointer', html)

    def test_start_timer(self):
        with app.test_client() as test_server:
            resp=test_server.get('/start-timer')
            html=resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 302)

    def test_game_start(self):
        with app.test_client() as test_server:
            with test_server.session_transaction() as change_session:
                change_session['high_score'] = 999

            resp=test_server.get('/game-start')
            html=resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('HighScore:', html)

    def test_submit_word(self):
        with app.test_client() as test_server:
            with test_server.session_transaction() as change_session:
                change_session['high_score'] = 999
                change_session['board'] = [
                    ["H", "A", "P", "P", "Y"], 
                    ["H", "A", "P", "P", "Y"], 
                    ["H", "A", "P", "P", "Y"],  
                    ["H", "A", "P", "P", "Y"], 
                    ["H", "A", "P", "P", "Y"]]
                begun=time.time
                print(f"TIME: {begun}")
                change_session['begun'] = 60

            import pdb
            pdb.set_trace()
            resp=test_server.post('/submit_word', json ={"word_input":"rabbit", "points":"9999"})
            html=resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            # self.assertIn('HighScore:', html)

