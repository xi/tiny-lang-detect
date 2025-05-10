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
963 out of 1000 samples were detected correctly (96.3%)
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

For examples how to use a model to classify languages, see `test.py` and
`demo/demo.js`.

## How does it work?

`langdetect` works by comparing n-gram frequencies. For example, the 3-gram
" th" is much more common in english than in german.

Before counting n-grams, it does some pre-processing, e.g. removing
punctuation, URLs, or latin characters in non-latin texts. The it uses bayesian
methods to find the most likely language for those frequencies.

The examples in this repo are much simpler though. They do not do any
pre-processing, and they use the euclidean distance to find the best match.
This is ultimately a tradeoff between accuracy and complexity.

To simplify the model, `gen_model.py` filters out all but the most significant
n-grams. N-grams are considered more significant if the absolute difference of
their frequencies in the candidate language is big.
