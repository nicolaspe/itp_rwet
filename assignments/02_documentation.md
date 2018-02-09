# Computer-aided poetry

For this assignment, we had to create our own poetry generator by modifying some well-known that already exist. The following ones were recoded from [Allison Parrish's](http://www.decontextualize.com/) [poetry generator examples](https://github.com/aparrish/rwet/blob/master/some-poetry-generators.ipynb).


## Dadaist terror
My first approach was to use the Dadaist poem generator with on of my own texts, in order to loosen myself and start experimenting. I chose ["Sometimes I forget"](https://inintocable.wordpress.com/2017/09/13/sometimes-i-forget/), a poem I wrote last September, for this experiment. I edited output by creating paragraphs in an attempt to add some cadence and hint as to how I'd read it.

```
fine
I'm don't
my world only But Even fault on you
soul face artificial
forget with I'll to farce
wondering The false Makes anything happier I'm
you've This hope
is that your
nothing with been easier
Cause entirely words not through forget
A concentrate-made appear
And That I'm uncertainty
happiness is fine
sure was forget farce
What-ifs makes admit
Still, I on this is me
a that I not your My I And before all
This hold the And life to same
it's it of I joy
This I else
my of I false soothes sometimes
with want I caffeine-free glimmer
It's it Ignoring
A killed for all
chose Sometimes the ignored
which coincidental get
if all
```


## Gorge of insanity
I did a reinvention of [Nick Montfort](http://nickm.com/)'s [Taroko Gorge](http://nickm.com/taroko_gorge/) in order to have a different approach, adding some sense of intimate storytelling.

My writing is often cathartic, taking elements that wander through my mind and exaggerating, deforming and mixing them with completely fictional fragments. As the words are selected by the algorithm, I tried to create a set of objects, descriptions and actions that go back and forth happiness and misery.

The code is divided in five functions: one to generate the introductory line, another for the verses, the bridge and outro and the last one to generate the poem itself.

```
My coins are noble
   listen to my vase
      enlightenment
   hold the pillow
   dream

... cigars are insane
   swim through his bed
      rejection
   don't forget the table
   just die

Their memories are suppressed
   bury your floor
   read...
      destruction
   steal the floor
   stay

Their memories are passionate
   face your floor
   enter...
      enlightenment
   look at the VCR
   just die

His arguments are intense
   listen to her desk
      wounded
   steal the VCR
   leave

Your memories are naked
   stamp my radio
   incinerate...
      wounded of the feelings
   sleep next to the table
   dream

My memories are passionate
   bury their book
      rejection
   hold the table
   dream
```


The jupyter notebook file can be seen [here](https://github.com/nicolaspe/itp_rwet/blob/master/notebook/02_poetry_generation.ipynb).
