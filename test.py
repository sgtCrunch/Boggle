from unittest import TestCase
from app import app
from flask import session, jsonify
from boggle import Boggle
import json

class FlaskTests(TestCase):

    def test_home_page(self):

        with app.test_client() as client:

            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertTrue(session['high_score'] != None)
            self.assertIn('Timer:', html)
    

    def test_check_word(self):

        with app.test_client() as client:
                
            client.get('/')
            resp = client.post('/check-answer',
                            data=json.dumps({'word':'sdfkldjf'}),
                            content_type='application/json')
            data = resp.get_json()

            self.assertEqual(resp.status_code, 200)
            self.assertTrue(session['score'] != None)
            self.assertIn("not-word", data.values())
        

    def test_check_highscore(self):

        with app.test_client() as client:

            with client.session_transaction() as change_session:
                change_session['score'] = 999
                change_session['high_score'] = 0

            resp = client.get('/check-highscore')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(session['high_score'], 999)
            self.assertIn("HIGH SCORE!", html)




    


