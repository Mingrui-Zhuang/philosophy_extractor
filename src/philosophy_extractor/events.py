import spacy
from keybert import KeyBERT

nlp = spacy.load("en_core_web_sm")
kw_model = KeyBERT()


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

    events = []

    for sentence in sentences:

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