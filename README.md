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
  "ngrams": ["ei", "en", " t", "ch", " th", "er", "en ", "a", "e", "o"],
  "freq": {
    "en": [0.0009, 0.0079, 0.0164, 0.0036, 0.0161, 0.0135, 0.0023, 0.0897, 0.1067, 0.0716],
    "de": [0.0159, 0.0233, 0.0006, 0.0195, 0.0002, 0.0299, 0.0202, 0.0574, 0.1466, 0.0311]
  }
}
```

For examples how to use a model to classify languages, see `test.py` and
`demo/demo.js`.
