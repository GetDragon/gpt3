import spacy

nlp = spacy.load("es_core_news_sm")
doc = nlp("Ley 100 de 1980")
print([(w.text, w.pos_) for w in doc])