from __future__ import annotations

from collections import Counter
import spacy

# Load spaCy model once
import spacy
from spacy.cli import download


def load_spacy_model():
    """
    Load spaCy model.
    Download automatically if missing.
    """

    model_name = "en_core_web_sm"

    try:
        return spacy.load(model_name)

    except OSError:
        print(
            "spaCy language model not found."
        )
        print(
            "Downloading "
            "en_core_web_sm..."
        )

        download(model_name)

        return spacy.load(model_name)


nlp = load_spacy_model()


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