from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING']=True
app.config['DEBUG_TB_HOSTS']=['dont-show-debug-toolbar']

b_board = Boggle()

class FlaskTests(TestCase):

    """Tests for view functions / features!"""
    def test_make_board(self):
        self.assertIsInstance(b_board.make_board(),list,"is it a")


# self.boggle_game = Boggle()
# self.board_cells = boggle_game.make_board()

# # TODO: Verify if words are confirmed as valid by the dictionary 
# #check upper case, capitalized, lower case, empty string, number
# def test_check_valid_word(self):
#     self.assertTrue(boggle_game.check_valid_word(board_cells, 'rabbit') == True

# TODO: Verify if words are on board 
#use standardized board with specific words

#TODO: Verify each app.route is returning 200 code

#TODO: verify each app.route is getting back the needed form data

#TODO: does EVERY word including individual letters give points?  why?

#TODO: Can you do the same word more than once?  (make words=[])

# def setUp(self):
#     """Stuff to do before every test."""

#     self.client = app.test_client()
#     app.config['TESTING'] = True

# def test_homepage(self):
#     """Make sure information is in the session and HTML is displayed"""

#     with self.client:
#         response = self.client.get('/')
#         self.assertIn('board', session)
#         self.assertIsNone(session.get('highscore'))
#         self.assertIsNone(session.get('nplays'))
#         self.assertIn(b'<p>High Score:', response.data)
#         self.assertIn(b'Score:', response.data)
#         self.assertIn(b'Seconds Left:', response.data)

# def test_valid_word(self):
#     """Test if word is valid by modifying the board in the session"""

#     with self.client as client:
#         with client.session_transaction() as sess:
#             sess['board'] = [["C", "A", "T", "T", "T"], 
#                              ["C", "A", "T", "T", "T"], 
#                              ["C", "A", "T", "T", "T"], 
#                              ["C", "A", "T", "T", "T"], 
#                              ["C", "A", "T", "T", "T"]]
#     response = self.client.get('/check-word?word=cat')
#     self.assertEqual(response.json['result'], 'ok')

# def test_invalid_word(self):
#     """Test if word is in the dictionary"""

#     self.client.get('/')
#     response = self.client.get('/check-word?word=impossible')
#     self.assertEqual(response.json['result'], 'not-on-board')

# def non_english_word(self):
#     """Test if word is on the board"""

#     self.client.get('/')
#     response = self.client.get(
#         '/check-word?word=fsjdakfkldsfjdslkfjdlksf')
#     self.assertEqual(response.json['result'], 'not-word')



