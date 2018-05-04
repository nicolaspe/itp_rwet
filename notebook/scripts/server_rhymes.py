from flask import Flask, request, jsonify
import random as rng
import pronouncing

app = Flask(__name__)

@app.route('/rhyme')
def rhyme():
    word_str = request.args['word']
    rhymes = pronouncing.rhymes(word_str.lower())
    return jsonify({'word':word_str, 'rhymes':rhymes})

app.run()
