from flask import Flask, request
import random as rng
import pronouncing

app = Flask(__name__)

@app.route('/rhyme')
def rhyme():
    word_str = request.args['word']
    rhymes = pronouncing.rhymes(word_str.lower())
    if len(rhymes) > 0:
        return (word_str + ' | ' + rng.choice(rhymes))
    else:
        return "no rhymes found  ¯\_(ツ)_/¯"

app.run()
