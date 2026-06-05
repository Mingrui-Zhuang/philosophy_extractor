# Philosophy Extractor

A Python command-line tool that extracts personal values and recurring life themes from journal entries.

The tool uses NLP techniques including spaCy named entity recognition, KeyBERT event extraction, semantic clustering with scikit-learn, and Hugging Face zero-shot classification to infer personal philosophy.

## Usage

Install:

uv add "git+https://github.com/yourname/repo.git"

Run:

philosophy-extractor analyze journal.txt

Custom output report:

philosophy-extractor analyze journal.txt --output my_report.md