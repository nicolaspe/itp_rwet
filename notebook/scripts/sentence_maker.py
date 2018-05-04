import random as rng
import pronouncing

nouns = ['aardvark', 'bee', 'sheep', 'cat', 'door', 'dragon']
verbs = ['escapes', 'attacks', 'runs', 'bellows']

for i in range(10):
    nn = rng.choice(nouns)
    rhyme = pronouncing.rhymes(nn)
    rh = rng.choice(rhyme)
    vb = rng.choice(verbs)
    print( 'the ' + nn + ' ' + vb + ' the ' + rh  )
