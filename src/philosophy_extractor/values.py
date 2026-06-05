from collections import defaultdict
from transformers import pipeline


classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

CANDIDATE_VALUES = [
    "Achievement",
    "Curiosity",
    "Belonging",
    "Growth",
    "Autonomy",
    "Security",
    "Connection",
    "Creativity",
    "Meaning",
    "Knowledge",
]


def infer_values(themes: list[dict]) -> list[dict]:
    """
    Infer values and merge duplicate themes.
    """

    value_scores = defaultdict(float)
    value_evidence = defaultdict(list)

    for theme in themes:

        combined_text = " ".join(
            theme["events"]
        )

        prediction = classifier(
            combined_text,
            candidate_labels=CANDIDATE_VALUES,
            multi_label=True,
        )

        # top 3 instead of top 1
        top_labels = prediction[
            "labels"
        ][:3]

        top_scores = prediction[
            "scores"
        ][:3]

        for label, score in zip(
            top_labels,
            top_scores
        ):

            value_scores[label] += (
                score * 10
            )

            value_evidence[
                label
            ].extend(
                theme["events"]
            )

    results = []

    # Normalize scores proportionally to a 0-10 scale
    if value_scores:
        max_score = max(value_scores.values())
    else:
        max_score = 0.0

    for value, score in value_scores.items():
        if max_score > 10:
            normalized = (score / max_score) * 10.0
        else:
            normalized = score

        results.append(
            {
                "value": value,
                "score": round(normalized, 2),
                "events": list(
                    set(
                        value_evidence[
                            value
                        ]
                    )
                )
            }
        )

    return sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )