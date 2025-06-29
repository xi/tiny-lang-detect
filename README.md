# tiny language detection

Language detection libraries like
[langdetect](https://github.com/DoodleBears/langdetect/) usually come with
large models. But if we just want to distinguish between a small set of
languages, the size of the model can be reduce significantly.

This is an experiment to generate tiny models that only contain the most
significant n-grams needed to distinguish between two languages.

Example usage:

```sh
$ ./download_data.sh
$ python gen_model.py en de -n 10 > en_de.json
$ python test.py en_de.json
981 out of 1000 samples were detected correctly (98.1%)
```

A model might look like this:

```json
{
  "ngrams": ["o", "e", "a", "en ", "er", " th", "ch", " t", "en", "ei"],
  "freq": {
    "en": [0.0716, 0.1067, 0.0897, 0.0023, 0.0135, 0.0161, 0.0036, 0.0164, 0.0079, 0.0009],
    "de": [0.0311, 0.1466, 0.0574, 0.0202, 0.0299, 0.0002, 0.0195, 0.0006, 0.0233, 0.0159]
  }
}
```

You can use the model like this:

```py
def probability(p, q):
    return math.prod(qi ** pi * (1 - qi) ** (1 - pi) for pi, qi in zip(p, q))

def classify(model, text):
    n = len(text) + 1
    freq = [text.count(g) / (n - len(g)) for g in model['ngrams']]
    return max(model['freq'], key=lambda lang: probability(freq, model['freq'][lang]))
```

## An even simpler classifier

To take this idea to the exteme, you could reduce the model to the single most
siginificant n-gram:

```py
def classify(text):
    freq = text.count('o') / len(text)
    return 'en' if freq > 0.05 else 'de'
```

This classifier still has an accuracy of 82.1% on the test data.

## How does it work?

`langdetect` works by comparing n-gram frequencies. For example, the 3-gram
" th" is much more common in English than in German.

Before counting n-grams, it does some pre-processing, e.g. removing
punctuation, URLs, or Latin characters in non-Latin texts. Then it uses
Bayesian methods to find the most likely language for those frequencies.

The examples in this repo are much simpler though. They do not do any
pre-processing. This is ultimately a trade-off between accuracy and simplicity.

To simplify the model, `gen_model.py` filters out all but the most significant
n-grams. N-grams are considered more significant if their frequencies have a
large absolute difference between the candidate languages.
