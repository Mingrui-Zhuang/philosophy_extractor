

def generate_report(
    people: dict,
    events: list[dict],
    themes: list[dict],
    values: list[dict],
) -> str:
    """
    Generate a philosophy report.
    """

    report = []

    report.append(
        "# Personal Philosophy Report\n"
    )

    # People
    report.append(
        "## People Mentioned\n"
    )

    if people:
        for name, count in sorted(
            people.items(),
            key=lambda x: x[1],
            reverse=True,
        ):
            report.append(
                f"- {name} ({count})"
            )
    else:
        report.append(
            "No people found."
        )

    # Events
    report.append(
        "\n## Key Events\n"
    )

    for event in events:
        report.append(
            f"- {event['event']}"
        )

    # Themes
    report.append(
        "\n## Themes\n"
    )

    for theme in themes:

        report.append(
            f"\n### "
            f"{theme['theme']}"
        )

        for event in theme[
            "events"
        ]:
            report.append(
                f"- {event}"
            )

    # Values
    report.append(
        "\n## Core Values\n"
    )

    report.append(
        "| Value | Score |"
    )

    report.append(
        "|--------|-------|"
    )

    for value in sorted(
        values,
        key=lambda x: x["score"],
        reverse=True,
    ):
        report.append(
            f"| "
            f"{value['value']} | "
            f"{value['score']} |"
        )

    # Philosophy summary
    report.append(
        "\n## Philosophy Summary\n"
    )

    top_values = [
        v["value"]
        for v in sorted(
            values,
            key=lambda x: x["score"],
            reverse=True,
        )[:3]
    ]

    summary = (
        f"Your journal suggests a strong emphasis "
        f"on {', '.join(top_values[:2])}. "
        f"Repeated reflections indicate these values "
        f"play a meaningful role in how you interpret "
        f"experiences and make sense of challenges."
    )

    if "Achievement" in top_values:
        summary += (
            " A recurring concern with progress, "
            "competence, or goals suggests strong "
            "achievement orientation."
        )

    if "Curiosity" in top_values:
        summary += (
            " Frequent exploration of ideas and "
            "learning suggests intellectual curiosity "
            "is important to you."
        )

    if "Belonging" in top_values:
        summary += (
            " Relationships and emotional connection "
            "appear to play a meaningful role."
        )
    
    if "Growth" in top_values:
        summary += (
            " Reflections on self-improvement and "
            "overcoming challenges suggest growth is "
            "a core value."
        )
    
    if "Autonomy" in top_values:
        summary += (
            " Emphasis on independence and self-direction "
            "indicates autonomy is important to you."
        )
        

    report.append(summary)

    return "\n".join(report)