import spacy
from spacy.lang.en.examples import sentences

nlp = spacy.load("en_core_web_sm")

def ner(input_text):
    """return named entity tagging"""
    doc = nlp(input_text)

    return [(x.text, x.label_) for x in doc.ents]

def pos_tagging(sentences):
    """return part of speach taggating"""
    doc = nlp(sentences)

    return [(token.text, token.pos_, token.dep_, token.ent_iob_, token.ent_type_) for token in doc]

if __name__ == "__main__":
    print(sentences[0])
    for res in ner(sentences[0]):
        print(res[0], "---->", res[1])
    # for tag in pos_tagging(sentences[0]):
    #     print(tag)