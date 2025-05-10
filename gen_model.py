import argparse
import json


def get_data(lang):
    with open(f'data/profiles/{lang}') as fh:
        raw = json.load(fh)
    return {k: v / raw['n_words'][len(k) - 1] for k, v in raw['freq'].items()}


def get_model(lang1, lang2, n=8, ndigits=None):
    data1 = get_data(lang1)
    data2 = get_data(lang2)

    ngrams = list(set(data1.keys()) | set(data2.keys()))

    # prioritize by biggest absolute difference
    ngrams.sort(key=lambda k: abs(data1.get(k, 0) - data2.get(k, 0)))
    ngrams = ngrams[-n:]

    return {
        'ngrams': ngrams,
        'freq': {
            lang1: [round(data1.get(g, 0), ndigits) for g in ngrams],
            lang2: [round(data2.get(g, 0), ndigits) for g in ngrams],
        },
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('lang', nargs=2)
    parser.add_argument('-n', type=int, default=8)
    parser.add_argument('-p', type=int, default=4)
    args = parser.parse_args()

    model = get_model(*args.lang, n=args.n, ndigits=args.p)
    print(json.dumps(model))
