# recipes for morning anxieties

For my final project, I combined my exploration of storytelling in media with my search for dealing with my anxieties and existential questions. I did so by looking for questions within movie scripts or books and the answers they have for these in the same media. By applying the answers as ingredients in a template of scraped recipes, I managed to concoct drinks that would help alleviate the mental dread with a ritualistic approach.


### 1. recipe scraping
I used [hhursev's](https://github.com/hhursev) [recipe scraper package](https://github.com/hhursev/recipe-scrapers) to get the recipes from the web. For each recipe, you can easily extract many parameters, but I only used the `.ingredients()` and `.instructions()`.

To create a set of instruction templates, I had to extract only the parts that were actual actions. Using spacy's word tags and dependency relations and subtrees, I extracted the actions and replaced all noun chucks with placeholder strings.

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
