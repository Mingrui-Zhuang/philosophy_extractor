from __future__ import annotations

import spacy
from keybert import KeyBERT
import re

from philosophy_extractor.people import (
    load_spacy_model
)

nlp = load_spacy_model()
kw_model = KeyBERT()

def clean_sentence(
    sentence: str
) -> str:
    """
    Remove dates and noisy numbers.
    """

    # Jan 16, January 16
    sentence = re.sub(
        r"\b(?:Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)\s+\d{1,2}\b",
        "",
        sentence,
        flags=re.IGNORECASE
    )

    # standalone numbers
    sentence = re.sub(
        r"\b\d+\b",
        "",
        sentence
    )

    return sentence.strip()

def split_sentences(text: str) -> list[str]:
    """
    Split journal into meaningful sentences.
    """

    doc = nlp(text)

    return [
        sent.text.strip()
        for sent in doc.sents
        if len(sent.text.strip()) > 15
    ]


def extract_events(text: str) -> list[dict]:
    """
    Extract key life events from journal text.
    """

    sentences = split_sentences(text)

    cleaned_sentences = [
        clean_sentence(sentence)
        for sentence in sentences
    ]
    events = []

    for sentence in cleaned_sentences:

        keywords = kw_model.extract_keywords(
            sentence,
            keyphrase_ngram_range=(1, 3),
            stop_words="english",
            top_n=1,
        )

        if not keywords:
            continue

        event_phrase = keywords[0][0]

        events.append(
            {
                "sentence": sentence,
                "event": event_phrase,
            }
        )

    return events