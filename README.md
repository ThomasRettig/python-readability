# Readability

A simple experiment to find the readability of text. It uses [Textstat](https://github.com/shivam5992/textstat) to readability using a variety of formulas.

## Getting started
This repository requires [Textstat](https://github.com/shivam5992/textstat) and [Rich](https://github.com/Textualize/rich). Install them if you haven’t yet:

```bash
pip install -r requirements.txt
```

After that, run `main.py`:

```bash
python src/main.py
```

## Output

You're output should look similar to this:

```yaml
Flesch reading ease: 46.64
Flesch-Kincaid: 8.7
SMOG index: 9.9
Coleman-Liau index: 12.89
Automated readability: 9.9
Dale-Chall readability score: 9.37
Difficult words: 97
Linsear write formula: 4.076923076923077
Fog scale: 6.28
Reading time: 37.93
```