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


def infer_values(
    themes: list[dict]
) -> list[dict]:
    """
    Infer human values from
    clustered life themes.
    """

    results = []

    for theme in themes:

        combined_text = " ".join(
            theme["events"]
        )

        prediction = classifier(
            combined_text,
            candidate_labels=CANDIDATE_VALUES,
            multi_label=True,
        )

        top_value = prediction[
            "labels"
        ][0]

        top_score = prediction[
            "scores"
        ][0]

        results.append(
            {
                "theme": theme["theme"],
                "value": top_value,
                "score": round(
                    top_score * 10,
                    2
                ),
                "events":
                    theme["events"],
            }
        )

    return results