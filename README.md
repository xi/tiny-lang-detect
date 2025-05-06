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
overall correctness 96.3% (1000)
```

For examples how to use a model to classify languages, see `test.py` and
`demo/demo.js`.
