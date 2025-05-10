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
    "en": [
      0.0008847549205632559,
      0.007865767270512856,
      0.01639325502081986,
      0.0035863210810589343,
      0.016136794462706813,
      0.01354675763365741,
      0.002292672343996773,
      0.0897445255534594,
      0.10672365966622427,
      0.07156346253706898
    ],
    "de": [
      0.015897498950157848,
      0.023261162650169673,
      0.0005690935513966353,
      0.019468205994060662,
      0.00021883618283788822,
      0.02992300137058795,
      0.02022536188476834,
      0.057449835679986086,
      0.14656171354570646,
      0.031128414709526073
    ]
  }
}
```

For examples how to use a model to classify languages, see `test.py` and
`demo/demo.js`.
