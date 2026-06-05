# Philosophy Extractor

A Python command-line tool that extracts personal values and recurring life themes from journal entries.

The tool uses NLP techniques including spaCy named entity recognition, KeyBERT event extraction, semantic clustering with scikit-learn, and Hugging Face zero-shot classification to infer personal philosophy.

## Usage

Install:

uv add git+https://github.com/Mingrui-Zhuang/philosophy_extractor

Run:

philosophy-extractor analyze journal.txt

Custom output report:

philosophy-extractor analyze journal.txt --output my_report.md

## Testing

A sample journal file, `sample_journal.txt`, is included in the repository for quick testing. You can run the analyzer against it with:

philosophy-extractor analyze sample_journal.txt