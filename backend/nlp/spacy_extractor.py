import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):

    doc = nlp(text)

    budget = None
    use_case = None

    for token in doc:
        if token.like_num:
            budget = int(token.text)

        if token.lemma_ == "game":
            use_case = "gaming"

    return {
        "budget": budget,
        "use_case": use_case
    }