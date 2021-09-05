import stanza
stanza.download('ar', processors={'ner': 'AQMAR'})
nlp = stanza.Pipeline('ar', processors={'ner': 'AQMAR'})