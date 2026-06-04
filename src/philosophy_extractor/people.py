from collections import Counter
import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")


def extract_people(text: str) -> dict[str, int]:
    """
    Extract PERSON entities and count frequency.
    """

    doc = nlp(text)

    names = []

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text.strip()

            # Simple cleaning rules
            if len(name) < 2:
                continue

            names.append(name)

    counts = Counter(names)

    return dict(counts)