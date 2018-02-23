# Flowing frustrations in rebellion
For this assignment, we had to create a text using at least two source texts and the `list` variable type. You can see all the source files in my [GitHub repository](https://github.com/nicolaspe/itp_rwet/tree/master/notebook)

## Sources
In an attempt to join my exploration of authors and topics, I chose some works by the poet Eileen Myles. I read her autobiographical book "Chelsea Girls" last year, and I loved her writing. I used her poems "Peanut Butter" and "Each Defeat". At the same time, I used Emmeline Pankhurst's speech "I Incite this Meeting to Rebellion" as a bank of words.


## Poem in paperspace
First, I wanted to create a poem where the form of the text was important. Wanting to replicate patterns that have formed while doing work in the terminal, I wanted to create on purpose a flow with the structure of the text.

The first stage was creating alternating lines of source material and made up lines with a fixed length, while indenting each line more and more. Each made up line uses words from the word bank, but only the ones that appear four times or less. Also, I had each line begin with the first letter of the previous one. This created the text I liked the most out of these experiments (which had an error in the code, as it read the first character of the previous line, which was a space (' ')):
```
I am always hungry
  incitement importa
    sort. Pleasure eye

        a woman with early

            a woman with other
```

Afterwards, I corrected this mistake and added the possibility of incorporating the overflowing text (result of cutting the lines to a certain length) into the next line.

Even though the code kept getting more and more complex, the results did not please me at all. It took me a long time to have an idea of what to do, but having it turn out so bad was kind of frustrating. I wanted to make the text flow and maybe my ideas should do that too.


### Flowing poems
This time I took a more "musical" approach. I would select words according to the letter they began with. I made three lists of beginning letters:  
```python
l_strong = ['b', 'c', 'p', 't']
l_flow   = ['d', 'f', 'g', 'l', 's']
l_vowel  = ['a', 'e', 'i', 'o', 'u']
```

And then I started mixing lines of poems with each of these words, always accompanied by a word starting with a vowel. I mixed a lot of these experiments, with one or two made-up lines, three poem lines together, etc. In the end, I got something I am satisfied with (finally)

```
one day was
further earnest So whore in
my death. Not
prison opposition
  There
  Take
people Ulster governments evidence disregard
let me move


like a playground
far Ulster go Unlicensed
ride.
teach important my child
  Commons
  Chartists
than And sacrifice other dared
the mail.

```

## Afterthoughts
I feel like I have to learn about natural language processing in order to make stuff that at least makes some sense (or stuff that I could build some sense into). I started using the `nltk` library, but I need to get more into that to use it correctly (specifically the tagging... It failed when I tried to use the `pos_tag()` function).

At the same time, I feel I just need to experiment more in order to have more ideas and a sense of what and how I can create better stuff.
