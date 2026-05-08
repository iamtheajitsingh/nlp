import spacy

nlp = spacy.load("en_core_web_sm")

# collection of news headlines
headlines = [
    "Apple unveils new iPhone in California",
    "Prime Minister Narendra Modi visits New Delhi hospital",
]

# Process each headline and extract named entities
for headline in headlines:
    doc = nlp(headline)
    print(f"\nHeadline: {headline}")
    print("Named Entities:")
    for ent in doc.ents:
        print(f" - {ent.text} ({ent.label_})")
