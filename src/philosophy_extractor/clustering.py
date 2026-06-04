from collections import Counter

from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans


# Small, fast embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def cluster_events(
    events: list[dict],
    n_clusters: int = 3
) -> list[dict]:
    """
    Cluster similar event phrases into themes.
    """

    if len(events) < n_clusters:
        n_clusters = max(1, len(events))

    event_phrases = [
        event["event"]
        for event in events
    ]

    embeddings = embedding_model.encode(
        event_phrases
    )

    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(
        embeddings
    )

    grouped = {}

    for label, event in zip(labels, events):

        grouped.setdefault(
            label,
            []
        ).append(event["event"])

    results = []

    for label, phrases in grouped.items():

        common_words = Counter()

        for phrase in phrases:
            words = phrase.lower().split()
            common_words.update(words)

        summary_word = (
            common_words.most_common(1)[0][0]
        )

        results.append(
            {
                "theme": summary_word.title(),
                "events": phrases,
            }
        )

    return results