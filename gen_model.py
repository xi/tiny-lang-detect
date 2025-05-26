import argparse
import json


def get_data(lang):
    with open(f'data/profiles/{lang}') as fh:
        raw = json.load(fh)
    return {k: v / raw['n_words'][len(k) - 1] for k, v in raw['freq'].items()}


def abs_diff(arr):
    return max(arr) - min(arr)


def get_model(*langs, n=8, ndigits=None):
    data = {lang: get_data(lang) for lang in langs}

    ngrams = set()
    for d in data.values():
        ngrams.update(d.keys())
    ngrams = list(ngrams)

    # prioritize by biggest absolute difference
    ngrams.sort(key=lambda k: -abs_diff([d.get(k, 0) for d in data.values()]))
    ngrams = ngrams[:n]

    return {
        'ngrams': ngrams,
        'freq': {
            lang: [round(d.get(g, 0), ndigits) for g in ngrams]
            for lang, d in data.items()
        },
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('lang', nargs='+')
    parser.add_argument('-n', type=int, default=8)
    parser.add_argument('-p', type=int, default=4)
    args = parser.parse_args()

    model = get_model(*args.lang, n=args.n, ndigits=args.p)
    print(json.dumps(model, ensure_ascii=False))
