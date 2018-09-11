# recipes for morning anxieties

For my final project, I combined my exploration of storytelling in media with my search for dealing with my anxieties and existential questions. I did so by looking for questions within movie scripts or books and the answers they have for these in the same media. By applying the answers as ingredients in a template of scraped recipes, I managed to concoct drinks that would help alleviate the mental dread with a ritualistic approach.



## 1. recipe scraping
I used [hhursev's](https://github.com/hhursev) [recipe scraper package](https://github.com/hhursev/recipe-scrapers) to get the recipes from the web. For each recipe, you can easily extract many parameters, but I only used the `.ingredients()` and `.instructions()`.

To create a set of instruction templates, I had to extract only the parts that were actual actions and their direct objects and prepositions. Using spacy's word tags and dependency relations and subtrees, I extracted the actions (words which `.tag_ == "VB"`), and for every children of the word selected the prepositions (`.dep_ == prep`) and direct objects (`.dep_ == dobj`) to add to the instructions. Also, I replaced all noun chucks with placeholder strings where to put the ingredients later. (The original idea was to use tracery on the final build, but I ended up just using simple string replacements.)

```python
def verb_tracer(s):
    # look for the verb on the sentence
    verb = ""
    for word in s:
        if word.tag_ == "VB":
            verb = word
    # if there's no verb, return ""
    if verb is "":
        return ""
    # if the verb has children, go through them looking for "prep" and "dobj"
    elif len(list(verb.children)) > 0:
        # get the prep
        prep_children = [ch for ch in list(verb.children) if ch.dep_ == "prep"]
        # join them for tracery
        prep_text = " ".join([ch.text+" #np#" for ch in prep_children])
        # get the dobj
        dobj_children = [ch for ch in list(verb.children) if ch.dep_ == "dobj"]
        # joint them as a string
        dobj_text = ""
        for ch in dobj_children:
            dobj_text += " ".join([word.text for word in ch.subtree])
        # get the noun_chunks from the sentence and replace them with
        # a tracery placeholder in the dobj_text
        chunks = s.noun_chunks
        for ch in chunks:
            dobj_text = dobj_text.replace(ch.text, "#np#")
        # return the beautiful phrase
        return verb.text + " " + dobj_text + " " + prep_text
    # else, just return the verb + a tracery placeholder
    else:
        return verb.text+" #np#"
```

To see these experiments and the full procedure go to [the following jupyter notebook](https://github.com/nicolaspe/itp_rwet/blob/master/notebook/recipes_for_/recipe_scraping.ipynb).




## 2. source material
Getting and adapting the source material was one of the most difficult tasks (or at least one of the most daunting). This involved some python usage, but mostly a lot of hand work fixing, editing and even correcting some mistakes along the way. As source material, I used all the Harry Potter books (except The Chamber of Secrets), and the scripts for Star Wars III, V and VII. Sadly, the approach for each source was very different.

#### Harry Potter
This one was the easiest, only because I couldn't go as far as I wanted to. On each file, I simply identified if the line had a quotation mark to discriminate if there was a dialog on the line. As some lines contain text before the dialog, I could not just check if it began with '"'.

```python
dialog = [line.strip() for line in open("harrypotterX.txt").readlines() if '"' in line]
```

The one thing I would have liked to achieve, was separating the dialogs by character and deleting the extra text in the middle of the dialogs (i.e: "character X said abruptly"). The problem with that, is that in many lines more than one character speaks. And given the length and amount of books, I decided that it was not worth the time given the other things I could do to the texts.

#### Star Wars
The Star Wars scripts were much more difficult. There's no standard to which they are transcribed, using different placeholders or separators for completely different things. Also, many have justifies paragraphs that cut the lines with '\n' characters, which makes it harder to know if the line actually ends or not. On the ones I could use, the dialog was filtered with a ':' on the line, or it was separated by four '\t' with the character name separated by six '\t'. This required a lot of manual work, but at least it didn't require me to read the whole script.



## 3. scraping the sources
This was the most difficult part of the project. Each source material is extremely different, yielding a wide array of nouns to be used, some better, some much worse. Deciding between what to use was key on this project.

Again, using spacy's nlp module, I extracted the different noun chucks and entities from each source. Sadly, the noun chunks don't have tags or labels one can use to further discriminate between them. And while such analysis can be done with the entities, the final list of the usable ones was not fulfilling.

```python
[(thing, thing.label_) for thing in hp1_a_nlp.ents if thing.label_ not in ["PERSON", "CARDINAL", "QUANTITY", "ORDINAL", "TIME", "DATE"] ]
```
    [(Tufty, 'NORP'),
     (Majorca, 'GPE'),
     (Aunt Petunia, 'PRODUCT'),
     (Aunt Petunia, 'WORK_OF_ART'),
     (Piers, 'GPE'),
     (Aunt Petunia, 'WORK_OF_ART'),
     (Aunt Petunia, 'WORK_OF_ART'),
     (Aunt Petunia, 'WORK_OF_ART'),
     (Aunt Petunia, 'PRODUCT'),
     (Aunt Petunia, 'PRODUCT'),
     (Uncle Vernon, 'GPE'),
     (London, 'GPE'),
     (Gringotts, 'LOC'),
     (Harry Potter, 'WORK_OF_ART'),
     (D-Defense Against the D-D-Dark Arts, 'WORK_OF_ART'),
     (Gringotts, 'LOC'),
     (Blimey, 'NORP'),
     (King's Cross, 'ORG'),
     (Harry Potter, 'WORK_OF_ART'),
     (Harry Potter, 'WORK_OF_ART'),
     (Starving, 'WORK_OF_ART'),
     (Chocolate Frogs, 'ORG'),
     (Romania, 'GPE'),
     (Africa, 'LOC'),
     (Daily Prophet, 'WORK_OF_ART'),
     (Scabbers, 'ORG'),
     (The Harry Potter, 'WORK_OF_ART'),
     (Malfoy, 'ORG'),
     (Malfoy, 'ORG'),
     (Malfoy, 'ORG'),
     (Wood, 'GPE'),
     (Crabbe, 'ORG'),
     (Malfoy, 'ORG'),
     (Nimbus, 'ORG'),
     (Malfoy, 'ORG'),
     (The Chasers throw the Quaffle, 'WORK_OF_ART'),
     (Wood, 'ORG'),
     (Three Chasers try and score with the Quaffle, 'WORK_OF_ART'),
     (Keeper, 'ORG'),
     (Wood, 'ORG'),
     (POTTER, 'WORK_OF_ART'),
     (Gryffindors, 'ORG'),
     (Greek, 'NORP'),
     ("How many days you got left until yer holidays?, 'WORK_OF_ART'),
     (Slytherin, 'PRODUCT'),
     (Slytherin, 'PRODUCT'),
     (Sorcerer's Stone, 'FAC'),
     (Malfoy, 'ORG'),
     (Potter, 'ORG'),
     (Malfoy, 'ORG'),
     (Fluffy, 'ORG'),
     (Wood, 'WORK_OF_ART'),
     (Filch, 'ORG'),
     (Yeh'll, 'WORK_OF_ART'),
     (Erm, 'ORG'),
     (Mars, 'LOC'),
     (Firenze, 'GPE'),
     (Harry Potter, 'WORK_OF_ART'),
     (Firenze, 'GPE'),
     (The Sorcerer's Stone, 'WORK_OF_ART'),
     (Quirrell, 'ORG'),
     (Quirrell, 'ORG'),
     (Quirrell, 'ORG'),
     (Quirrell, 'ORG'),
     (Quirrell, 'ORG'),
     (Quirrell, 'ORG')]




These experiments and procedure were done in [the following jupyter notebook](https://github.com/nicolaspe/itp_rwet/blob/master/notebook/recipes_for_/scraping_and_word_vecs.ipynb).


### 4.recipes for morning anxieties
The final step was putting everything together. One of my ideas was transforming this into a web application, but it didn't really fit the tone. Nevertheless, that way of thinking was useful to create this last notebook.

I created functions that encapsulate the whole procedure from the recipe scraping, instruction creating and the dialog loading. As I wanted these recipes to answer some of my own problems, I needed to guide their hands. So, the whole text generation depends on an input of my own: what do I want to move away from - which dictates the question; and where do I want to be after - which dictates the ingredients.

This last part was very dependent on word vectors. The source question gets vectorized to get the most similar ones on the source material. This gets accompanied by some lines of my creation (from some previous explorations on anxiety) which in turn use verbs (taken from the questions) that relate to the issue. Then, to move towards the answer, I take the difference of the original vectors (my own input) and add it to the selected question, in order to find a related answer to my problem. From here, I select a list of ingredients and fill in the blanks of the previously parsed instructions. 


```python
def develop_questions(q):
    first_bit = q +" "
    verb_closests = spacy_closest(q_develop, vec(q), 10)
    for i in range(rng.randrange(5,9)):
        first_bit += rng.choice(verb_closests)+" "
        first_bit = first_bit.replace("#qvb#", rng.choice(verbs_q))
    print(first_bit)


def develop_instructions(ingred):
    # select the instructions
    instructions = ''
    for i in range(rng.randrange(3, 5)):
        # select a random instruction
        instructions += rng.choice(instr_body) + rng.choice(a_develop) + '\n'
    # replace the placeholders with ingredients in the order of the list,
    # overflowing if the index goes out of bounds
    ingr_index = 0
    while "#np#" in instructions:
        instructions = instructions.replace("#np#", ingred[ingr_index], 1)
        ingr_index = (ingr_index+1)%len(ingred)
    # add the finishing instruction
    instructions += rng.choice( instr_finish )
    print(instructions)


def get_drink_new(q_target, a_target):
    # == DEFINE FROM DIALOG SOURCE
    # define a question according to the target
    all_questions = spacy_closest_sent( dialog_q, vec(q_target), 5 )
    question = rng.choice( all_questions )
    develop_questions(question)
    # get the target noun_chunk to "solve" and create the solution vector (question to target)
    question_chunks = [ch.text for ch in nlp(question).noun_chunks]
    selected_chunk = rng.choice(question_chunks)
    solution_vector = subtractv(vec(q_target), sentvec(selected_chunk))
    # get the answer noun_chunks > the ingredients
    a_vector = vec(a_target)
    all_ingredients = spacy_closest(ingr_tokens, addv(solution_vector, a_vector), 15)
    # == INGREDIENTS
    # get closest 2 ingredients + 2 random
    ingredients = all_ingredients[0:2]
    ingredients.extend(rng.sample(all_ingredients,2))
    # and write the list with the amounts
    print()
    for ingr in ingredients:
        amnt = rng.randrange(1, 4)
        unit = rng.choice(ingr_units)
        print( str(amnt) + ' ' + unit + ' of ' + ingr )
    # add random extra ingredient
    print( rng.choice(ingr_extra) )
    print('')
    # == INSTRUCTIONS
    # select the instructions
    develop_instructions(ingredients)
    print("\n==========\n")
```
