from flask import Flask
import random as rng

app = Flask(__name__)

greets = ['hello', 'hi', 'salutations', 'hiya']
places = ['region', 'people', 'world', 'planet', 'location']

@app.route('/hello')
def hello():
    greeting = rng.choice(greets) + ' ' + rng.choice(places)
    return greeting

# if __name__ == '__main__':
#     app.run()
app.run()
